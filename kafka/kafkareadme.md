Start kafka:
---------------

Go to the kafka where it is put the src file and then run one by one

.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties

.\bin\windows\kafka-server-start.bat .\config\server.properties

.\bin\windows\kafka-topics.bat --create --topic test-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

.\bin\windows\kafka-console-producer.bat --broker-list localhost:9092 --topic test-topic

Medolian Architecture:
------------------------
ronze Layer – Raw Ingestion
- Purpose: Capture raw, unfiltered data from sources like Kafka, APIs, or files.
- Traits: Schema-on-read, minimal transformation, often includes metadata like ingestion timestamps.
- Use case: Replayability, audit trails, and historical snapshots.

🥈 Silver Layer – Cleansed & Conformed
- Purpose: Clean, deduplicate, and standardize data from Bronze.
- Traits: Joins across sources, type casting, null filtering, basic business rules.
- Use case: Trusted datasets for analysts, ML feature engineering, and downstream enrichment.

🥇 Gold Layer – Business-Ready
- Purpose: Aggregate and model data for specific business domains.
- Traits: Dimensional modeling, KPIs, curated metrics, and dashboards.
- Use case: BI tools, executive reporting, and ML model consumption.

🔁 Why Use It?
- Promotes data quality and governance
- Enables modular development and scalability
- Supports streaming and batch workloads
- Ideal for real-time analytics, especially in healthcare, finance, and IoT

