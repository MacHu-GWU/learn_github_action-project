Context Information
==============================================================================
Context 是一些在运行 Workflow 的过程中自带的变量. 你可以再 Workflow YAML 文件中用 ``${{ context_name.key }}`` 的方式来引用这些值. 常见的 context 有:

1. GitHub repo name
2. branch name
3. commit id
4. environment variable
5. secrets
6. workflow inputs

这里有个地方要注意, 不是在 yaml 中的任何地方都可以使用这些 context 的, 每个 context 有自己的 availability scope, 详情请参考 `Context Availability <https://docs.github.com/en/actions/learn-github-actions/contexts#context-availability>`_ 文档. 这里一个常见的坑是 ``${{ env.ENV_NAME }}``, 用环境变量来传递参数是很方便, 但是的确在很多地方是无法使用这个 context 的, 例如 ``jobs.<job_id>.if``, ``jobs.<job_id>.uses``. 一般凡是你想要用 env 但是用不了的时候就可以考虑用 ``on.workflow_dispatch.inputs`` 来定义 workflow 的入参, 然后再这些地方引用.


Sample Workflow Definition
------------------------------------------------------------------------------
.. literalinclude:: ../../../../.github/workflows/01_04_environment_variables.yml
   :language: yaml
   :linenos:


Reference
------------------------------------------------------------------------------
- `Context <https://docs.github.com/en/actions/learn-github-actions/contexts>`_: 关于 context 的官方文档.
- `Context Availability <https://docs.github.com/en/actions/learn-github-actions/contexts#context-availability>`_:
