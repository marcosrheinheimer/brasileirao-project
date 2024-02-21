from google.cloud import bigquery
from google.api_core import exceptions


def create_table_from_uri(dataset, table, uri, project='gcp-brasileirao', format='JSON'):
    client = bigquery.Client(project)
    
    try:
        client.dataset(dataset)
        bq_table = client.create_table(f'{project}.{dataset}.{table}', exists_ok=True)
        job_config = bigquery.LoadJobConfig()

        if format.upper() == 'JSON':
            job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
            job_config.autodetect = True
            job_config.
        
        else:
            print('Sorry, come later')
        

        load_job = client.load_table_from_uri(
            uri,
            bq_table,
            location="US",  # Must match the destination dataset location.
            job_config=job_config
            ) 
        
        return load_job.result()

    except Exception as e:
        return e

