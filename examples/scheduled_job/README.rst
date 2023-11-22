Scheduled Job
==============================================================================
GitHub Action 支持用 cron expression 设置定时任务.

例如:

- ``*/5 * * * *``: every 5 minutes
- ``0 8 * * *``: at 8AM every day
- ``0 8 1 * *``: at 8AM every 1st day of the month

这里有一些工具可以帮助你学习以及生成 cron expression:

- `A Guide To Cron Expressions <https://www.baeldung.com/cron-expressions>`_: 一个 cron expression 的指南
- `crontab guru <https://crontab.guru/>`_: 一个自动解释 cron expression 的工具, 帮助你理解 cron expression 的含义
- `OpenAI chatgpt <https://chat.openai.com/>`_: 你把你的需求告诉它, 它会帮你生成 cron expression, 然后再回到 crontab guru 中验证即可
