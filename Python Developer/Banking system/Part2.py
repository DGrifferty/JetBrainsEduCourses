import random


def create_card_number():
    bin = "400000"
    account_identifier = ""
    for i in range(9):
        account_identifier = account_identifier + str(random.randint(0, 9))

    check_sum = luhn_algorthm_generate(int(bin + account_identifier))


    return int(bin + account_identifier + check_sum)


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


def luhn_algorthm_generate(card_num: int) -> bool:
    """generates a card num to
    correspond with the luhn algorithm"""

    card_num_lst = [int(x) for x in str(card_num)]

    # Mutiplying odd digits by two
    for index, value in enumerate(card_num_lst):
        if index == 0 or index % 2 == 0:
            # print(index)
            card_num_lst[index] *= 2

        if card_num_lst[index] > 9:
            card_num_lst[index] -= 9

    if sum(card_num_lst) % 10 == 0:
        return str(0)
    else:
        return str(10 - sum(card_num_lst) % 10)


def luhn_algorthm_check(card_num: int) -> bool:
    """Checks that a user entered card num
    corresponds with the luhn algorithm"""

    card_num_lst = [int(x) for x in str(card_num)]
    last_digit = card_num_lst[-1]

    card_num_lst[-1] = 0
    # Mutiplying odd digits by two
    for index, value in enumerate(card_num_lst):
        if index == 0 or index % 2 == 0:
            card_num_lst[index] *= 2

        if card_num_lst[index] > 9:
            card_num_lst[index] -= 9

    if (sum(card_num_lst) + last_digit) % 10 == 0:
        return True

    else:
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
            # if luhn_algorthm_check(card_num):
            #     print('True')
            # else:
            #     print('False')

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
            print(0)  # Create add balance function
            continue

        elif user_choice == 2:
            logged_in = False
            print('You have successfully logged out!')
            continue

        elif user_choice == 0:
            exit()

print('Goodbye!')
