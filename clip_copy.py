import sys
from rich import print as rprint
from rich.panel import Panel
from pyperclip import copy

def main(argument: list): 
    try:
        # print(argument[1])
        copy(get_text(argument[1], int(argument[2]), int(argument[3])))
    except IndexError:
        print("Invalid format.")
        print("Use format clipcopy <filename> <starting_line> <ending_line>")
        exit()

def get_text(filename: str, line_start: int, line_end: int) -> str:
    line_list: list
    relevant_lines: list
    line_str: str

    with open(filename, 'r') as my_file:
        line_list = my_file.readlines()
        relevant_lines = line_list[line_start-1:line_end]
        line_str = ''.join(relevant_lines)[:-1]

    copied_color = "#81d400"
    rprint(
        Panel.fit(
            f"[{copied_color}]{line_str}[/]", 
            title="[#fff176] [/][white bold]Text copied[/] [#fff176] [/]"
        )
    )

    return line_str

if __name__ == "__main__":
    main(sys.argv)

