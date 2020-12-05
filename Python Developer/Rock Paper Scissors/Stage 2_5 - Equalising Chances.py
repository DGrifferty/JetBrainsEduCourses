import random


def winner(user, comp):
    draw = False

    if comp == user:
        print(f'There is a draw ({comp})')
        draw = True

    if not draw:

        if comp == 'rock':
            if user == 'paper':
                print(f'Well done the computer chose {comp} and failed')
            else:
                print(f'Sorry but the computer chose {comp}')

        elif comp == 'scissors':
            if user == 'rock':
                print(f'Well done the computer chose {comp} and failed')
            else:
                print(f'Sorry but the computer chose {comp}')

        elif comp == 'paper':
            if user == 'scissors':
                print(f'Well done the computer chose {comp} and failed')
            else:
                print(f'Sorry but the computer chose {comp}')


choices = ['rock', 'paper', 'scissors']

while True:
    user_choice = input()
    if user_choice.lower() in choices:
        user_choice = user_choice.lower()
        break

comp_choice = random.choice(choices)

winner(user_choice, comp_choice)
