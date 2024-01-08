from google.cloud import bigquery
from google.api_core.exceptions import BadRequest, ClientError


# Construct a BigQuery client object.
client = bigquery.Client('gcp-brasileirao-gcp')

bq_dataset = client.dataset('brasileirao')
bq_table = bq_dataset.table('leagues2')


job_config = bigquery.LoadJobConfig()

job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
job_config.autodetect = True


uri = "gs://stg-brasileirao-raw/leagues.json"

load_job = client.load_table_from_uri(
    uri,
    bq_table,
    location="US",  # Must match the destination dataset location.
    job_config=job_config
)  # Make an API request.

try:
    load_job.result()  # Waits for the job to complete.
except BadRequest as ex:
    for err in ex.errors:
        print(err)
    raise


