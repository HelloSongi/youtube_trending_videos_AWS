# PROJECT OUTCOMES

* Understanding the project Overview and Architecture
* ETL on Big Data
* Data Staging and Data Lake
* Creating AWS Lambda Functions
* Setting up Glue Jobs for ETL
* Using AWS Glue Crawler and AWS Glue Studio
* Creating Glue Data Catalog
* Converting JSON to Parquet format
* Performing Data Transformations (wrangling) and Joins
* Visualizing using AWS QuickSight





# GENERAL PROJECT ARCHITECTURE AND DESIGN

![ARCHITECTURE](https://user-images.githubusercontent.com/69304233/183481878-a0c9b7d6-c611-4a31-8144-548a9789bc4e.PNG)






# CREATING AWS S3 BUCKET AND UPLOADING DATA 

creating both AWS S3 and uploading data to S3 bucket can be done using AWS CLI or the AWS dashboard. 
USing the AWS cli, data is uploaded using the command: AWS S3 CP /FILE_LOACATION

![1](https://user-images.githubusercontent.com/69304233/183393565-12e8b95c-6e80-4359-a192-a3ce8aa810ea.PNG)


![2](https://user-images.githubusercontent.com/69304233/183395819-dbaa4a35-fc9d-4a5e-a20c-28eaa148474b.PNG)


# DATA CLEANSING

In this stage, we create a pipline that wrangle and cleans our data to remove erros, redundant data etc
This pre-processing stage essentially inlvoves tranformin the data from semi-structured data to structured data for easier querying by AWS Athena
JSON file are coverted to tabular form.
AWS lambda works on the data processing in the S3 bucket and puts the puts the processed data into a new cleansed S3 bucket.

![3](https://user-images.githubusercontent.com/69304233/183401177-9f458e3c-1c8c-4e51-899d-4339e9f1722a.PNG)

![4](https://user-images.githubusercontent.com/69304233/183408698-542d5293-ff61-4de7-a775-900606f41132.PNG)

After the data have tranformed from JSON to tabular form, we use AWS Athena to query the data

![5](https://user-images.githubusercontent.com/69304233/183411088-71df5c97-918c-4dbf-89e9-4487657faeda.PNG)


# MONITORING DIFFERENT JOBS ETL JOBS

![6](https://user-images.githubusercontent.com/69304233/183475149-c543e484-69e3-4531-bd24-65aad2a5bba8.PNG)



# VISUALIZATION DATA USING QUICKSIGHT

![7](https://user-images.githubusercontent.com/69304233/183475309-c8ae4b32-1ba2-44bd-b41e-5ce4e868f522.PNG)

![8](https://user-images.githubusercontent.com/69304233/183475365-3bc93570-cbf6-4225-bd15-75cf0e73e07a.PNG)
