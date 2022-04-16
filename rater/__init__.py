from typing import List
from rich.console import Console

console = Console()

def isfloat(value: int) -> bool:
    """Checks if the given value is a float"""
    try:
      float(value)
      return True
    except ValueError:
      return False

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

