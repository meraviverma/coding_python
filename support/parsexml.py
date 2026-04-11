from pyspark.sql import functions as F
from pyspark.sql import SparkSession
# Parameters to mimic the T-SQL UDF’s inputs
standardize_address = 1                 # 1 or 0 (equivalent to @StandardizeAddress)
response_type = "IdentityDetail"        # "IdentityDetail" | "Enrich" | "Identity"

# Initialize SparkSession with spark-xml package
builder = SparkSession.builder \
    .appName("Read XML Example") \
    .config("spark.jars.packages", "com.databricks:spark-xml_2.12:0.17.0")

spark=builder.getOrCreate()

xml_path=r"D:\pythonProject\support\rawxml.xml"
# Read the XML (top-level row is <Results>)
df = (
    spark.read.format("xml")
    .option("rowTag", "Results")
    .option("treatEmptyValuesAsNulls", "true")
    .option("primitivesAsString", "true")     # keep raw strings (safer for IDs/codes)
    .load(xml_path)
)

# Helpers to safely access possibly-missing structs/arrays
def first_or_null(expr_str):
    """Return expr_str[0] if array has at least one element, else null."""
    return F.expr(f"CASE WHEN {expr_str} IS NOT NULL AND size({expr_str}) > 0 THEN {expr_str}[0] ELSE NULL END")

# Industry code helpers (match by typeDnBCode and priority)
def industry_field(base, type_code, priority, field):
    # base is a string path to *.industryCodes (array)
    return F.expr(f"""
        CASE 
          WHEN {base} IS NOT NULL THEN
            element_at(
              transform(
                filter({base}, x -> x.typeDnBCode = '{type_code}' AND cast(x.priority as string) = '{priority}'),
                x -> x.{field}
              ), 1
            )
          ELSE NULL
        END
    """)

# tradeStyleNames priority=1 (DBA)
def trade_style_name(base):
    # base is path to *.tradeStyleNames (array)
    return F.expr(f"""
        CASE 
          WHEN {base} IS NOT NULL THEN
            element_at(
              transform(
                filter({base}, x -> cast(x.priority as string) = '1'),
                x -> x.name
              ), 1
            )
          ELSE NULL
        END
    """)

# Choose the “organization” node based on ResponseType, with fallbacks
org_emb = F.col("embeddedProduct.organization")
org_id  = F.col("organization")  # present in Enrich/Identity responses

# Address sources per the T-SQL union logic
addr_std = F.col("cleanseAndStandardizeInformation.standardizedAddress")
addr_emb = F.col("embeddedProduct.organization.primaryAddress")
addr_id  = F.col("organization.primaryAddress")

address_source = (
    F.when((F.lit(response_type) == F.lit("IdentityDetail")) & (F.lit(standardize_address) == 1), addr_std)
     .when((F.lit(response_type) == F.lit("IdentityDetail")) & (F.lit(standardize_address) == 0), addr_emb)
     .otherwise(F.coalesce(addr_id, addr_emb))
)

# Family tree role description present in multiple places; coalesce across likely locations
family_tree_desc = F.coalesce(
    F.col("matchCandidates.organization.corporateLinkage.familytreeRolesPlayed.description"),
    F.col("organization.corporateLinkage.familytreeRolesPlayed.description"),
    F.col("embeddedProduct.organization.corporateLinkage.familytreeRolesPlayed.description")
)

# Match quality (different placements)
confidence_code = F.coalesce(
    F.col("matchCandidates.matchQualityInformation.confidenceCode"),
    F.col("matchQualityInformation.confidenceCode")
)
match_grade = F.coalesce(
    F.col("matchCandidates.matchQualityInformation.matchGrade"),
    F.col("matchQualityInformation.matchGrade")
)

