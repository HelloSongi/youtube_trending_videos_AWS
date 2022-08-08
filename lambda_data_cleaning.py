import awswrangler as wr
import pandas as pd
import urllib.parse
import os

#temporary AWS setting e.g
#setting OS as variable in lambda
os_input_s3_cleansed_layer = os.environ['s3_cleansed_layer']
os_input_glue_catalog_db_name = os.environ['glue_catalog_db_name']
os_input_glue_catalog_table_name = os.environ['glue_catalog_table_name']
os_input_write_data_operation = os.environ['write_data_operation']
def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['object']['name']
    key = urllib.parse.unquote_plus(['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        #dataframe from the content
        df_row = wr.s3.read.json('s3://{}/{}'.format(bucket, key))
        #extract needed coluns
        df_step_1 = pd.json_normalize(df_raw['items'])
        #save data to new S3 bucket
        wr_response = wr.s3.to_parset(
            df=df_step_1,
            path = os_input_s3_cleansed_layer,
            dataset = True,
            database = os_input_glue_catalog_db_name,
            table = os_input_glue_catalog_table_name
            mode = os_input_write_data_operation
        )
        return wr_response
    except exception as e:
        print(e)
        print('error getting object {} from bucket {}. Make sure they exit and the bucket is in the same region as this function}')
        raise e