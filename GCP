## GCP PDE examination

# Section 1
## 1.1
-------------------------------------------------------------------
● Identity and Access Management (e.g., Cloud IAM and organization policies)
● Data security (encryption and key management)
● Privacy (e.g., strategies to handle personally identifiable information)
● Regional considerations (data sovereignty) for data access and storage
● Legal and regulatory compliance
● Designing the project, dataset, and table architecture to ensure proper data
governance
● Multi-environment use cases (development vs. production)
-------------------------------------------------------------------

“Restrict access to only required users” → ✅ IAM roles
“Enforce company-wide policies” → ✅ Org policies
“Pipeline authentication” → ✅ Service accounts


## Types of Encryption
Google Managed Keys

CMEK (Managed via Cloud KMS)

Full control (rotate, revoke)

# CSEK customer supplied key :- You provide keys at request time (rare)

## Privacy (Handling PII )

Data masking :: Hide sensitive fields

Tokenization  :: Replace actual data

Anoymization :: Remove identity completely

DLP API :: Detect + classify sensitive data (PII)
Identify sensitive data like SSNs and emails


“Identify sensitive data” → ✅ DLP
“Mask PII” → ✅ Tokenization/masking
“Prevent unauthorized access” → ✅ IAM + policies

## Legal & Regulatory Compliance
GDPR (EU)
HIPAA (healthcare)
PCI-DSS (payments)


## Top Pointers
Use least privilege IAM
Use service accounts for pipelines
Default encryption exists, but CMEK gives control
Use DLP for PII detection
Single-region = data sovereignty
Multi-region = availability
Use audit logs for compliance
Separate projects for environments
Apply IAM at dataset/table level
Compliance = security + auditing + governanc






#### Session 1
Topics:: Biglake, External tables, Biglake tables 

### Exam pointers
fine-grained access → BigLake
BigLake enables fine-grained security on external data
BigLake supports multi-engine access (BQ + Spark)
BigLake tables store data in GCS, not BigQuery
BigLake integrates with Dataplex for governance
BigLake is key for lakehouse architecture   
simple quick query → external table

Data in GCS
Multiple teams need access
Need security at row level
👉 ✅ BigLake


## Real world example
Data ingestion → GCS (Parquet files)
                     ↓
                BigLake Tables
                     ↓
     -------------------------------
     |             |               |
 BigQuery      Dataproc        Dataflow
 (SQL)         (Spark)         (ETL)


## Use case of BIG lake
Single data copy
Unified access control
Works across engines

A company stores logs in GCS (Parquet files)
They want:
Data analysts → use SQL (BigQuery)
Data engineers → run Spark jobs (Dataproc)
ETL pipelines → run (Dataflow)

## Final Take AWAY
External Tables → lightweight, quick access
BigLake Tables → secure, governed, multi-engine
Native Tables → fastest analytics,in-frequent reads



### Session 2

## Transfer services

1. Storage transfer service :: Batch type
Use STS if:
Data is > 1 TB
You need automation / recurring jobs
Migrating from AWS S3 or Azure Blob
You have good network bandwidth

## Keywords to remember
“Managed”
“Petabyte scale”
“Scheduled transfers”
“Hybrid / multi-cloud”

2. Transfer Appliances
“No/slow network → Transfer Appliance”
✅ Keywords
“Offline migration”
“Physical device”
“Petabyte-scale ingest”


3. BigQuery Data Transfer Service

Google Ads, YouTube, SaaS apps
Cloud Storage, Cloud SQL
Scheduled ingestion jobs [linkedin.com]

4. Data stream :: Only for the database not for Object transfer

Use Datastream when:
✅ 1. Real-time analytics
Example:
MySQL → BigQuery → dashboards
✅ 2. Database replication
Keep cloud DB synced with on-prem DB
✅ 3. Cloud migration (low downtime)
Continuous sync → cutover later
✅ 4. Event-driven systems
Stream DB changes → trigger workflows
👉 Keywords:
“near real-time”
“CDC”
“database sync”



5. gsutils and 

Data is small (< 1 TB) [docs.cloud...google.com]
One-time/manual copy
Scripts / DevOps automation


## Key Exam Memory Hacks

🔁 STS = Online + Automated
📦 Transfer Appliance = Offline + Huge data
📊 BigQuery DTS = Analytics ingestion
💻 gsutil = Small + manual


## Phase 3
Dataform ::- Transform data already in BigQuery using SQL
Dataform = ELT, Data Fusion = ETL
Dataform integrates with Git for version control
Dataform assertions:: Built-in data quality checks

## "Dataform Incremental Models" :: Processes only new or changed data instead of full-table recomputation


## Data Fusion → GUI + ETL + ingestion


## Data fusion and DataForm
Data Sources (DB, APIs)
        ↓
   Data Fusion (ETL)
        ↓
   BigQuery (Storage)
        ↓
   Dataform (Transformations)
        ↓
   BI / Analytics

   ✅ Quick Revision Tips

Dataform → SQL + ELT + BigQuery
Data Fusion → GUI + ETL + ingestion
Dataflow → streaming + code-based pipelines

Exam Pattern Observations (Very Important)
 If question says:

“SQL transformations in BigQuery”
👉 ✅ Dataform
If question says:

“GUI / drag-and-drop / connectors”
👉 ✅ Data Fusion



## Phase 4
Data flow :: Batch + pub/sub
Exactly-once processing ✅
Windowing ✅
Late data handling ✅


DataProc
Flexibility ✅
Custom Spark jobs ✅
Cost control with preemptible VMs ✅
