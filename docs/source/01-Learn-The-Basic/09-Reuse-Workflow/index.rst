.. _reuse-workflow:

Reuse Workflow
==============================================================================
GitHub Actions 中的 Reuse Workflow 和 `CircleCI Orb <https://circleci.com/orbs/>`_, 都是为了解决 YAML 代码复用, 参数化而设计的机制.

它的本质就是用一个 Workflow 去 Call 另一个 Workflow (用 ``${Organization}/${Repository}/${PathToYamlFile}@${reference}`` 这样的格式去调用).


1. Basic Usage
------------------------------------------------------------------------------
这里的关键就是 Worker (被调用方) 需要在 ``on`` 里加一个 ``workflow_call:`` trigger. 然后再 Caller (调度方) 用 ``jobs.<job_id>.uses`` 指定使用 Worker 的 yaml file. 具体格式是 ``${Organization}/${Repository}/${PathToYamlFile}@${reference}``.

Caller

.. literalinclude:: ../../../../.github/workflows/01_09_01_reusable_workflow_caller.yml
   :language: yaml
   :linenos:

Worker

.. literalinclude:: ../../../../.github/workflows/01_09_01_reusable_workflow_worker.yml
   :language: yaml
   :linenos:


2. Reuse a Workflow in the Same Branch
------------------------------------------------------------------------------
前面的例子介绍了, 引用一个 Workflow 需要指定 ``@${reference}``, 也就是 branch / tag / commit_id. 如果你不指定的话就会使用默认 branch. 但有的时候你在一个 feature branch 上的开发任务就是 workflow yaml file 本身, 你可不想把你的 feature branch hardcode 在 ``@${reference}`` 里.

凭直觉, 你可能会想要用 ``${{ github.base_ref }}`` 这个 context 来取代 ``main``, 但是很不幸, 这个 context 在 ``jobs.<job_id>.uses`` 里是不支持的.

GitHub 在 2022-01-25 发布了一个新功能, 现在你能用相对路径的语法来指定一个同 branch 上的 yaml 文件了

- GitHub Actions: Reusable workflows can be referenced locally: https://github.blog/changelog/2022-01-25-github-actions-reusable-workflows-can-be-referenced-locally/

Caller

.. literalinclude:: ../../../../.github/workflows/01_09_02_reusable_workflow_caller.yml
   :language: yaml
   :linenos:

Worker

.. literalinclude:: ../../../../.github/workflows/01_09_02_reusable_workflow_worker.yml
   :language: yaml
   :linenos:


4. Multiple Project Release in Mono Repo
------------------------------------------------------------------------------
在 Monorepo 项目中, 你可能会用多个项目文件夹隔离不同的项目. 每一个项目都是一个 deployment unit, 都会有一个自己的 workflow 让自己分别部署. 但有的时候你会希望将这些 workflow 一次性部署. 这应该如何实现比较好呢?

可以这样做, 由于是 mono repo, 你的每个 project 的 release 都是放在 ``${project_name}/release`` branch 上做的.

而如果你要一次性的 release 多个项目, 你则是在 ``all/release`` branch 上做, 并且直接在这个 branch 上修改 caller 的 workflow yaml file 即可. 你要 release 几个项目就启用几个项目即可, 不需要的项目就 comment 掉.

Caller

.. literalinclude:: ../../../../.github/workflows/01_09_04_reusable_workflow_caller.yml
   :language: yaml
   :linenos:

Project 1 Worker

.. literalinclude:: ../../../../.github/workflows/01_09_04_reusable_workflow_project1.yml
   :language: yaml
   :linenos:

Project 2 Worker

.. literalinclude:: ../../../../.github/workflows/01_09_04_reusable_workflow_project1.yml
   :language: yaml
   :linenos:


Reference
------------------------------------------------------------------------------
- Reusing workflows: https://docs.github.com/en/actions/using-workflows/reusing-workflows
