import random

words = ['website', 'python', 'machine', 'learning', 'computer', 'vision', 'ethical', 'hacking', 'internet', 'things']
word = random.choice(words)
guesses = ""
turns = 10
while turns > 0:
    guess = input('\nGuess the character: ')
    guesses += guess
    flag = 0
    # flag used to keep an account that last entry was valid and later to break loop when word found
    # cant use word == guesses to break loop because wrong char guesses would also be present
    for text in word:
        if text in guesses:
            print(text, end=" ")
        else:
            print('_', end=" ")
            flag = 1
    if flag == 0:
        print('\nYou win. The word is ', word)
        break
    if guess not in word:
        turns -= 1
        print('\nWrong. You have ', turns, 'chance(s) left')
        if turns == 0:
            print('\nYou lose')



