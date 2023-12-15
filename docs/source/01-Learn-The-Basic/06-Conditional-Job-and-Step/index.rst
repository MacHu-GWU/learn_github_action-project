Conditional Job and Step
==============================================================================
有的 Job 或者 Step 你不是什么时候都想执行的. 例如你的 Job 种有一步是只有 Windows 机器上需要做的, 这时候你就可以用 ``if`` 语法进行条件判断, 只有条件判断返回 True 才能执行. 并且这个条件判断是可以用 ``||``, ``&&`` 来进行组合的.


Sample Workflow Definition
------------------------------------------------------------------------------
.. literalinclude:: ../../../../.github/workflows/01_06_conditional_job_and_step.yml
   :language: yaml
   :linenos:


Sample Workflow Run
------------------------------------------------------------------------------
.. image:: ./conditional-job-and-step.png


Reference
------------------------------------------------------------------------------
- job.<job_id>.if: https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idif
- jobs.<job_id>.steps[*].if: https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idstepsif
- Logical operators: https://docs.github.com/en/actions/learn-github-actions/expressions#operators
- Functions: https://docs.github.com/en/actions/learn-github-actions/expressions#functions
- Context Availability: https://docs.github.com/en/actions/learn-github-actions/contexts#context-availability
