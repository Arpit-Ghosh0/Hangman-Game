import random
from hangman_words import word_list
from hangman_art import stages,logo
lives = 6 ##Initialize that user has 6 lives
print(logo) ##hangman Logo
chosen_word = random.choice(word_list) ##Random word Choosen for the user to guess
placeholder ="" ##creating a placeholder to show the user how many dashes or number of letters they are gonna guess
for position in range(len(chosen_word)):
    placeholder += "_"
print("Word to guess:"+ placeholder)

game_over = False ## initialize for while loop
correct_letters = []
while not game_over:
    print(f"**************************{lives}/6 lives left**************************")
    guess = input("Guess a letter: ").lower()
    if guess in correct_letters:
        print(f"You already guessed {guess}") ##handling if a user selectinjg the same letter again
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display+= letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print("Word to guess:"+display)

    if guess not in chosen_word:
        lives-=1
        print(f"**************************{lives}/6 lives left ************You lost a live!!**************")
    if lives==0:
        game_over = True
        print(f"*****Correct word: {chosen_word} ************You Lose!!**************")
    if "_" not in display:
        game_over = True
        print(f"*****Congratulations******You guessed the word {chosen_word}***********You Win!!***************")
    print(stages[lives])