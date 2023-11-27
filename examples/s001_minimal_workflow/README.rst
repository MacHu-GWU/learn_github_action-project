Minimal Workflow
==============================================================================
Assets:

- `s101_cache_python_package_dependencies.yml <../../.github/workflows/s101_cache_python_package_dependencies.yml>`_: GitHub Action Workflow file.
- `Sample build jobs <https://github.com/MacHu-GWU/learn_github_action-project/actions/workflows/s101_cache_python_package_dependencies.yml>`_


Overview
------------------------------------------------------------------------------
本例是一个最简单的 GitHub Action Workflow 工作流. 仅仅是把代码从 main branch 上 check out, 然后打印几行 Command Line 命令. 这个 workflow 没有任何 trigger, 只能由手动在 GitHub 网站 App 上, 或是用 API 触发.
