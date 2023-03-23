word_list = ["UDEMY", "APPMILLERS", "PYTHON"]
import random
from logo_stages import logo,hangman_stages
from replit import clear
print(logo)
secret_word = random.choice(word_list)
length_word = len(secret_word)
blanks = []

for _ in range(length_word):
    blanks.append("_")

print(" ".join(blanks))


lives=6
guessed_letters = []
end_game = False
while not end_game:
    guess = input("Guess a letter: ").upper()
    clear()
    if guess in guessed_letters:
        print("You have already guessed this letter!")
        
        continue
    else:
        guessed_letters.append(guess)
    #print(guessed_letters)
    
    for position in range(length_word):
        letter = secret_word[position]
        if guess == letter:
            blanks[position] = letter
    if guess not in secret_word:
      lives-=1
    if lives==0:
      end_game=True
      print("You lose!")
      
   
    final_string=" ".join(blanks)      
    print(final_string)
    print(hangman_stages[lives])
  
    if "_" not in blanks:
        end_game = True
        print("You win!")# only claim win or lose when while loops ends
    if end_game:
      ask=input("Do you want to play again? (Y/N)")
      if ask=="Y":
        secret_word = random.choice(word_list)
        length_word = len(secret_word)
        blanks.clear()
        for _ in secret_word:
          blanks.append("_")
        print(" ".join(blanks))
        end_game=False
        lives=6
        guessed_letters.clear()
      else:
        print("See you next time!")
