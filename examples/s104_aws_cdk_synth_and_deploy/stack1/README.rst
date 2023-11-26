AWS CDK Synth and Deploy
==============================================================================

Overview
------------------------------------------------------------------------------
GitHub Action 作为 CI/CD 工具非常强大. 但是对于用 CDK 来部署的 AWS 项目, AWS CodePipeline 能并行部署多个 CDK Stack 是一个非常大的优势. 在 GitHub Action 中, 一个 Job 只能够并行部署一个
AWS CDK Deploy