def is_negative():
    pass

def define_variable():
    pass


def solve():
    pass


def bracket_scan(equ):
    count = 0
    solved = False

    for open_index, ch in enumerate(equ):
        if ch == '(':
            if solved == True:
                break
            for closed_index, ch2 in enumerate(equ[open_index + 1:]):
                if ch2 == '(':
                    count += 1
                if ch2 == ')':
                    if count == 0:
                        equ[open_index:closed_index + 2] = [solver(equ[open_index + 1:closed_index + 1])]
                        return equ
                        if '(' not in equ:
                            solved = True
                        break
                    else:
                        count -= 1
                else:
                    if count != 0 and closed_index == len(equ) - 1:
                        raise Exception('Unequal brackets')

    return equ

def check_input(user_input, variables):
    '''Checks input by converting every element in the equation to a
    character and then looking at the sequence of characters'''
    numbers = '0123456789'
    equ = user_input.split()
    conv_equ = []
    symbols = '^*+-/'

    for element in equ:
        contains_number = False
        contains_letter = False
        
        print(f'{element} element')

        if element in variables.keys():
            conv_equ.append('av')
        elif element == '(':
            conv_equ.append('(')
        elif element == ')':
            conv_equ.append(')')
        elif element == '=':
            conv_equ.append('=')
        elif element in symbols:
            conv_equ.append('s')
        else:
            for char in element:
                print(f'{char}, char}')
                if char in numbers:
                    contains_number = True
                    if contains_letter:
                        conv_equ.append('bav')
                        break
                elif char in alphabet:
                    contains_letter = True
                    if contains_number:
                        conv_equ.append('bav')
                        break
                elif char in '+-':
                    if contains_letter or contains_number:
                        E = 'bad element - +- in middle of element'
                else:
                    E = 'bad element - unallowed element/ character'

            if contains_number:
                conv_equ.append('n')
            else:
                conv_equ.append('uav')

        if '=' in conv_equ:

            # Errors - bad variable name left
            # Bad equation right -  bad assignment
            # More than one =
            allowed_combs = [['uav', '=', 'n'], ['uav', '=', 'av']]
            if conv_equ not in allowed_combs:
                print(conv_equ)
                if 'bav' == equ[0]:
                    E = 'Invalid identifier'
                elif 'bav' == equ[2]:
                    E = 'Invalid assignment'
                else:
                    E = 'Invalid assignment'
                return False, E

            else:
                print(conv_equ)
                return True, None






    print(conv_equ)


if __name__ == '__main__':

    variables = dict()
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '1234567890'

    while True:

        user_input = input()

        if user_input == '':
            continue

        elif user_input[0] == '/':
            if user_input == "/exit":
                print('Bye!')
                exit()
            elif user_input == '/help':
                print('This program will calculate the sum of a user'
                      'enter list of numbers separated by spaces.\n'
                      'It can calculate equations containing +, -, *, / (), ^ only. \n'
                      'You can assign variables using = to use in later question')
                continue
            else:
                print('Unknown command')
                continue

        print(check_input(user_input, variables))

