GitHub Actions Overview
==============================================================================
GitHub Actions 是 2018-08-16 上线的一款由 GitHub 提供的 CI/CD 产品. 微软看中了 GitHub 上无数的开源代码数据, 为了利用这些数据训练 AI, 跟自家的产品深度整合构建护城河, 微软于是于 2018 年 10 月完成了对 GitHub 的收购. 以后 GitHub 背靠微软, 以及 Azure 云, 基本上所有的功能的费用都是同类产品最低, 因为微软根本不打算靠这个挣钱. 虽然 GitHub Actions 跟其他 CI 产品相比资历尚浅, 但是背靠微软这颗大树, 以及没有历史包袱, GitHub Actions 的新功能以及社区活跃度都是同类产品中首屈一指的. 非常值得投入时间学习.


The Nature of CI/CD
------------------------------------------------------------------------------
如果你把市场上流行的 CI/CD 产品 (GitHub Actions, GitLab CI, BitBucket Pipeline, CircleCI, Jenkins, AWS CodeBuild) 放在一起看, 跑开各个供应商自己定义的术语和概念, 我们可以发现一个 CI/CD 产品的核心是 **Step**, Build **Job** (简称 Job), **Workflow** (简称 WF) 三部分. 注意, 虽然 GitHub Action 中也有这些概念, 但是本节中提到的是我们总结的抽象概念.

- **Step** 的本质是按顺序执行的一堆 Command Line 命令. 在有些 CI 系统中会有将多个 Step 打包成一个组 (没错, 说的就是 Jenkins 里的 Stage). 但是本质上来说都是对 Step 的封装. 在执行 Step 的时候可能会有一些上下文环境, 例如环境变量, 当前工作目录等. 简单来说, Step 就是对自动化代码级的抽象.
- **Job** 的本质是一个在一个特定的环境 (操作系统, 内存) 中运行许多 Step. 一个 Job 都是一个全新的计算资源, 不同的 Job 中的程序是物理隔离的, 无法互相访问. 每次启动一个 Job 的时候都要重新拉取代码. 而 Job Run 可以被各种各样的事件所触发, 例如 Git push 事件. 大部分 CI 产品都提供了在 Job 之间传递参数, 传递 Artifacts 的功能. 简单来说 Job 是对业务逻辑级的抽象, 也是对一个 CI/CD 工作流的编排.
- **Workflow** 的本质是对 Job 的编排. 不同的 Job 之间的依赖关系可能有顺序执行, 并行执行. Job 出现错误时可能需要立刻停止, 也可以忽略错误继续执行. 有些 CI 系统中 Workflow 也可以对其他 Workflow 进行编排. Workflow 也可以被各种各样的事件所触发, 例如 Git push 事件. 简单来说 Workflow 本身不执行任何代码, 它只是对 Job 的编排.

有了以上三个概念再回头看这些 CI 产品:

- GitHub Actions 中, GitHub Action Step 就是上面的 Step, GitHub Action Job 就是上面的 Job, GitHub Action Workflow 就是上面的 Workflow.
- AWS CodeBuild 中的 commands 就是 Step, CodeBuild Job Run 就是 Job, CodePipeline 就是 Workflow.


Knowledge Graph
------------------------------------------------------------------------------
本节把 GitHub Action 的知识点做了一个总结. 在学习的时候可以照着这个知识图谱来查漏补缺.

