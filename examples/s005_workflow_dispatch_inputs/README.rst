Workflow Dispatch Inputs
==============================================================================
Assets:

- `s005_workflow_dispatch_inputs.yml <../../.github/workflows/s005_workflow_dispatch_inputs.yml>`_: GitHub Action Workflow file.
- `Sample build jobs <https://github.com/MacHu-GWU/learn_github_action-project/actions/workflows/s005_workflow_dispatch_inputs.yml>`_


Overview
------------------------------------------------------------------------------
将工作流参数化有助于代码的复用以及更好的可读性. 在 Jenkins 中你可以定义参数然后让人在 Run 的时候输入这些参数, 又或者用 dropdown menu 来选择参数. 在 GitHub Action 中, 你可以使用 `on.workflow_dispatch.inputs <https://docs.github.com/en/enterprise-cloud@latest/actions/using-workflows/workflow-syntax-for-github-actions#onworkflow_dispatchinputs>`_ 来实现此功能. 其中 ``type: choice`` 可以实现 dropdown menu.

注意, 文档中提到的另一个方法 `on.workflow_call.inputs <https://docs.github.com/en/enterprise-cloud@latest/actions/using-workflows/workflow-syntax-for-github-actions#onworkflow_callinputs>`_ 是当你用一个 workflow call 其他的 workflow 时用的. 这里不涉及一个 workflow call 其他的 workflow 的情况.

