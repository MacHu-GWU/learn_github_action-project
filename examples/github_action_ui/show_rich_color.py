# -*- coding: utf-8 -*-

from rich.console import Console

# console = Console() # this works in terminal, but won't show color in GitHub action
console = Console(force_terminal=True) # this can show color in GitHub action

data = {
    "name": "Show rich color",
    "description": "Show rich color",
    "author": "nobody",
}
console.print(data)
console.print("Hello", "World!", style="bold red")
