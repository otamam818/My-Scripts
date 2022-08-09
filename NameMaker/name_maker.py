import subprocess
from rich.console import Console

console = Console()

def main():
    console.rule("[b]Name Maker[/]")
    try:
        while True:
            name = console.input("Enter [b]name:[/] ")
            out = "[b #11FF11]Randomized name: [/]" + get_name(name)
            console.print(out)
    except KeyboardInterrupt:
        print("")
        console.rule("[b]Good Bye![/]")

def get_name(name: str):
    """Generates a name based on the user choice"""
    command = ["java", "Main", f"'{name}'"]
    return subprocess.run(
        command,
        capture_output=True
    ).stdout.decode("utf-8")[1:-1]

if __name__ == "__main__":
    main()