.. dropdown:: Basic

    - CI/CD: CI/CD 的本质是 Build (CI), 一个能运行一堆命令的 runtime, 以及 Orchestration (CD), 将这些 Build job run 编排起来. 这是核心功能中的核心功能.
        - Orchestration:
            - `Using workflows <https://docs.github.com/en/actions/using-workflows>`_: workflow 是编排的核心, 这篇是 GitHub Actions Workflows 文档的入口.
            - `Defining prerequisite jobs <https://docs.github.com/en/actions/using-jobs/using-jobs-in-a-workflow#setting-a-name-for-a-job>`_: 这篇文档介绍了如何定义 job 之间的先后顺序关系
            - `Using conditions to control job execution <https://docs.github.com/en/actions/using-jobs/using-conditions-to-control-job-execution>`_: 这篇文档介绍了如何用 if else 来控制 job 是否执行
            - `jobs.<job_id>.steps[*].if <https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idstepsif>`_: 这篇文档介绍了如何用 if else 来控制 step 是否执行
            - `Using a matrix for your jobs <https://docs.github.com/en/actions/using-jobs/using-a-matrix-for-your-jobs>`_: 这篇文档介绍了如何用矩阵构建方式来并行运行很多 job. 通常用于不同操作系统, 不同软件版本, 不同参数的组合运行.
        - Build
            - Job, `Using jobs in a workflow <https://docs.github.com/en/actions/using-jobs/using-jobs-in-a-workflow>`_, 这篇是介绍 Job 的官方文档.
            - Step, `jobs.<job_id>.steps <https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idsteps>`_ 这篇文档介绍了 step 语法的各种选项和用法.
    - Trigger: 如何触发一个 workflow, 常见的方式有通过 PR, commit 到特定 branch, 或是定时触发.
        - Ref:
            - `Events that trigger workflows <https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows>`_
    - `Environment Variables <https://docs.github.com/en/actions/learn-github-actions/variables>`_: 环境变量是将 CI 参数化的关键技术之一.
    - `Context <https://docs.github.com/en/actions/learn-github-actions/contexts>`_: Context 是用来访问 CI 的运行时数据的方式, 例如在一个 job 内访问当前的 job 的名字, 开始时间等.
    - Security: 在 CI 中使用一些例如密码的敏感信息的最佳实践.
        - Ref:
            - `Security guides <https://docs.github.com/en/actions/security-guides>`_
    - Runner: runner 是 GitHub action 用来运行程序的机器, 主要是虚拟机而不是容器.
        - Ref:
            - `About GitHub-hosted runners <https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners/about-github-hosted-runners>`_: 这篇文档详细介绍了 GitHub hosted runner 的操作系统, 内存 CPU, 操作系统权限, 网络等信息.
            - `Supported software <https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners/about-github-hosted-runners#supported-software>`_: 这篇文档列出了自带的 Runner 上所有预装的软件和工具.
    - `Reuse Workflows <https://docs.github.com/en/actions/using-workflows/reusing-workflows>`_: 如何复用 Workflow yaml 文件, 避免重复造轮子.
    - `Manual Approve <https://docs.github.com/en/actions/managing-workflow-runs/reviewing-deployments>`_: 如何强制要求手动 approve 一个 Job Run, 通常用于部署到 Production 之前.

.. dropdown:: Advanced

    - `Find and Customize Actions <https://docs.github.com/en/actions/learn-github-actions/finding-and-customizing-actions>`_: Actions 相当于是给 GitHub Actions CI 专用的包, 把一些常用的 CI 功能打包成一个个的 Action, 发布到 Marketplace 平台上, 从而避免了为了重复的功能写大量 YAML 的麻烦.
    - `Deployment <https://docs.github.com/en/actions/deployment>`_: 如何部署 App, 以及如何部署到各种云平台上.
    - `Publishing Package <https://docs.github.com/en/actions/publishing-packages>`_: 如何将 Artifacts 打包上传, 以及上传到各种 Host 系统时的权限问题.
    - `Using container services <https://docs.github.com/en/actions/using-containerized-services>`_: 很多测试需要依赖于 database 之类的其他资源, 在本地开发时我们往往会用容器来模拟这些生产环境资源. GitHub Actions 可以用 side-car 模式在 CI 中自动配置这些资源.
    - `GitHub Hosted Runner <https://docs.github.com/en/actions/using-github-hosted-runners>`_: GitHub Actions 自带的 Runner 机器的详细配置, 以及上面预装的软件.
    - `Security Guide <https://docs.github.com/en/actions/security-guides>`_: 数据和网络安全最佳实践.
    - `Monitoring and Trouble Shooting <https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows>`_: 如何监控和排查 CI 的问题.

.. dropdown:: Python Related

.. dropdown:: AWS Related

    - AWS and GitHub OpenID:
        - Ref:
            - `Using OpenID Connect to access cloud resources <https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions#using-openid-connect-to-access-cloud-resources>`_: 这是有关用 OpenID 让 GitHub Action 访问 Cloud Provider 上的 Resource (例如 AWS) 的 GitHub 官方文档.
            - `Configuring OpenID Connect in Amazon Web Services <https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services>`_
