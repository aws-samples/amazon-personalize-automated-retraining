# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
 
import json
import boto3
import os

campaignArn = os.environ['CAMPAIGN_ARN']

personalizeClient = boto3.client('personalize')

def lambda_handler(event, context):
    if campaignArn:
        print("Updating campaign")
        response = personalizeClient.update_campaign(
            campaignArn=campaignArn,
            solutionVersionArn=event['solutionVersionArn']
        )
    else:
        print("Skipping campaign update. No campaignArn provided. Be sure to roll out the updated solution version yourselves.")

    return response["campaignArn"]