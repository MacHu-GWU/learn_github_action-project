Sensitive Data
==============================================================================
让你在 CI Job 中运行的程序能访问一些敏感数据, 例如登录密钥, 数据库密码等是非常常见的需求. GitHub Action 中对敏感信息的管理的核心是 `secrets <https://docs.github.com/en/actions/learn-github-actions/contexts#secrets-context>`_ Context. 你可以在网站里定义 secrets, 然后用 Context 将这些 secrets 传递给 environment variable 所使用. 详情请参考 `Security Guide <https://docs.github.com/en/actions/security-guides>`_

这里要注意的一点是, 凡是被定义为 secrets 的值, 一旦在 log 中出现这些值, GitHub Action 会自动将其 mask 掉. 非常人性化.

但是这里也会有个小坑, 例如你把你的内部系统的网址设为了敏感信息, 如果你在 log 中打印了你的网址信息, 希望开发者能点击跳转, 这时 GitHub Action 就会将其 mask 掉. 但这是开发者自己的错, 既然将这个值视为 secret, 你就不应该将他打印出来.

这里还有小技巧. 如果有的 secret 是你用户 ID, 电话号码, SSN 之类的信息, 但你确实有将其打印出来进行辨别的需求, 这时你可以将其设为 Secret, 但是在打印的时候只打印前三位或后四位.


Sample Workflow Definition
------------------------------------------------------------------------------
.. literalinclude:: ../../../../.github/workflows/01_08_sensitive_data.yml
   :language: yaml
   :linenos:


Sample Workflow Run
------------------------------------------------------------------------------
::

    masked secret:
    ***
    first four digits:
    1234
