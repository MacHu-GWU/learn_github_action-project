# -*- coding: utf-8 -*-

"""
Requirements::

    aws-cdk-lib==2.89.0
"""

from aws_cdk import App, Stack
import aws_cdk.aws_iam as iam
from constructs import Construct


class GitHubActionTestCdkStack(Stack):
    def __init__(
        self,
        scope: Construct,
        id: str,
        **kwargs,
    ) -> None:
        super().__init__(scope, id, **kwargs)

        iam.Group(self, "MyFirstIamGroup", group_name="MyFirstIamGroup")


app = App()
stack = GitHubActionTestCdkStack(app, "GitHubActionTestCdkStack")