# Build a single flattened select that mirrors your T-SQL output
df_flat = df.select(
    # DUNS (prefer organization at root for Enrich/Identity, else embedded)
    F.coalesce(org_id.duns, org_emb.duns).alias("Duns"),

    # FEIN / CRN (typeDnBCode mappings differ in your SQL example; keep 6863 and 1372)
    F.expr("""
      element_at(
        transform(
          filter(embeddedProduct.organization.registrationNumbers, x -> x.typeDnBCode = 6863),
          x -> x.registrationNumber
        ), 1)
    """).alias("FEIN"),
    F.expr("""
      element_at(
        transform(
          filter(embeddedProduct.organization.registrationNumbers, x -> x.typeDnBCode = 1372),
          x -> x.registrationNumber
        ), 1)
    """).alias("CRN"),

    # Corporate linkage (global/domestic ultimate, parent)
    F.coalesce(
        F.col("embeddedProduct.organization.corporateLinkage.globalUltimate.duns"),
        F.col("organization.corporateLinkage.globalUltimate.duns")
    ).alias("GlobalUltimateDuns"),
    F.coalesce(
        F.col("embeddedProduct.organization.corporateLinkage.globalUltimate.primaryName"),
        F.col("organization.corporateLinkage.globalUltimate.primaryName")
    ).alias("GlobalUltimateDunsName"),
    F.coalesce(
        F.col("embeddedProduct.organization.corporateLinkage.domesticUltimate.duns"),
        F.col("organization.corporateLinkage.domesticUltimate.duns")
    ).alias("DomesticUltimateDuns"),
    F.coalesce(
        F.col("embeddedProduct.organization.corporateLinkage.domesticUltimate.primaryName"),
        F.col("organization.corporateLinkage.domesticUltimate.primaryName")
    ).alias("DomesticUltimateDunsName"),
    F.coalesce(
        F.col("embeddedProduct.organization.corporateLinkage.parent.duns"),
        F.col("organization.corporateLinkage.parent.duns")
    ).alias("ParentDuns"),
    F.coalesce(
        F.col("embeddedProduct.organization.corporateLinkage.parent.primaryName"),
        F.col("organization.corporateLinkage.parent.primaryName")
    ).alias("ParentDunsName"),

    # Names / marketable flag
    F.coalesce(org_id.primaryName, org_emb.primaryName).alias("PrimaryName"),
    F.coalesce(
        F.col("embeddedProduct.organization.dunsControlStatus.isMarketable"),
        F.col("organization.dunsControlStatus.isMarketable")
    ).alias("IsMarketable"),

    # NAICS/SIC/SIC8 using your typeDnBCode+priority rules
    industry_field("embeddedProduct.organization.industryCodes", "30832", 1, "code").alias("NAICSCode"),
    industry_field("embeddedProduct.organization.industryCodes", "30832", 1, "description").alias("NAICSCodeDescription"),
    industry_field("embeddedProduct.organization.industryCodes", "399",   1, "code").alias("SICCode"),
    industry_field("embeddedProduct.organization.industryCodes", "399",   1, "description").alias("SICCodeDescription"),
    industry_field("embeddedProduct.organization.industryCodes", "3599",  1, "code").alias("SIC8Code"),
    industry_field("embeddedProduct.organization.industryCodes", "3599",  1, "description").alias("SIC8CodeDescription"),

    # SubsidiaryStatus (hierarchyLevel == '1' -> false else true)
    F.when(
        F.coalesce(
            F.col("embeddedProduct.organization.corporateLinkage.hierarchyLevel"),
            F.col("organization.corporateLinkage.hierarchyLevel")
        ) == F.lit("1"),
        F.lit("false")
    ).otherwise(F.lit("true")).alias("SubsidiaryStatus"),

    # Contact info
    F.coalesce(F.col("embeddedProduct.organization.fax.isdCode"),       F.col("organization.fax.isdCode")).alias("FaxNumberCountryCode"),
    F.coalesce(F.col("embeddedProduct.organization.fax.telephoneNumber"),F.col("organization.fax.telephoneNumber")).alias("FaxAreaCodePhoneNumber"),
    F.coalesce(F.col("embeddedProduct.organization.telephone.isdCode"),  F.col("organization.telephone.isdCode")).alias("PhoneNumberCountryCode"),
    F.coalesce(F.col("embeddedProduct.organization.telephone.telephoneNumber"), F.col("organization.telephone.telephoneNumber")).alias("PhoneAreaCodePhoneNumber"),
    F.coalesce(F.col("embeddedProduct.organization.websiteAddress.url"), F.col("organization.websiteAddress.url")).alias("URL"),

    # Address fields (switch based on params)
    address_source.getField("streetAddress").getField("line1").alias("AddressLine1"),
    address_source.getField("streetAddress").getField("line2").alias("AddressLine2"),
    address_source.getField("addressLocality").getField("name").alias("City"),
    address_source.getField("addressRegion").getField("abbreviatedName").alias("State"),
    address_source.getField("addressCountry").getField("name").alias("Country"),
    address_source.getField("addressCountry").getField("isoAlpha2Code").alias("ISOCountryCode"),
    address_source.getField("postalCode").alias("PostalCode"),
    address_source.getField("postalCodeExtension").alias("PostalCodeExtension"),
    address_source.getField("latitude").alias("Latitude"),
    address_source.getField("longitude").alias("Longitude"),

    # Match quality
    confidence_code.cast("int").alias("ConfidenceCode"),
    match_grade.alias("MatchGradeString"),

    # AddressType (only exists on standardizedAddress in your T-SQL)
    F.when(
        (F.lit(response_type) == F.lit("IdentityDetail")) & (F.lit(standardize_address) == 1),
        F.col("cleanseAndStandardizeInformation.standardizedAddress.addressType")
    ).otherwise(F.lit(None)).alias("AddressType"),

    # Family tree role (coalesced)
    family_tree_desc.alias("FamilyTreeRolesPlayed"),

    # DBA (trade style) priority = 1
    F.coalesce(
        trade_style_name("embeddedProduct.organization.tradeStyleNames"),
        trade_style_name("organization.tradeStyleNames")
    ).alias("DBAName")
)

# Show result
df_flat.printSchema()
df_flat.show(truncate=False)
