#Step 1 
import random
from graph import stages

def get_secret_letters(words = ["aardvark", "baboon", "camel"]):
    letters = str (random.choice(words))
    return letters

def print_words_blanks(letters):
    blanks = ""
    for index in range (len(letters)):
        blanks += "_ "
    print (blanks)

def get_input():
    user_input = input ("Please guess a letter:\n").lower()
    return user_input

def is_guess_the_words(letter, words):
    guessed_indexes = []
    for index in range(len(words)):
        if(words[index] == letter): 
            print("append "+ str(index) + " into gussed_indexes")
            guessed_indexes.append(index)
    return guessed_indexes


def get_new_words_with_blanks(guessed_indexes, words: str):
    words_with_blanks = ""
    for index in range(len(words)):
        if index in guessed_indexes:
            words_with_blanks += words[index]
        else:
            words_with_blanks += "_"
    return words_with_blanks

def is_all_blanks_filled(words: str):
    result = True
    for index in range(len(words)):
        if words[index] == "_" :
            result = False
    return result

def remaining_life(guessed_indexes, life):
    new_life = life
    if len(guessed_indexes) == 0:
        new_life = life - 1
    return new_life

def is_run_out_of_life(life):
    return life == 0;


life=7

secret_words = get_secret_letters()
print(secret_words)
print_words_blanks(secret_words)


game_is_over = False
found_indexes = []

while(game_is_over == False):
    # get user input
    user_input = get_input()

    guessed_indexes = is_guess_the_words(user_input, secret_words)
    for index in range(len(guessed_indexes)):
        current_value = guessed_indexes[index]
        if current_value not in found_indexes:
            found_indexes.append(current_value)

    print(guessed_indexes)

    print('found indexes: ' + str(found_indexes))

    found_guess = False
    if len(guessed_indexes) > 0:
        found_guess = True
        print (" found, Game is not over")

        new_words = get_new_words_with_blanks(found_indexes, secret_words)
        print("you found: " +  new_words)
        if is_all_blanks_filled(new_words) == True:
            print ("Game Over")
            game_is_over = True
    else:
        print ("not found, Game is not over")
        life = remaining_life(guessed_indexes, life)
        print("you have " + str(life) + " life")
        print (stages[life])
        if is_run_out_of_life(life):
            print ("Game Over, out of life")
            game_is_over = True

    
