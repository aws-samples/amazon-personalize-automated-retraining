# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
S3_BUCKET ?= CONFIGURE_S3_BUCKET_HERE
REGION ?= eu-west-1

all:
	aws cloudformation package \
		--template-file stack.template \
		--s3-bucket $(S3_BUCKET) \
		--output-template-file packaged-template.yaml
	aws cloudformation deploy \
		--template-file packaged-template.yaml \
		--s3-bucket $(S3_BUCKET) \
		--stack-name automated-personalize-retraining \
		--capabilities CAPABILITY_IAM \
		--parameter-overrides $$(cat parameters.cfg) \
		--region $(REGION)