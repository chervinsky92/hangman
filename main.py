from random import choice
from hangman_graphics import stages, logo
from hangman_words import word_list
from replit import clear

print(logo)

chosen_word = choice(word_list)
# print(f'Debugging: {chosen_word}')

lives = 6
end_of_game = False

# display will hold remaining blanks and user's correct guesses
display = []
for char in chosen_word:
    display.append('_')

while not end_of_game:
    guess = input('Guess a letter: ').lower()
    clear() # clear screen to avoid scrolling

    # user has already guessed correct letter
    if guess in display:
        print(f' You have already guessed {guess}.')

    # user makes correct guess -> display will update
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess

    print(' '.join(display))

    # user wins if display has no blanks remaining
    if '_' not in display:
        print('You win!')
        end_of_game = True
    
    # user makes an incorrect guess -> loses a life
    if guess not in chosen_word:
        print(f"You guessed {guess} but that's not in the word. You lose a life.")
        lives -= 1
        # user loses if lives reaches 0
        if lives == 0:
            print('You lose.')
            end_of_game = True

    # display hangman image relative to user's remaining lives
    print(stages[lives]) 
