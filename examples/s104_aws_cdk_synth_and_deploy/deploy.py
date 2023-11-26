# -*- coding: utf-8 -*-

import subprocess
from pathlib import Path

# List of commands you want to run in parallel
dir_here = Path(__file__).absolute().parent
commands = []
for stack in ["stack1", "stack2"]:
    args = [
        "python",
        str(dir_here.joinpath("cdk_deploy.py")),
        stack,
    ]
    cmd = " ".join(args)
    commands.append(args)

# Start all the processes
processes = [subprocess.Popen(cmd) for cmd in commands]

# Wait for all processes to complete
for proc in processes:
    proc.wait()
