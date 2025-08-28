import random

emoji = {'r': '🪨', 's': '✂️', 'p': '📃'}
choices = ('r', 'p', 's')

while True:
    user_choice = input("Rock , Paper, Scissors ? (r/p/s) : ").lower()
    if user_choice not in choices:
        print("Invalid Choice! ")
        continue

    computer_choice = random.choice(choices) 

    print(f'You Choice {emoji[user_choice]}' )
    print(f'Computer Choice {emoji[computer_choice]}' )

    if user_choice == computer_choice:
        print('Tie!')
    elif (
        (user_choice == 'r' and computer_choice == 's') or 
        (user_choice == 's' and computer_choice == 'p') or 
        (user_choice == 'p' and computer_choice == 'r')):
        print('You Win')
    else :
        print('You Lose')

        should_continue = input('Continue? (y/n) : ').lower()
        if should_continue == 'n': 
            break