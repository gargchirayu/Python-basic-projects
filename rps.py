import random

choices = ['Rock', 'Paper', 'Scissor']
pc_choice = random.choice(choices)
pc_score = 0
user_score = 0

while True:
    user_choice = input('Rock ! Paper ! Scissor! : ').capitalize()
    pc_choice = random.choice(choices)
    if user_choice == pc_choice:
        print('Tie')
    elif user_choice == 'Rock':
        if pc_choice == 'Paper':
            print('PC (', pc_choice, ') Wins')
            pc_score += 1
        else:
            print('PC (', pc_choice, ') Loses')
            user_score +=1
    elif user_choice == 'Paper':
        if pc_choice == 'Scissor':
            print('PC (', pc_choice, ') Wins')
            pc_score += 1
        else:
            print('PC (', pc_choice, ') Loses')
            user_score +=1
    elif user_choice == 'Scissor':
        if pc_choice == 'Rock':
            print('PC (', pc_choice, ') Wins')
            pc_score += 1
        else:
            print('PC (', pc_choice, ') Loses')
            user_score +=1
    print('User Score: ', user_score)
    print('PC Score: ', pc_score)
    if user_choice == 'End':
        break
if user_score > pc_score:
    print('\nUser Wins')
elif pc_score > user_score:
    print('\nPC Wins')
else:
    print('\nTied')

