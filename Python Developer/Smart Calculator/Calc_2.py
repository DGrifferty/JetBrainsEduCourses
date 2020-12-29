def conv_to_float(equ):


def define_variable(user_input, variables):

    equ = user_input.split()
    equ = ''.join(equ)
    equ = equ.split('=')

    if equ[-1] in variables.keys():
        equ[-1] = variables[equ[0]]
    variables[equ[0]] = equ[-1]

    return variables


def solve(input, variables):
    pass


def replace_variables(user_input):

    equ = user_input.split()

    # could use conv_equ to save computation time

    for index, element in enumerate(equ):
        if element in variables.keys():
            equ[index] = variables[equ[index]]

    return equ


def bracket_scan(equ):
    #TODO: legacy code - Check
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
    character and then looking at the sequence of characters
    returns True and none if input is good, or false and E if it is bad,
    E will be a string and state the issue'''

    equ = user_input.split()
    conv_equ = []
    symbols = '^*+-/'
    # negative_check_indices = []
    # av = assigned variable
    # bv = bad variable - letters and numbers
    # uav = unassigned variable (just letters)
    # n = number
    # s = symbol (not brackets or =)

    for p, element in enumerate(equ):
        contains_number = False
        contains_letter = False

        print(f'{element} element')

        # if '-' in element:
        #     negative_check_indices.append(p)

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
            for index, char in enumerate(element):
                print(f'{char}, char')
                if char in numbers:
                    contains_number = True
                    if contains_letter:
                        conv_equ.append('bv')
                        break
                elif char in alphabet:
                    contains_letter = True
                    if contains_number:
                        conv_equ.append('bv')
                        break
                elif char in '+-':
                    if index == 0:
                        continue
                    elif element[index - 1] in '+-':
                        continue
                    else:
                        E = 'bad element - +- in middle of element'
                        return False, E
                else:
                    E = 'bad element - not allowed element/ character'
                    return False, E

            if contains_number:
                conv_equ.append('n')
            else:
                conv_equ.append('uav')

    if 'bv' in conv_equ:
        E = 'Bv used'
        return False, E

    if '=' in conv_equ:

        # Errors - bad variable name left
        # Bad equation right -  bad assignment
        # More than one =
        allowed_combs = [['uav', '=', 'n'], ['uav', '=', 'av']]
        if conv_equ not in allowed_combs:
            if 'bv' == equ[0]:
                E = 'Invalid identifier'
            elif 'bv' == equ[2]:
                E = 'Invalid assignment'
            else:
                E = 'Invalid assignment'
            return False, E

        elif 'av' not in conv_equ:
            return True, 'Assignment'
        else:
            return True, 'Assignment', True

    if 'uav' in conv_equ:
        E = 'Unassigned variable used'
        return False, E

    if conv_equ.count('(') != conv_equ.count(')'):
        if conv_equ.count('(') >= conv_equ.count(')'):
            E = 'More opening brackets than closing brackets'
        else:
            E = 'More closing brackets than opening brackets'
        return False, E

    open_count = 0

    for index, element in enumerate(conv_equ):
        # Here element can equal (, ), s, n, av
        if element == 'n':
            if index != len(conv_equ) - 1:
                if conv_equ[index + 1] not in 's)':  # right
                    E = 'Bad symbol to right of number'
                    return False, E
            if index != 0:
                if conv_equ[index - 1] not in '(s':  # left
                    E = 'Bad symbol to left of number'
                    return False, E
        elif element == 's':
            if index == 0:
                E = 'Symbol at start of equation'
                return False, E
            if index == len(conv_equ) - 1:
                E = 'Symbol at end of equation'
                return False, E
            if conv_equ[index + 1] not in '(nav':  # right
                E = 'Bad symbol to right of symbol'
                return False, E
            if conv_equ[index - 1] not in ')nav':  # left
                E = 'Bad symbol to left of symbol'
                return False, E

        elif element == 'av':
            if conv_equ[index + 1] not in 's':  # right
                E = 'Bad symbol to right of number'
                return False, E
            if index != 0:
                if conv_equ[index - 1] not in 's':  # left
                    E = 'Bad symbol to left of number'
                    return False, E

        elif element == '(':
            open_count += 1
            # count brackets opening and closed with integers if closed, minus from open, if it goes negative close before open
            # if they are not zero at the end, bad count!
            if index == len(conv_equ) - 1:
                E = 'Opening bracket at end of equation'
                return False, E
            if conv_equ[index + 1] not in 'nav':  # right
                E = ' Bad right of opening bracket'
                return False, E
            if index != 0:
                if conv_equ[index - 1] not in 's':
                    E = 'Bad left of opening bracket'
                    return False, E

        elif element == ')':
            open_count -= 1
            if open_count < 0:
                E = 'Closed bracket before open bracket'
                return False, E
            if index != len(conv_equ) - 1:
                if conv_equ[index + 1] not in 's)':  # right
                    E = ' Bad right of closing bracket'
                    return False, E
            if index != 0:
                if conv_equ[index - 1] not in ')nav':
                    E = 'Bad left of closing bracket'
                    return False, E

    if 'av' not in conv_equ:
        return True, 'Calculation'
    else:
        return True, 'Calculation', True

    # TODO: if [n (] insert * or if )(
    # TODO: Make check input tell whether av's have been used, so they can be replaced
    #


if __name__ == '__main__':

    variables = dict()
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '1234567890'

    while True:

        user_input = input()
        av_used = False

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

        tup = check_input(user_input, variables)

        if len(tup) == 2:
            check, type = tup
        else:
            check, type, av_used = tup

        if check == False:
            print(type)
        else:
            if type == 'Assignment':
                define_variable(user_input)
            elif type == 'Calculation':
                if av_used:
                    equ = replace_variables(input, variables)
                    conv_to_float(equ)
                    solve(equ)
                else:
                    equ = user_input.split()
                    solve(equ)


