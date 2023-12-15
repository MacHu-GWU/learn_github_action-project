GitHub Actions Rest API
==============================================================================
GitHub 的 API 是市面上做的最好的一批之一. 也是最早一批使用 GraphQL API 的公司.

你可以用 GitHub API 来操作 Workflow. 例如创建一个 Workflow dispatch event.

使用 API 是要鉴权的, 最佳的做法是创建一个 Personal Access Token. GitHub API 是一个 HTTP request API, 你可以用 Python 的 request 库来做. 不过我推荐使用 PyGitHub 库, 用人类友好的方式对这些方法进行了封装. 下面给出了一个手动运行 Workflow 的一个脚本.

.. literalinclude:: ./github_action_rest_api_example.py
   :language: python
   :linenos:

Reference:

- Create a workflow dispatch event: https://docs.github.com/en/rest/actions/workflows?apiVersion=2022-11-28#create-a-workflow-dispatch-event
- PyGitHub: https://pygithub.readthedocs.io/en/latest/introduction.html
