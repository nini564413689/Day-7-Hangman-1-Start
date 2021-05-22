#Step 1 
import random
words= ["aardvark", "baboon", "camel"]
# words = ["straight", "collection", "ferocious", "sheer","humidity", "explicit","ravage", "wreck","impede", "immune"]
words_picked = str (random.choice(words))
print (words_picked)
# functions below----------------------------------------|
def result(): # check if the letter is correct
    tip1 = " ".join(blank)
    print (tip1)

# def guess_step():    
#     guess = input ("Please guess a letter:\n").lower()
#     blank2 = blank # copy a previous result
#     for letter in range (len(words_picked)):
#         if words_picked [letter] == guess:
#             blank [letter] = guess
# functions above-----------------------------------------|

blank = []
for b in range (len(words_picked)):
    blank += "_"
result() # show at the begining as a tip of word length
# game start from here---------------------

lives = 6
while list (words_picked) != blank and lives > 0:
    guess = input ("Please guess a letter:\n").lower()
    for letter in range (len(words_picked)):
        if words_picked [letter] == guess:
            blank [letter] = guess
    result() # show if the inputted word is correct
    if  guess not in list (words_picked):
        lives -= 1
        if lives == 5:
            print ('''
      _______
     |/      |
     |      (_)
     |      
     |       
     |      
     |
    _|___
    ''' )
        elif lives == 4:
            print ('''
      _______
     |/      |
     |      (_)
     |       | 
     |       |
     |       
     |
    _|___''')
        elif lives == 3:
            print ('''
      _______
     |/      |
     |      (_)
     |      \|
     |       |
     |      
     |
    _|___''')
        elif lives == 2:
            print ('''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
    _|___''')       
        elif lives == 1:
            print ('''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
    _|___''')
        else:
            print ('''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \  
     |
    _|___ You lose....''')
if list (words_picked) == blank and lives > 0:
    print ("You win!!!")

