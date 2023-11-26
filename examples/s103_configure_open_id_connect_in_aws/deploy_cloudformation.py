# -*- coding: utf-8 -*-

"""
This script automates the GitHub open id connect configuration in AWS.

Python >= 3.7 is required.

Requirements::

    boto_session_manager>=1.5.4,<2.0.0
    aws_cloudformation>=1.5.1,<2.0.0
"""

from pathlib import Path
from boto_session_manager import BotoSesManager
import aws_cloudformation.api as aws_cf

# ------------------------------------------------------------------------------
# Edit the following variables:
# ------------------------------------------------------------------------------
# the name of AWS profile in ~/.aws/credentials for this deployment
# it should have permission to create IAM role
aws_profile = "bmt_app_dev_us_east_1"
# cloudformation stack name, alpha, digit, hyphen only
stack_name = "learn-github-action-configure-open-id-connect-test"
github_org = "MacHu-GWU"
github_repo = "learn_github_action-project"
role_name = "learn-github-action-configure-open-id-connect-test"

# ------------------------------------------------------------------------------
# No need to edit below this line
# ------------------------------------------------------------------------------
bsm = BotoSesManager(profile_name=aws_profile)
dir_here = Path(__file__).absolute().parent
aws_cf.deploy_stack(
    bsm=bsm,
    stack_name=stack_name,
    template=dir_here.joinpath("configure-aws-credentials-2023-11-26.yml").read_text(),
    parameters=[
        aws_cf.Parameter(key="GitHubOrg", value=github_org),
        aws_cf.Parameter(key="RepositoryName", value=github_repo),
        aws_cf.Parameter(key="RoleName", value=role_name),
    ],
    skip_prompt=True,
    include_named_iam=True,
    tags={
        "tech:description": "Test configure GitHub open id connect in AWS",
    },
)
