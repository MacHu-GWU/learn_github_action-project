Cache Python Package Dependencies
==============================================================================
本例的实例 GitHub action workflow yaml 文件在 `cache_python_package_dependencies.yml <../../.github/workflows/cache_python_package_dependencies.yml>`_.


Overview
------------------------------------------------------------------------------
Python 项目的 CI/CD 过程中一个必要步骤就是创建虚拟环境并安装依赖. 而这些依赖在一个项目的开发周期内并不会频繁变化. 而复杂的生产项目不仅有 App 所需的依赖, 还有测试, 部署, 自动化等需要的依赖. 这些依赖的安装过程可能会占据 CI 的时间的一半以上. 所以自然而然的就会想到, 如果我们能将这些依赖缓存起来, 那么下次安装的时候就可以直接使用缓存, 而不需要重新安装. 这样就可以大大减少 CI 的时间.

这个 ``setup-python`` GitHub Action 就提供了这一功能, 它可以将 pip, pipenv, poetry 的依赖缓存起来供下次使用. 详情请参考 `Caching packages dependencies <https://github.com/actions/setup-python#caching-packages-dependencies>`_ 官方文档.


依赖是如何被缓存起来的
------------------------------------------------------------------------------
虽然 ``setup-python`` 支持 pipenv, 但是由于 poetry 的设计明显比 pipenv 更完善, 所以我们主要学习 pip 和 poetry 的缓存过程.

每当你 pip install 的时候, pip 就会将包文件下载到 `pip 的缓存目录 <https://pip.pypa.io/en/stable/cli/pip_cache/>`_ 中. 如果下次安装的时候, pip 发现缓存目录中已经有了这个包, 那么就不会再去下载了. 而 ``setup-python`` 可以将整个 pip 缓存目录缓存起来. 那么我们如何知道该不该使用这个缓存呢? 对于 pip,  ``setup-python`` 会自动搜索 ``requirements.txt`` 或 ``pyproject.toml`` 文件, 并以这个文件的哈希值来作为缓存的 key. 也就是一旦这个文件发生改动 (通常也是你的依赖发生了改动), 就要重新构建缓存. 注意, pip 缓存只是节约了下载的时间, 还是要花时间安装的. 对于复杂的项目, 大约能减少 2/3 的安装时间. 你可以用 ``cache-dependency-path`` 参数来显式指定缓存的 key 是由哪个文件决定的.

而对于 poetry, ``setup-python`` 会将 ``poetry install`` 命令所找到的 virtualenv 目录整个缓存起来. 根据社区规定, 你如何将 ``.venv`` 作为目录名, poetry 是可以自动发现的. 这个好处是它缓存的是整个 virtualenv 目录, 你不仅不用下载了, 甚至还不用安装了. 而这个缓存的 key 是由于 ``poetry.lock`` 文件的哈希值来决定的. 同样的, 你也可以用 ``cache-dependency-path`` 参数 `来显式指定缓存的 key 是由哪个文件决定的 <https://github.com/actions/setup-python/blob/main/docs/advanced-usage.md#caching-packages>`_.


一些注意事项
------------------------------------------------------------------------------
``pip install`` 和 ``poetry install`` 命令在所有的包都已经安装完的情况下虽然不会安装任何包, 但仍然会执行检查看看这些包是不是已经装好了. 这个检查本身在包很多的时候也很耗时, 所以我推荐在你的 CI 脚本中用 ``[ ! -d ".venv" ] && virtualenv -p python3.9 .venv`` 和 ``[ ! -d ".venv/lib/python3.9/site-packages/boto3" ] && poetry install`` 的条件判断语句实现在检测到 poetry 缓存已经生效的情况下, 跳过创建虚拟环境和安装依赖的步骤.
