Understanding OIDC Authentication for GitHub and AWS
==============================================================================


Overview
------------------------------------------------------------------------------
GitHub Actions 是世界上最流行的代码托管平台 GitHub 的原生 CI/CD 服务, 以简单, 易用和慷慨的免费计划而著称 (这种慷慨得益于微软的支持, 微软通过这种方式吸引开发者加入其生态系统, 不在乎这些成本) . 而 AWS 则是目前市场占有率最高的公有云, 以可选服务数量最多, 功能最全, 上手难度最低而闻名. 如果你的代码在 GitHub 上, 而应用部署在 AWS 上, 那么就必然涉及如何为 GitHub Actions 中运行的 CI/CD 程序配置适当的 AWS 权限问题. 


Why Not Using AWS Access Key
------------------------------------------------------------------------------
大部分开发者接触 AWS 都是从创建 IAM User, 使用 Access Key 和 Secret Key 开始的. 但在 GitHub Actions 中使用这种方式有几个明显缺点: 

1. 需要为每个 GitHub Repository 管理 Actions Secret. 若 Repo 数量多, 管理工作量将大幅增加. 
2. Access Key 可能因误操作而存在泄露风险. 

对于简单的, 临时性的实验项目, 这种做法尚可接受. 但在企业和生产环境中, 显然需要更安全的解决方案. 下面我们来介绍正确的做法. 


What is OIDC
------------------------------------------------------------------------------
在介绍正确做法前, 我们首先需要了解核心技术概念 OIDC. OIDC (OpenID Connect) 是一种身份验证协议, 它允许用户使用一个身份提供者 (Identity Provider, IDP) 的凭据来访问多个应用程序. 例如, "使用 Google 账号登录", "使用 Microsoft 账号登录", "使用 Facebook 账号登录"等选项之所以存在, 是因为这些公司都提供了以自身为 IDP 的 OIDC 集成服务, 使任何网站只要集成它们的 SDK 就能支持这些第三方账号登录. 


How GitHub OIDC Works with AWS
------------------------------------------------------------------------------
简单来说, GitHub 与 AWS 有合作关系. 用户可以在 AWS IAM Identity Provider 中创建一个 GitHub IDP 的 AWS 资源. 创建此资源相当于声明: "我的 AWS 账户信任 GitHub 了". 

接着, 用户可以创建一个 IAM Role, 在其 Trusted Identity Document 中定义允许 GitHub IDP 来 Assume 这个角色. 最后, 在 GitHub Actions 中使用 AWS 官方维护的 `configure-aws-credentials <https://github.com/marketplace/actions/configure-aws-credentials-action-for-github-actions>`_ 这个 Action, 只需指定 role-to-assume 为前面创建的 IAM Role, CI 环境中的默认 AWS Credentials 就会被替换成该 IAM Role 的临时凭证. 这样就能安全地访问 AWS 资源了. 

我们用拟人化的表述来复盘整个过程: 当你运行 GitHub Actions 时, configure-aws-credentials 会去"询问 AWS": "你认识我吗？"由于我们在 AWS 账户中创建了这个 IDP, AWS 回复说: "认识". 然后 GitHub Actions 表示: "我现在已经是 IDP 这个 IAM Principal 了, 我可以 assume 这个 IAM Role 吗？"由于 IAM Role 的 Trusted Identity Document 中已声明可以, GitHub Actions 便获得了该 IAM Role 的临时凭证. 

相比使用 Access Key 的方法, 这种做法全程没有涉及显式的访问密钥, 也就不存在泄露风险. 而整个信任链是由 GitHub 和 AWS 两家大公司维护的, 安全性自然比自行维护要高得多. 


What's Next
------------------------------------------------------------------------------
相信你已经迫不及待想要亲自尝试了. 这里我推荐一个实用工具: 由于我需要为众多不同公司, 大量 GitHub 仓库和多个 AWS 账户配置这套机制, 我专门开发了 `gh_action_open_id_in_aws <https://github.com/MacHu-GWU/gh_action_open_id_in_aws-project>`_ 这个 Python 库工具, 可以帮助你快速配置好这一切. 这个库的使用方式与 AWS CDK 类似, 你可以直接在 Python 代码中使用它. 
