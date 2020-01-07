# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
 
import os

itemDatasetArn = os.environ['ITEM_DATASET_ARN']
userDatasetArn = os.environ['USER_DATASET_ARN']
userItemDatasetArn = os.environ['USER_INTERACTIONDATASET_ARN']
itemDatasource = os.environ['S3_ITEM_DATASOURCE_PATH']
userDatasource = os.environ['S3_USER_DATASOURCE_PATH']
interactionDatasource = os.environ['S3_USERINTERACTION_DATASOURCE_PATH']

def formatDatasetObject(datasetArn, datasource):
    if datasetArn and datasource:
        return {"arn": datasetArn, "s3Datasource": datasource}
    return None 

def lambda_handler(event, context):
    items = formatDatasetObject(itemDatasetArn, itemDatasource)
    users = formatDatasetObject(userDatasetArn, userDatasource)
    interactions = formatDatasetObject(userItemDatasetArn, interactionDatasource)

    datasources = [x for x in [items, users, interactions] if x is not None]

    return datasources