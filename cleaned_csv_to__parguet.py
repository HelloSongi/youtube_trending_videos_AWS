import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import job
from awsglue.dynamicframe import DynamicFrame


#job name
args = getResolvedOptions(sys.argv, [JOB_NAME])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = job(glueContext)
job.init(args['JOB_NAME'], args)

predictive_pushdown = 'region in ('ca,' 'gb', 'us')'
#apply mapping
datasource0 = glueContext.create_dyanamic_frame.from_catalog(database = 'de_youtube_raw', table_name = 'raw_statistics', transformation_ctx = 'datasource0', push_down_predictive = predictive_pushdown)
applymapping1 = ApplyMapping.apply(frame = datasource0, mappings = [('video_id', 'string', 'video_id', 'string'), ('trending_date', 'string', 'trending_date', 'string')])
