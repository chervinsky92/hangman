from random import choice
from hangman_graphics import stages, logo
from hangman_words import word_list
from replit import clear

print(logo)

chosen_word = choice(word_list)
# print(chosen_word)
lives = 6
end_of_game = False

display = []
for _char in chosen_word:
    display.append('_')

while end_of_game == False:
    guess = input('Guess a letter: ').lower()

    clear()

    if guess in display:
        print(f' You have already guessed {guess}.')

    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess
        
    if '_' not in display:
        print('You win!')
        end_of_game = True
        
    print(' '.join(display))

    if guess not in chosen_word:
        print(f"You guessed {guess} but that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            print('You lose.')
            end_of_game = True

    print(stages[lives])

clear()
    
    
