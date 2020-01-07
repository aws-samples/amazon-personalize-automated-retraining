# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
 
import json
import boto3
import os
import datetime

importRoleArn = os.environ['IMPORT_ROLE_ARN']

personalizeClient = boto3.client('personalize')

def triggerImport(datasetArn, s3Datasource):
    datasetType = datasetArn.split("/")[-1]
    response = personalizeClient.create_dataset_import_job(
        jobName=datasetType + '-import-' + datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'),
        datasetArn=datasetArn,
        dataSource={
            'dataLocation': s3Datasource
        },
        roleArn=importRoleArn
    )
    return response['datasetImportJobArn']

def lambda_handler(event, context):
    datasetArn = event['arn']
    s3Datasource = event['s3Datasource']

    return triggerImport(datasetArn, s3Datasource)