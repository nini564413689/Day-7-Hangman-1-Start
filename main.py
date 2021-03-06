#Step 1 
import random

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

# generate secret words
secret_words = get_secret_letters()
print(secret_words)


print_words_blanks(secret_words)

# get user input
user_input = get_input()
print (user_input)

guessed_indexes = is_guess_the_words(user_input, secret_words)
print(guessed_indexes)

found_guess = False
if len(guessed_indexes) > 0:
    found_guess = True

print(found_guess)

# if found_guess is True:
#     get_new_words_with_blanks()
    
print (get_new_words_with_blanks(guessed_indexes, "ascd"))

# print(remaining_life(guessed_indexes, 6))

# result = get_new_words_with_blanks([0,3], "abca")
# print(result)
