from pyspark.sql import SparkSession
from pyspark.sql.functions import col, coalesce, expr, explode
from pyspark.sql.functions import col, coalesce, expr, explode, lit,when
from pyspark.sql.types import ArrayType, StructType


def build_spark(app_name="dnb-xml-parse"):
    # adjust spark.jars.packages if you need to pull spark-xml dynamically
    return SparkSession.builder \
        .appName(app_name) \
        .config("spark.sql.legacy.allowUntypedScalaUDF", "true") \
        .config("spark.jars.packages", "com.databricks:spark-xml_2.12:0.17.0")\
        .getOrCreate()

def parse_xml_file(spark, xml_path, standardize_address=1, response_type='IdentityDetail'):
    # read XML where each <Results> element is one row
    df = spark.read.format("xml").option("rowTag", "Results").load(xml_path)
    resp = (response_type or 'IdentityDetail')
    std_flag = int(standardize_address or 1)

    # helpers to safely reference nested/array fields in the inferred schema
    def path_exists(schema, dotted_path):
        if not dotted_path:
            return False
        parts = dotted_path.split(".")
        cur = schema
        for i, p in enumerate(parts):
            found = None
            if hasattr(cur, "fields"):
                for f in cur.fields:
                    if f.name == p:
                        found = f
                        break
            if found is None:
                return False
            dt = found.dataType
            if isinstance(dt, ArrayType):
                dt = dt.elementType
            # if not a struct but not the last part, can't continue
            if not isinstance(dt, StructType) and i != len(parts) - 1:
                return False
            cur = dt
        return True

    def get_type(schema, dotted_path):
        if not dotted_path:
            return None
        parts = dotted_path.split(".")
        cur = schema
        for p in parts:
            found = None
            if hasattr(cur, "fields"):
                for f in cur.fields:
                    if f.name == p:
                        found = f
                        break
            if found is None:
                return None
            cur = found.dataType
            if isinstance(cur, ArrayType):
                cur = cur.elementType
        return cur

    def safe_col(schema, dotted_path):
        # return col(dotted_path) if path exists in schema, otherwise lit(None)
        if path_exists(schema, dotted_path):
            return col(dotted_path)
        return lit(None)

    def safe_collection_expr(schema, base_path, array_expr_tpl, struct_expr_tpl):
        dt = get_type(schema, base_path)
        if dt is None:
            return lit(None)
        if isinstance(dt, ArrayType):
            return expr(array_expr_tpl)
        if isinstance(dt, StructType):
            # struct expression template should reference the struct directly (no lambda)
            return expr(struct_expr_tpl)
        return lit(None)

    # Identity branch: explode matchCandidates
    if resp == 'Identity':
        mc = df.select(explode(col("matchCandidates")).alias("mc"))
        base = mc.select(col("mc.organization").alias("org"), col("mc.matchQualityInformation").alias("mq"))
        base_schema = base.schema

        def regnum_expr_safe(prefix, code):
            base_path = f"{prefix}.registrationNumbers"
            array_tpl = f"element_at(filter({prefix}.registrationNumbers, x -> x.typeDnBCode = '{code}'), 1).registrationNumber"
            struct_tpl = f"{prefix}.registrationNumbers.registrationNumber"
            return safe_collection_expr(base_schema, base_path, array_tpl, struct_tpl)

        def industry_code_safe(prefix, code, priority='1'):
            base_path = f"{prefix}.industryCodes"
            array_tpl = f"element_at(filter({prefix}.industryCodes, x -> x.typeDnBCode = '{code}' AND x.priority = '{priority}'),1).code"
            struct_tpl = f"{prefix}.industryCodes.code"
            return safe_collection_expr(base_schema, base_path, array_tpl, struct_tpl)

        def industry_descr_safe(prefix, code, priority='1'):
            base_path = f"{prefix}.industryCodes"
            array_tpl = f"element_at(filter({prefix}.industryCodes, x -> x.typeDnBCode = '{code}' AND x.priority = '{priority}'),1).description"
            struct_tpl = f"{prefix}.industryCodes.description"
            return safe_collection_expr(base_schema, base_path, array_tpl, struct_tpl)

        def trade_style_safe(prefix):
            base_path = f"{prefix}.tradeStyleNames"
            array_tpl = f"element_at(filter({prefix}.tradeStyleNames, x -> x.priority = '1'),1).name"
            struct_tpl = f"{prefix}.tradeStyleNames.name"
            return safe_collection_expr(base_schema, base_path, array_tpl, struct_tpl)

        sel = base.select(
            safe_col(base_schema, "org.duns").alias("Duns"),
            regnum_expr_safe("org", "6863").alias("FEIN"),
            regnum_expr_safe("org", "1372").alias("CRN"),
            safe_col(base_schema, "org.corporateLinkage.globalUltimate.duns").alias("GlobalUltimateDuns"),
            safe_col(base_schema, "org.corporateLinkage.globalUltimate.primaryName").alias("GlobalUltimateDunsName"),
            safe_col(base_schema, "org.corporateLinkage.domesticUltimate.duns").alias("DomesticUltimateDuns"),
            safe_col(base_schema, "org.corporateLinkage.domesticUltimate.primaryName").alias("DomesticUltimateDunsName"),
            safe_col(base_schema, "org.corporateLinkage.parent.duns").alias("ParentDuns"),
            safe_col(base_schema, "org.corporateLinkage.parent.primaryName").alias("ParentDunsName"),
            safe_col(base_schema, "org.primaryName").alias("PrimaryName"),
            safe_col(base_schema, "org.dunsControlStatus.isMarketable").alias("IsMarketable"),
            industry_code_safe("org", "30832").alias("NAICSCode"),
            industry_descr_safe("org", "30832").alias("NAICSCodeDescription"),
            when(
                coalesce(safe_col(base_schema, "org.corporateLinkage.hierarchyLevel"), lit(None)) == '1',
                lit('false')
            ).otherwise(lit('true')).alias("SubsidiaryStatus"),  # { changed code }
            safe_col(base_schema, "org.fax.isdCode").alias("FaxNumberCountryCode"),
            safe_col(base_schema, "org.fax.telephoneNumber").alias("FaxAreaCodePhoneNumber"),
            safe_col(base_schema, "org.telephone.isdCode").alias("PhoneNumberCountryCode"),
            safe_col(base_schema, "org.telephone.telephoneNumber").alias("PhoneAreaCodePhoneNumber"),
            safe_col(base_schema, "org.websiteAddress.url").alias("URL"),
            safe_col(base_schema, "org.primaryAddress.streetAddress.line1").alias("AddressLine1"),
            safe_col(base_schema, "org.primaryAddress.streetAddress.line2").alias("AddressLine2"),
            safe_col(base_schema, "org.primaryAddress.addressLocality.name").alias("City"),
            safe_col(base_schema, "org.primaryAddress.addressRegion.abbreviatedName").alias("State"),
            safe_col(base_schema, "org.primaryAddress.addressCountry.name").alias("Country"),
            safe_col(base_schema, "org.primaryAddress.addressCountry.isoAlpha2Code").alias("ISOCountryCode"),
            safe_col(base_schema, "org.primaryAddress.postalCode").alias("PostalCode"),
            safe_col(base_schema, "org.primaryAddress.postalCodeExtension").alias("PostalCodeExtension"),
            safe_col(base_schema, "org.primaryAddress.latitude").alias("Latitude"),
            safe_col(base_schema, "org.primaryAddress.longitude").alias("Longitude"),
            safe_col(base_schema, "mq.confidenceCode").cast("int").alias("ConfidenceCode"),
            safe_col(base_schema, "mq.matchGrade").alias("MatchGradeString"),
            expr("NULL").alias("AddressType"),
            safe_col(base_schema, "org.corporateLinkage.familytreeRolesPlayed.description").alias("FamilyTreeRolesPlayed"),
            trade_style_safe("org").alias("DBAName"),
            industry_code_safe("org", "399").alias("SICCode"),
            industry_descr_safe("org", "399").alias("SICCodeDescription"),
            industry_code_safe("org", "3599").alias("SIC8Code"),
            industry_descr_safe("org", "3599").alias("SIC8CodeDescription")
        )
        return sel

    # IdentityDetail or Enrich: use Results row as base
    r = df.alias("r")
    r_schema = df.schema

    def regnum_expr_top(prefix, code):
        base_path = f"{prefix}.registrationNumbers"
        array_tpl = f"element_at(filter({prefix}.registrationNumbers, x -> x.typeDnBCode = '{code}'), 1).registrationNumber"
        struct_tpl = f"{prefix}.registrationNumbers.registrationNumber"
        return safe_collection_expr(r_schema, base_path, array_tpl, struct_tpl)

    def industry_code_top(prefix, code, priority='1'):
        base_path = f"{prefix}.industryCodes"
        array_tpl = f"element_at(filter({prefix}.industryCodes, x -> x.typeDnBCode = '{code}' AND x.priority = '{priority}'),1).code"
        struct_tpl = f"{prefix}.industryCodes.code"
        return safe_collection_expr(r_schema, base_path, array_tpl, struct_tpl)

    def industry_descr_top(prefix, code, priority='1'):
        base_path = f"{prefix}.industryCodes"
        array_tpl = f"element_at(filter({prefix}.industryCodes, x -> x.typeDnBCode = '{code}' AND x.priority = '{priority}'),1).description"
        struct_tpl = f"{prefix}.industryCodes.description"
        return safe_collection_expr(r_schema, base_path, array_tpl, struct_tpl)

    def trade_style_top(prefix):
        base_path = f"{prefix}.tradeStyleNames"
        array_tpl = f"element_at(filter({prefix}.tradeStyleNames, x -> x.priority = '1'),1).name"
        struct_tpl = f"{prefix}.tradeStyleNames.name"
        return safe_collection_expr(r_schema, base_path, array_tpl, struct_tpl)

    def pick_addr(field):
        candidates = []
        if resp == 'IdentityDetail' and std_flag == 1:
            candidates.append(f"r.cleanseAndStandardizeInformation.standardizedAddress.{field}")
        candidates.append(f"r.embeddedProduct.organization.primaryAddress.{field}")
        candidates.append(f"r.organization.primaryAddress.{field}")
        cols = []
        for c in candidates:
            p = c[len("r."):] if c.startswith("r.") else c
            cols.append(safe_col(r_schema, p))
        if len(cols) == 1:
            cols.append(lit(None))
        return coalesce(*cols)

    sel = r.select(
        coalesce(safe_col(r_schema, "embeddedProduct.organization.duns"), safe_col(r_schema, "organization.duns")).alias("Duns"),
        regnum_expr_top("embeddedProduct.organization", "6863").alias("FEIN"),
        regnum_expr_top("embeddedProduct.organization", "1372").alias("CRN"),
        coalesce(safe_col(r_schema, "embeddedProduct.organization.corporateLinkage.globalUltimate.duns"),
                 safe_col(r_schema, "organization.corporateLinkage.globalUltimate.duns")).alias("GlobalUltimateDuns"),
        coalesce(safe_col(r_schema, "embeddedProduct.organization.corporateLinkage.globalUltimate.primaryName"),
                 safe_col(r_schema, "organization.corporateLinkage.globalUltimate.primaryName")).alias("GlobalUltimateDunsName"),
        coalesce(safe_col(r_schema, "embeddedProduct.organization.corporateLinkage.domesticUltimate.duns"),
                 safe_col(r_schema, "organization.corporateLinkage.domesticUltimate.duns")).alias("DomesticUltimateDuns"),
        coalesce(safe_col(r_schema, "embeddedProduct.organization.corporateLinkage.domesticUltimate.primaryName"),
                 safe_col(r_schema, "organization.corporateLinkage.domesticUltimate.primaryName")).alias("DomesticUltimateDunsName"),
        coalesce(safe_col(r_schema, "embeddedProduct.organization.corporateLinkage.parent.duns"),
                 safe_col(r_schema, "organization.corporateLinkage.parent.duns")).alias("ParentDuns"),
        coalesce(safe_col(r_schema, "embeddedProduct.organization.corporateLinkage.parent.primaryName"),
                 safe_col(r_schema, "organization.corporateLinkage.parent.primaryName")).alias("ParentDunsName"),
        coalesce(safe_col(r_schema, "embeddedProduct.organization.primaryName"), safe_col(r_schema, "organization.primaryName")).alias("PrimaryName"),
        coalesce(safe_col(r_schema, "embeddedProduct.organization.dunsControlStatus.isMarketable"),
                 safe_col(r_schema, "organization.dunsControlStatus.isMarketable")).alias("IsMarketable"),
        industry_code_top("embeddedProduct.organization", "30832").alias("NAICSCode"),
        industry_descr_top("embeddedProduct.organization", "30832").alias("NAICSCodeDescription"),
        when(
            coalesce(
                safe_col(r_schema, "embeddedProduct.organization.corporateLinkage.hierarchyLevel"),
                safe_col(r_schema, "organization.corporateLinkage.hierarchyLevel")
            ) == '1',
            lit('false')
        ).otherwise(lit('true')).alias("SubsidiaryStatus"),  # { changed code }
        coalesce(safe_col(r_schema, "embeddedProduct.organization.fax.isdCode"), safe_col(r_schema, "organization.fax.isdCode")).alias("FaxNumberCountryCode"),
        coalesce(safe_col(r_schema, "embeddedProduct.organization.fax.telephoneNumber"), safe_col(r_schema, "organization.fax.telephoneNumber")).alias("FaxAreaCodePhoneNumber"),
        coalesce(safe_col(r_schema, "embeddedProduct.organization.telephone.isdCode"), safe_col(r_schema, "organization.telephone.isdCode")).alias("PhoneNumberCountryCode"),
        coalesce(safe_col(r_schema, "embeddedProduct.organization.telephone.telephoneNumber"), safe_col(r_schema, "organization.telephone.telephoneNumber")).alias("PhoneAreaCodePhoneNumber"),
        coalesce(safe_col(r_schema, "embeddedProduct.organization.websiteAddress.url"), safe_col(r_schema, "organization.websiteAddress.url")).alias("URL"),
        pick_addr("streetAddress.line1").alias("AddressLine1"),
        pick_addr("streetAddress.line2").alias("AddressLine2"),
        pick_addr("addressLocality.name").alias("City"),
        pick_addr("addressRegion.abbreviatedName").alias("State"),
        pick_addr("addressCountry.name").alias("Country"),
        pick_addr("addressCountry.isoAlpha2Code").alias("ISOCountryCode"),
        pick_addr("postalCode").alias("PostalCode"),
        pick_addr("postalCodeExtension").alias("PostalCodeExtension"),
        coalesce(safe_col(r_schema, "embeddedProduct.organization.primaryAddress.latitude"), safe_col(r_schema, "organization.primaryAddress.latitude")).alias("Latitude"),
        coalesce(safe_col(r_schema, "embeddedProduct.organization.primaryAddress.longitude"), safe_col(r_schema, "organization.primaryAddress.longitude")).alias("Longitude"),
        coalesce(safe_col(r_schema, "matchCandidates.matchQualityInformation.confidenceCode"), safe_col(r_schema, "matchQualityInformation.confidenceCode")).cast("int").alias("ConfidenceCode"),
        coalesce(safe_col(r_schema, "matchCandidates.matchQualityInformation.matchGrade"), safe_col(r_schema, "matchQualityInformation.matchGrade")).alias("MatchGradeString"),
        coalesce(safe_col(r_schema, "cleanseAndStandardizeInformation.standardizedAddress.addressType"), safe_col(r_schema, "matchQualityInformation.addressType"), safe_col(r_schema, "organization.addressType")).alias("AddressType"),
        coalesce(safe_col(r_schema, "matchCandidates.organization.corporateLinkage.familytreeRolesPlayed.description"),
                 safe_col(r_schema, "organization.corporateLinkage.familytreeRolesPlayed.description"),
                 safe_col(r_schema, "embeddedProduct.organization.corporateLinkage.familytreeRolesPlayed.description")).alias("FamilyTreeRolesPlayed"),
        trade_style_top("embeddedProduct.organization").alias("DBAName"),
        industry_code_top("embeddedProduct.organization", "399").alias("SICCode"),
        industry_descr_top("embeddedProduct.organization", "399").alias("SICCodeDescription"),
        industry_code_top("embeddedProduct.organization", "3599").alias("SIC8Code"),
        industry_descr_top("embeddedProduct.organization", "3599").alias("SIC8CodeDescription")
    )

    if resp == 'Enrich':
        # re-select forcing organization.* precedence
        org_sel = df.selectExpr(
            "organization.duns as Duns",
            "element_at(filter(organization.registrationNumbers, x -> x.typeDnBCode='6863'),1).registrationNumber as FEIN",
            "element_at(filter(organization.registrationNumbers, x -> x.typeDnBCode='1372'),1).registrationNumber as CRN",
            "organization.corporateLinkage.globalUltimate.duns as GlobalUltimateDuns",
            "organization.corporateLinkage.globalUltimate.primaryName as GlobalUltimateDunsName",
            "organization.corporateLinkage.domesticUltimate.duns as DomesticUltimateDuns",
            "organization.corporateLinkage.domesticUltimate.primaryName as DomesticUltimateDunsName",
            "organization.corporateLinkage.parent.duns as ParentDuns",
            "organization.corporateLinkage.parent.primaryName as ParentDunsName",
            "organization.primaryName as PrimaryName",
            "organization.dunsControlStatus.isMarketable as IsMarketable",
            "element_at(filter(organization.industryCodes, x -> x.typeDnBCode='30832' AND x.priority='1'),1).code as NAICSCode",
            "element_at(filter(organization.industryCodes, x -> x.typeDnBCode='30832' AND x.priority='1'),1).description as NAICSCodeDescription",
            "CASE WHEN organization.corporateLinkage.hierarchyLevel = '1' THEN 'false' ELSE 'true' END as SubsidiaryStatus",
            "organization.fax.isdCode as FaxNumberCountryCode",
            "organization.fax.telephoneNumber as FaxAreaCodePhoneNumber",
            "organization.telephone.isdCode as PhoneNumberCountryCode",
            "organization.telephone.telephoneNumber as PhoneAreaCodePhoneNumber",
            "organization.websiteAddress.url as URL",
            "organization.primaryAddress.streetAddress.line1 as AddressLine1",
            "organization.primaryAddress.streetAddress.line2 as AddressLine2",
            "organization.primaryAddress.addressLocality.name as City",
            "organization.primaryAddress.addressRegion.abbreviatedName as State",
            "organization.primaryAddress.addressCountry.name as Country",
            "organization.primaryAddress.addressCountry.isoAlpha2Code as ISOCountryCode",
            "organization.primaryAddress.postalCode as PostalCode",
            "organization.primaryAddress.postalCodeExtension as PostalCodeExtension",
            "organization.primaryAddress.latitude as Latitude",
            "organization.primaryAddress.longitude as Longitude",
            "matchQualityInformation.confidenceCode as ConfidenceCode",
            "matchQualityInformation.matchGrade as MatchGradeString",
            "organization.addressType as AddressType",
            "organization.corporateLinkage.familytreeRolesPlayed.description as FamilyTreeRolesPlayed",
            "element_at(filter(organization.tradeStyleNames, x -> x.priority='1'),1).name as DBAName",
            "element_at(filter(organization.industryCodes, x -> x.typeDnBCode='399' AND x.priority='1'),1).code as SICCode",
            "element_at(filter(organization.industryCodes, x -> x.typeDnBCode='399' AND x.priority='1'),1).description as SICCodeDescription",
            "element_at(filter(organization.industryCodes, x -> x.typeDnBCode='3599' AND x.priority='1'),1).code as SIC8Code",
            "element_at(filter(organization.industryCodes, x -> x.typeDnBCode='3599' AND x.priority='1'),1).description as SIC8CodeDescription"
        )
        return org_sel

    return sel


def main():
    # hardcoded for now
    xml_path = r"D:\pythonProject\support\rawxml.xml"
    standardize = 1
    response_type = "IdentityDetail"

    spark = build_spark()
    df = parse_xml_file(spark, xml_path, standardize_address=standardize, response_type=response_type)
    df.show(truncate=False)
    spark.stop()

if __name__ == "__main__":
    main()
# ...existing code...