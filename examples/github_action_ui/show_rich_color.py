# -*- coding: utf-8 -*-

from rich.console import Console

console = Console(force_terminal=True)


data = {
    "name": "Show rich color",
    "description": "Show rich color",
    "author": "nobody",
}
console.print(data)
console.print("Hello", "World!", style="bold red")