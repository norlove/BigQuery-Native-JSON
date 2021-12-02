# Copyright 2021 Google. This software is provided as-is, without warranty or representation for any use or purpose.
# Your use of it is subject to your agreement with Google.

from google.cloud import bigquery
import json

#Read events data from a local file called local_file.json
with open('local_file.json', 'r') as json_file:
    data = json.load(json_file)

#Stream the data into BigQuery
project_id = '<supply_your_project_id_here>'
table_id = 'json_streaming.events'

client = bigquery.Client(project=project_id)
table_obj = client.get_table(table_id)

#Throw errors if encountered.
#https://googleapis.dev/python/bigquery/latest/generated/google.cloud.bigquery.client.Client.html?highlight=insertall

errors = client.insert_rows(table=table_obj, rows=data)
if errors == []:
    print("New rows have been added.")
else:
    print("Encountered errors while inserting rows: {}".format(errors))
