import subprocess
from rich.console import Console

console = Console()

SH_FILE: str = "update.sh"

def main():
    lines: list = get_lines()
    console.rule(f"Running {SH_FILE}", style="#00FF00")
    for line in lines:
        with console.status(f"[b]Currently running:[/] {line}"):
            subprocess.run(line.split())
        console.print(f"[b]Completed:[/] [#00FF00]{line}[/]")
    console.rule(f"Completed!", style="#00FF00")

def get_lines() -> list:
    ans: list
    with open(SH_FILE, "r") as my_file:
        ans = my_file.readlines()
    return [i for i in ans if len(i) > 1]

if __name__ == "__main__":
    main()

