# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
 
import json
import boto3

personalizeClient = boto3.client('personalize')

def lambda_handler(event, context):
    response = personalizeClient.describe_dataset_import_job(
        datasetImportJobArn = event['importJobArn']
    )

    return response['datasetImportJob']['status']