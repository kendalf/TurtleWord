import random
from rich import print 

WORD_LIST_FILE = "google-10000-english-usa-no-swears.txt"
MAX_WORD_LENGTH = 50
word_list = [[] for x in range(MAX_WORD_LENGTH + 1)]

def init(file = WORD_LIST_FILE):
  with open(file, "r") as f:
    for line in f:
        word = line.strip()
        word_list[len(word)].append(word)


def generate_word(wlen = 5, freq = 5):
  """
  Generate a random word of length wlen with frequency freq.
  freq: (1-10) 1 = most common words 10 = least common words
  """
  if wlen > MAX_WORD_LENGTH or not word_list[wlen]:
    return ""
  word_num = len(word_list[wlen])
  freq = clamp(freq, 1, 10)
  word_num = int(float(freq)/10 * word_num)
  if not word_num:
    word_num = len(word_list[wlen])
  return word_list[wlen][random.randrange(word_num)]


def start_game(wlen = 5, max_guesses = 6, difficulty = 5):
  word = generate_word(wlen, difficulty)
  if not word:
    print(f"No word of length {wlen} found")
    return
  print("[magenta]Welcome to Turtle![/magenta]")
  print(f"[green]Guess the {wlen}-letter word:[/green]")
  guesses = 0
  while guesses < max_guesses:
      guess = input("Enter your guess " + str(guesses + 1) + ": ")
      if len(guess) != wlen:
          print(f"[red]Invalid guess. Please enter a {wlen}-letter word.[/red]")
          continue
      if guess == word:
          print("[bold green]Congratulations! You guessed the word in " + str(guesses + 1) + " guesses.[/bold green]")
          break
      else:
          display = ""
          for i in range(wlen):
              if guess[i] == word[i]:
                color = "bold green"
              elif guess[i] in word:
                color = "bold yellow"
              else:
                color = "bold red"
              display += "[" + color + "]" + guess[i] + "[/" + color + "] "
          print(display)
          guesses += 1
        
      if guesses == max_guesses:
          print("[blue]Sorry, you ran out of guesses. The word was [/blue][bold green]" + word + "[/bold green].")



def clamp(n, min, max): 
    if n < min: 
        return min
    elif n > max: 
        return max
    else: 
        return n 