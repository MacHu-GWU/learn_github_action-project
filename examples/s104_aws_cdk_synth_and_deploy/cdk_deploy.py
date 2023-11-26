# -*- coding: utf-8 -*-

import os
import sys
import subprocess
from pathlib import Path


if __name__ == "__main__":
    stack = sys.argv[1]
    dir_here = Path(__file__).absolute().parent
    dir_stack = dir_here.joinpath(stack)
    os.chdir(str(dir_stack))
    args = [
        "cdk",
        "deploy",
        "--require-approval",
        "never",
    ]
    subprocess.run(args)
