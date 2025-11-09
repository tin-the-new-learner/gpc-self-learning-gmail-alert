from google.cloud import bigquery
# from google.oauth2 import service_account

# key_path = "gcp-sa-001.json"
# credentials = service_account.Credentials.from_service_account_file(key_path)
client = bigquery.Client(project="gcp-owner-self-learning")

query = """
    insert into gcp-owner-self-learning.pubsub_dataflow_uat.pubsub_dataflow_bq_v1
    values(13,'tin13')
"""

df = client.query(query)