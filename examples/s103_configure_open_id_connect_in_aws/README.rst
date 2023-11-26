Configuring OpenID Connect in Amazon Web Services
==============================================================================
本例的实例 GitHub action workflow yaml 文件在 `s103_configure_open_id_connect_in_aws.yml <../../.github/workflows/s103_configure_open_id_connect_in_aws.yml>`_.

这里有一些 `示例的 Build <https://github.com/MacHu-GWU/learn_github_action-project/actions/workflows/s103_configure_open_id_connect_in_aws.yml>`_.


Overview
------------------------------------------------------------------------------
由于 GitHub 是如此的流行, 很多企业还是会选择优先使用将 Git 代码库 host 在 GitHub. 而 GitHub Action 又是原生的 CI/CD 方案, 所以有很多企业在使用 GitHub Action. 而 AWS 又是云计算时代一直保持了市场份额第一长达 10 多年的平台, 大量的企业会将它们的数据, App 部署在 AWS 上. 所以用 GitHub Action 进行 CI, 并将 App 部署到 AWS 上是一个很常见的需求. 这其中就必然涉及到给 GitHub Action 合适的 AWS 权限问题.

早期很多人的做法是用 `Secret Environment Variable <https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions>`_ 把 `AWS IAM User <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html>`_ 的 `access key 和 secret key <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html>`_ 分别赋值给 `AWS_ACCESS_KEY_ID 和 AWS_SECRET_ACCESS_KEY <https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html>`_, 从而实现了一个默认的 AWS credential.

后来 GitHub 和 AWS 合作, 原生支持了用 OpenID connect 来给 GitHub action 授权. 并且 AWS 官方明确说明了 `在 CI 环境中使用长期不失效的 credential 是不安全的 <https://github.com/aws-actions/configure-aws-credentials#long-term-credentials-warning-10323>`_. 为了方便用户 GitHub 和 AWS 都更新了它们的官方文档, 详细说明了如何使用 OpenID connect 来给 GitHub action 授权.


How it work
------------------------------------------------------------------------------
OpenID 是一种让不同系统中的 identity 互相能相连的互联网标准. 例如 GitHub 中的用户和 AWS 中的用户相连.

你需要再 AWS 上添加一个 Identity provider, 也就是让 AWS 认识 GitHub. 然后创建一个 IAM Role 显式允许 GitHub 的某个 Organization 的某些 Repo 能 assume 这个 Role. 然后使用 `configure-aws-credentials <https://github.com/aws-actions/configure-aws-credentials>`_ 这个由 AWS 维护的 GitHub action 即可轻松让 CI Job 获得跟这个 IAM Role 等效的权限了.


How to Setup
------------------------------------------------------------------------------
本节把 GitHub 和 AWS 的官方文档中的重要信息提炼出来并整合在一起, 照做可以迅速滴为你的 GitHub Action 配置好 AWS 权限. 本节主要是方便我自己以后参考.

第一步, 配置 AWS 的 IAM, 本质上是告知 AWS 请允许 GitHub 上的某个 Organization 的某个 Repository (或是全部的 Repository) 能 assume 某一个 Role. 我们就要在这创建这个 Role.

1. 部署 CloudFormation Template (本例中使用的是 us-east-1 region): 打开 `AWS CloudFormation Console 的 Create stack 菜单 <https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create>`_, 选择 Prepare template -> Template is ready, Specify template -> Template source -> Upload a template file -> Choose file -> 选择 `Sample IAM OIDC CloudFormation Template <https://github.com/aws-actions/configure-aws-credentials#sample-iam-oidc-cloudformation-template>`_ 官方文档中下载好的 CloudFormation template, 我这里自己做了一个基于官方并有略微改动的 point-in-time 备份 `configure-aws-credentials-2023-11-26.yml <./configure-aws-credentials-2023-11-26.yml>`_. (我倾向于使用我自己的因为官方的生成的 IAM Role 名字是不确定的, 而我的是确定的).
    - stack name: 我的 stack name 是 ``learn-github-action-configure-open-id-connect-test``
    - Github Org: 我的 Organization 是 ``MacHu-GWU``
    - RepositoryName: 如果你想让所有的 Repo 都能 assume 这个 Role, 就填 ``*``, 否则填写你想要的 Repo 名称, 例如我们这个 Repo ``learn_github_action-project``.
    - OIDCAudience: 使用它自动填好的 ``sts.amazonaws.com``
    - OIDCProviderArn: 默认留空.
    - RoleName: 填写你想要的 Role 名称, 例如 ``learn-github-action-configure-open-id-connect-test``.
    - Tag: ``tech:description = Test configure GitHub open id connect in AWS``
    - Capabilities: 勾选 "I acknowledge that AWS CloudFormation might create IAM resources".


Reference
------------------------------------------------------------------------------
- `Configuring OpenID Connect in Amazon Web Services <https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services>`_: GitHub 的官方文档. 建议先看这个文档了解一下原理和详细步骤.
- `Sample IAM OIDC CloudFormation Template <https://github.com/aws-actions/configure-aws-credentials#sample-iam-oidc-cloudformation-template>`_: 由 AWS 维护的 GitHub action, 可以方便地配置好 AWS 权限. 这一节里提到的 cloudformation template 可以方便地配置好 AWS 那边需要的设置, 大大减少手动配置出错的概率.
