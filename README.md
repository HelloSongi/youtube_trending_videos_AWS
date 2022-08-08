PROJECT OUTCOMES

1. Understanding the project Overview and Architecture
2. ETL on Big Data
3. Data Staging and Data Lake
4. Creating IAM access Roles and Policies
5. Creating AWS Lambda Functions
6. Setting up Glue Jobs for ETL
7. Using AWS Glue Crawler and AWS Glue Studio
8. Creating Glue Data Catalog
9. Converting JSON to Parquet format
10. Performing Data Transformations (wrangling) and Joins
11. Visualizing using AWS QuickSight





GENERAL PROJECT ARCHITECTURE AND DESIGN

![SYSTEM_DESIGN](https://user-images.githubusercontent.com/69304233/182819671-ff0f1b67-a3b1-4bef-a0bf-2231eaaab06f.PNG)






CREATING AWS S3 BUCKET AND UPLOADING DATA 

creating both AWS S3 and uploading data to S3 bucket can be done using AWS CLI or the AWS dashboard. 
USing the AWS cli, data is uploaded using the command: AWS S3 CP /FILE_LOACATION

![1](https://user-images.githubusercontent.com/69304233/183393565-12e8b95c-6e80-4359-a192-a3ce8aa810ea.PNG)


![2](https://user-images.githubusercontent.com/69304233/183395819-dbaa4a35-fc9d-4a5e-a20c-28eaa148474b.PNG)


DATA CLEANSING

In this stage, we create a pipline that wrangle and cleans our data to remove erros, redundant data etc
This pre-processing stage essentially inlvoves tranformin the data from semi-structured data to structured data for easier querying by AWS Athena
JSON file are coverted to tabular form.
AWS lambda works on the data processing in the S3 bucket and puts the puts the processed data into a new cleansed S3 bucket.

![3](https://user-images.githubusercontent.com/69304233/183401177-9f458e3c-1c8c-4e51-899d-4339e9f1722a.PNG)

![4](https://user-images.githubusercontent.com/69304233/183408698-542d5293-ff61-4de7-a775-900606f41132.PNG)

After the data have tranformed from JSON to tabular form, we use AWS Athena to query the data

![5](https://user-images.githubusercontent.com/69304233/183411088-71df5c97-918c-4dbf-89e9-4487657faeda.PNG)

