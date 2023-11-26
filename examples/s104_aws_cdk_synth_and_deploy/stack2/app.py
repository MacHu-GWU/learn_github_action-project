# -*- coding: utf-8 -*-

"""
Requirements::

    aws-cdk-lib==2.89.0
"""

from aws_cdk import App, Stack
import aws_cdk.aws_iam as iam
import aws_cdk.aws_s3_assets as s3_assets
from constructs import Construct


class GitHubActionTestCdkStack2(Stack):
    def __init__(
        self,
        scope: Construct,
        id: str,
        **kwargs,
    ) -> None:
        super().__init__(scope, id, **kwargs)

        self.iam_group = iam.Group(
            self,
            "MySecondIamGroup",
            group_name="MySecondIamGroup",
        )
        self.s3_asset = s3_assets.Asset(
            self,
            "SourceCode",
            path=__file__,
        )


app = App()
stack = GitHubActionTestCdkStack2(app, "GitHubActionTestCdkStack2")
app.synth()
