Matrix Build for OpenSource
==============================================================================
本例的实例 GitHub action workflow yaml 文件在 `cache_python_package_dependencies.yml <../../.github/workflows/s101_cache_python_package_dependencies.yml>`_.

这里有一些 `示例的 Build <https://github.com/MacHu-GWU/learn_github_action-project/actions/workflows/s102_matrix_build_for_opensource.yml>`_.


Overview
------------------------------------------------------------------------------
对于开源软件, 在 Windows 和 Linux 平台下, 对多个 Python 版本进行充分测试是保证软件质量的关键. 这里的关键技术是用 `GitHub action matrix <https://docs.github.com/en/actions/using-jobs/using-a-matrix-for-your-jobs>`_ 同时对多个平台的多个版本进行测试.
