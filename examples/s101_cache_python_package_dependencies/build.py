# -*- coding: utf-8 -*-

import subprocess
from pathlib import Path

if Path(".venv").exists() is False:
    subprocess.run(
        [
            "virtualenv",
            "-p",
            "python3.9",
            ".venv",
        ]
    )
    subprocess.run(
        [
            "poetry",
            "install",
        ]
    )
