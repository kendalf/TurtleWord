# Import necessary modules
import typer
import turtleGameLogic

app = typer.Typer(add_completion=False)


"""@app.callback(invoke_without_command=True)
def callback():
  randword()"""


@app.command()
def play(wlength: int = 5, guesses: int = 6, difficulty: int = 5, swears: bool = False):
  """
  Play a game of Turtle.
  Its like that popular word guessing game but with a shell!
  Set the word length, number of guesses, and difficulty (1-10).
  """
  turtleGameLogic.start_game(wlength, guesses, difficulty)


# Generate random 5-letter word
@app.command()
def randword(length: int = 5, freq: int = 5):
  """
  Generate a random word of a given length.
  --length: The length of the word to generate.
  --freq: (1-10) Lower numbers are restricted to more common words
  """
  print(turtleGameLogic.generate_word(length, freq))


# Call main function
if __name__ == "__main__":
  turtleGameLogic.init()
  app()
  