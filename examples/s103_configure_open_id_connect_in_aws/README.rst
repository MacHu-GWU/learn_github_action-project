Configuring OpenID Connect in Amazon Web Services
==============================================================================
本例的实例 GitHub action workflow yaml 文件在 `s103_configure_open_id_connect_in_aws.yml <../../.github/workflows/s103_configure_open_id_connect_in_aws.yml>`_.

这里有一些 `示例的 Build <https://github.com/MacHu-GWU/learn_github_action-project/actions/workflows/s103_configure_open_id_connect_in_aws.yml>`_.


Overview
------------------------------------------------------------------------------
让 GitHub Action 来部署 AWS 资源是那些在 GitHub 上开发, 但在 AWS 上部署 App 的企业的常见需求. 早期很多人的做法是用 Secret environment variable 把 AWS IAM User 的 access key 和 secret key 注入进去. 而 AWS 明确说明了在 CI 环境中使用长期不失效的 credential 是不安全的. 后来 GitHub 和 AWS 原生支持了用 OpenID connect 来给 GitHub action 授权.


How it work
------------------------------------------------------------------------------
OpenID 是一种让不同系统中的 identity 互相能相连的互联网标准. 例如 GitHub 中的用户和 AWS 中的用户相连.

你需要再 AWS 上添加一个 Identity provider, 也就是让 AWS 认识 GitHub. 然后创建一个 IAM Role 显式允许 GitHub 的某个 Organization 的某些 Repo 能 assume 这个 Role. 然后使用 `configure-aws-credentials <https://github.com/aws-actions/configure-aws-credentials>`_ 这个由 AWS 维护的 GitHub action 即可轻松让 CI Job 获得跟这个 IAM Role 等效的权限了.


Reference
------------------------------------------------------------------------------
- `Configuring OpenID Connect in Amazon Web Services <https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services>`_: GitHub 的官方文档
- `Sample IAM OIDC CloudFormation Template <https://github.com/aws-actions/configure-aws-credentials#sample-iam-oidc-cloudformation-template>`_: 由 AWS 维护的 GitHub action, 可以方便地配置好 AWS 权限. 这一节里提到的 cloudformation template 可以方便地配置好 AWS 那边需要的设置.
