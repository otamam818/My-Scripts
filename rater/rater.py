from typing import List
from rich.console import Console
from rich.table import Table
from __init__ import *
from math import floor

console = Console()

finlist = []

def main():
    # Set up a way to handle keyboard interrupts
    try:
        # We don't need to print the table if its not
        if (len(finlist) != 0):
            console.print(get_table())
            options = [
                "Add a new rating",
                "Delete a rating",
                "Edit a rating",
                "Copy to clipboard",
                "Export as .txt file"
            ]
        else:
            options = ["Add a new rating"]
        choice = Prompt.ask_options(
            question = "What would you like to do?",
            options = options
        )

        parse_choices(choice)
        main()
    except KeyboardInterrupt:
        console.print("\nGood bye", style="#ffff00")

def parse_choices(choice):
    "1. Add a new rating"
    if choice == 1:
        item_name   = console.input("Name of item: ")
        item_rating = ""
        # TODO: Parse for floats
        while not(isfloat(item_rating)):
            item_rating = console.input("Rating: ")
        item_rating = floor(float(item_rating))
        finlist.insert(item_rating, item_name)
    # 2. Delete a rating
    elif choice == 2:
        pass
    # 3. Edit a rating
    elif choice == 3:
        pass

def get_table() -> Table:
    table = Table(title="Rater", header_style="#ff8a65 bold")
    for i in ["Item", "Rating"]:
        table.add_column(i)

    count = 1
    for i in finlist:
        table.add_row(i, str(count))
        count += 1

    return table

if __name__ == "__main__":
    main()

