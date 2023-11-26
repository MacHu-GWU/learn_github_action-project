Learn GitHub Action
==============================================================================
本仓库是我用来学习 `GitHub Action <https://docs.github.com/en/actions>`_ 时候做的笔记和测试用的代码. 作为最流行的 Git 仓库和 CICD 产品之一, 我认为投入精力学习 GitHub Action 很有必要. 但是由于它的内容较多, 我很难记住所有的细节. 所以我决定把学习过程中的笔记和代码都放在这个仓库里, 以便日后查阅, 做到在 5 分钟内查到并 pick up 所需要的知识点和细节.

.. contents::
    :depth: 1
    :local:


Knowledge Graph
------------------------------------------------------------------------------
- CI/CD: CI/CD 的本质是 Build (CI), 一个能运行一堆命令的 runtime, 以及 Orchestration (CD), 将这些 Build job run 编排起来. 这是核心功能中的核心功能.
    - Orchestration:
        - Ref:
            - `Using workflows <https://docs.github.com/en/actions/using-workflows>`_: workflow 是编排的核心
            - `Defining prerequisite jobs <https://docs.github.com/en/actions/using-jobs/using-jobs-in-a-workflow#setting-a-name-for-a-job>`_: 这篇文档介绍了如何定义 job 之间的先后顺序关系
            - `Using conditions to control job execution <https://docs.github.com/en/actions/using-jobs/using-conditions-to-control-job-execution>`_: 这篇文档介绍了如何用 if else 来控制 job 是否执行
            - `jobs.<job_id>.steps[*].if <https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idstepsif>`_: 这篇文档介绍了如何用 if else 来控制 step 是否执行
            - `Using a matrix for your jobs <https://docs.github.com/en/actions/using-jobs/using-a-matrix-for-your-jobs>`_: 这篇文档介绍了如何用矩阵构建方式来并行运行很多 job. 通常用于不同操作系统, 不同软件版本, 不同参数的组合运行.
    - Build
        - Job: 一个 Job 是在一个特定的环境 (操作系统, 内存
            - Ref: `Using jobs in a workflow <https://docs.github.com/en/actions/using-jobs/using-jobs-in-a-workflow>`_
        - Step: `jobs.<job_id>.steps <https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idsteps>`_
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
- AWS and GitHub OpenID:
    - Ref:
        - `Using OpenID Connect to access cloud resources <https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions#using-openid-connect-to-access-cloud-resources>`_: 这是有关用 OpenID 让 GitHub Action 访问 Cloud Provider 上的 Resource (例如 AWS) 的 GitHub 官方文档.
        - `Configuring OpenID Connect in Amazon Web Services <https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services>`_


Table of Content
------------------------------------------------------------------------------
- Python
    - `s101_cache_python_package_dependencies <../../examples/s101_cache_python_package_dependencies/README.rst>`_
