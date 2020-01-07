# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
 
import json
import boto3
import os

solutionArn = os.environ['SOLUTION_ARN']

personalizeClient = boto3.client('personalize')

def triggerSolutionVersionCreate():
    response = personalizeClient.create_solution_version(
        solutionArn=solutionArn
    )
    return response['solutionVersionArn']

def lambda_handler(event, context):
    solutionVersionArn = triggerSolutionVersionCreate()

    return solutionVersionArn