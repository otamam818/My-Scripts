from typing import List
from rich.console import Console
from rich.table import Table

console = Console()

finlist = []

def main():
    # Set up a way to handle keyboard interrupts
    try:
        if (len(finlist) != 0):
            console.print(get_table())
            options = [
                "Add a new rating",
                "Delete a rating",
                "Edit a rating"
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
        while not(item_rating.isnumeric()):
            item_rating = console.input("Rating: ")
        item_rating = round(int(item_rating))
        finlist.insert(item_rating, item_name)
    "2. Delete a rating"
    "3. Edit a rating"

def get_table() -> Table:
    table = Table(title="Rater", header_style="#ff8a65 bold")
    for i in ["Item", "Rating"]:
        table.add_column(i)

    count = 1
    for i in finlist:
        table.add_row(i, str(count))
        count += 1

    return table

class Prompt:
    @staticmethod
    def ask_options(question: str, options: List[str]) -> int:
        question_style = "bold white"
        console.print(question, style=question_style)
        for i in range(1, len(options)+1):
            option_number_style = "bold #fff176" # yellow
            console.print(i, style=option_number_style, end=' ')
            console.print(options[i-1])

        choice: str = ""
        while not(choice.isnumeric()):
            console.print("Enter a [b i white]number[/]: ", end='')
            choice = input()
            if not(choice.isnumeric()):
                console.print("Error", style="#e53935 bold") # red
                console.print("Not a number.\nPlease enter a [i]number[/]")
        return int(choice)

if __name__ == "__main__":
    main()

