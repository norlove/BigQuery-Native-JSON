# BigQuery-Native-JSON
This repo contains examples of how to stream JSON data natively into BigQuery using both the Storage Write API and legacy insertAll streaming API.

The blog post which provides context into BigQuery Native JSON and streaming via these two methods can be found here: [Add Link Once Published].

**Ingesting via the BigQuery Storage Write API:**
    
Documentation on how to use the Storage Write API can be found [HERE](https://cloud.google.com/bigquery/docs/write-api)
    For a longer example that shows how to send different data types, including STRUCT types, see the [append_rows_proto2](https://github.com/googleapis/python-bigquery-storage/blob/main/samples/snippets/append_rows_proto2.py) sample on GitHub. 

Please refer and copy the files from the *storage-write-api-method* folder.
  
    
**Ingesting via the BigQuery Legacy insertAll Streaming API:** 
    
Documentation on how to use the legacy insertAll streaming API can be found [HERE](https://cloud.google.com/bigquery/streaming-data-into-bigquery)
  
Please refer and copy the files from the *legacy-insertAll-api-method* folder.
