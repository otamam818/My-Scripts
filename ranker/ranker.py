from typing import List
from rich.console import Console
from rich.table import Table
from __init__ import *
from math import floor

console = Console()

finlist = []

def main():
    # Set up a way to let the user leave the program
    try:
        # We don't need to print the table if its empty
        if (len(finlist) != 0):
            console.print(get_table())
            options = [
                "Add a new item",
                "Delete a item",
                "Edit an item",
                "Copy to clipboard",
                "Export as .txt file"
            ]
        else:
            options = ["Add a new item"]
        choice = Prompt.ask_options(
            question = "What would you like to do?",
            options = options
        )

        parse_choices(choice)
        main()

    except KeyboardInterrupt:
        console.print("\nGood bye", style="#ffff00")

def parse_choices(choice):
    if choice == 1:
        add_item()

    elif choice == 2:
        delete_item()

    # 3. Edit a ranking
    elif choice == 3:
        pass

def add_item() -> None:
    item_name   = console.input("Name of item: ")
    item_ranking = ""
    while not(isfloat(item_ranking)):
        item_ranking = console.input("Rank: ")
        if not(isfloat(item_ranking)):
            console.print("Please enter a", end=' ')
            console.print("number", style="#ff0000 bold italic")
    item_ranking = floor(float(item_ranking))
    finlist.insert(item_ranking, item_name)

def delete_item() -> None:
    item_number: str = request_int("Which item would you like to delete?")
    finlist.pop(item_number-1)

def request_int(message) -> int:
    console.print(message)

    item_number_input = ""
    while (not(item_number_input.isnumeric())):
        item_number_input = console.input("Enter [i]number[/]: ")
        if (not(item_number_input.isnumeric())):
            console.print("Please enter a", end=' ')
            console.print("whole number", style="#ff0000 bold italic")
    
    return int(item_number_input)

def get_table() -> Table:
    table = Table(title="Ranker", header_style="#ff8a65 bold")
    for i in ["Item", "Ranking"]:
        table.add_column(i)

    count = 1
    for i in finlist:
        table.add_row(i, str(count))
        count += 1

    return table

if __name__ == "__main__":
    main()

