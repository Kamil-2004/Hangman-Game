import random

stages = [
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]

# Sample word_list and logo (these should be defined or imported from a module if necessary)
word_list = ["ardvark", "baboon", "camel"]
logo = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
'''

end_of_game = False
lives = 6

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print(logo)

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

print(display)

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You have already guessed {guess}")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(display)

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You won!")

    # Check if guess is not in the chosen_word
    if guess not in chosen_word:
        lives -= 1
        print(f"You have {lives} lives left")
        if lives == 0:
            end_of_game = True
            print("You lose!")
            print(f"The chosen word was: {chosen_word}")

    print(stages[lives])