import random


def create_card_number():

    BIN = "400000"
    Account_identifier = ""
    for i in range(9):
        Account_identifier = Account_identifier + str(random.randint(0, 9))
    Check_sum = "9"

    Card_num = BIN + Account_identifier + Check_sum

    return int(Card_num)


def create_card_pin():

    return random.randint(1000, 9999)

def create_an_account():

    print('Your card has been created.')

    print('Your card number is:')
    Card_number = create_card_number()
    print(Card_number)

    print('Your pin is: ')
    pin = create_card_pin()
    print(pin)

    return Card_number, pin


def log_in(card_num, pin):
    user_card_num = int(input('Enter card number: '))
    user_pin = int(input('Enter pin: '))

    if user_card_num == card_num and user_pin == pin:
        print('You have successfully logged in!')
        return True
    else:
        print('Wrong pin/card num combination.')
        return False


card_num = False
pin = False
logged_in = False

while True:

    if logged_in == False:
        print('1. Create an account')
        print('2. Log into account')
        print('0. Exit')
        user_choice = int(input('>'))

        if user_choice == 1:
            card_num, pin = create_an_account()
            continue

        elif user_choice == 2:
            logged_in = log_in(card_num, pin)
            continue

        elif user_choice == 0:
            exit()

    if logged_in == True:
        print('1. Balance')
        print('2. Log out')
        print('0. Exit')
        user_choice = int(input('>'))

        if user_choice == 1:
            print(0) # Create add balance function
            continue

        elif user_choice == 2:
            logged_in = False
            print('You have successfully logged out!')
            continue

        elif user_choice == 0:
            exit()


print('Goodbye!')
