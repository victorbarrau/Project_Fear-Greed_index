
from google.cloud import storage
from google.cloud import bigquery
import pandas as pd
import datetime
import io
import numpy as np
import pandas_gbq

client = storage.Client()
bucket = client.get_bucket('data-coin-market-cap')
crypto_list = ["bnb", "eth", "doge","btc"]
start_date = datetime.datetime(2023, 3, 1)
end_date = datetime.datetime(2023, 3, 5)
date_generated = [start_date + datetime.timedelta(days=x) for x in range((end_date-start_date).days+1)]
date_generated = [date.strftime('%Y%m%d') for date in date_generated]
for crypto in crypto_list:
    for date in date_generated:

        file_name = crypto+"/daily/dominance_du_"+str(date)+".csv"
        blob = bucket.get_blob(file_name)
        if blob is not None:
            content = blob.download_as_string()
            df = pd.read_csv(io.StringIO(content.decode('utf-8')))
            df['date'] = pd.to_datetime(df['date'], format='%Y%m%d', errors='coerce')
            project = 'sublime-vial-365809'
            destination_table = 'dominance.'+crypto

            job_config = bigquery.LoadJobConfig(
                schema=[
                    bigquery.SchemaField("date", bigquery.enums.SqlTypeNames.DATE), 
                    bigquery.SchemaField("dominance", bigquery.enums.SqlTypeNames.FLOAT),
                ],
                write_disposition="WRITE_APPEND",
            )
            client = bigquery.Client()
            table_id = "dominance."+crypto
            job = client.load_table_from_dataframe(
                df, table_id, job_config=job_config
            )
            job.result()

            table = client.get_table(table_id)
            print(
                "Loaded {} rows and {} columns to {}".format(
                    table.num_rows, len(table.schema), table_id
                )
            )
        else:
            print(f"Le fichier {file_name} n'existe pas dans le bucket.")
