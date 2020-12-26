from typing import List

variables = dict()
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '1234567890'


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


def convert(equ, variables):
    symbols = '()*/+-=^'
    breaks = False
    for index, element in enumerate(equ):
        if element not in symbols:
            for char in element:
                if char in alphabet:
                    if element not in variables.keys():
                        print('Unknown variable')
                        breaks = True
                        break
            if breaks == False:
                equ[index] = is_negative(equ, index, variables)
            else:
                break
    return equ, breaks


def is_negative(equ: List, index: int, variables) -> float:
    plus_count = 0
    if '-' not in str(equ[index]) and '+' not in str(equ[index]):
        if str(equ[index]) not in variables.keys():
            return float(equ[index])
        else:
            return float(variables[str(equ[index])])
    else:
        for i, element in enumerate(str(equ[index])):
            minus_count = 0
            for index, char in enumerate(element):
                if char in '1234567890':
                    break
                elif len(element) == 0 and element not in variables.keys():
                    return element
                else:
                    if element == '-':
                        minus_count += 1
                    elif element == '+':
                        pass
                    if index + 1 == len(element):
                        if minus_count % 2 == 0:
                            return '+'
                        else:
                            return '-'

            if element != '-':
                if element == '+':
                    plus_count += 1
                    continue
                elif int(i - plus_count) % 2 == 0:
                    if str(equ[index])[i:] in variables.keys():
                        print('yes')
                        return float(variables[str(equ[index])[i:]])
                    else:
                        return float(-str(equ[index])[i:])
                else:
                    if str(equ[index])[i:] in variables.keys():
                        return float(-variables[str(equ[index])[i:]])
                    else:
                        return float(-str(equ[index])[i:])


def solver(equ):
    while True:
        if '(' in equ:
            equ = bracket_scan(equ)
            continue
        elif '^' in equ and '(' not in equ:
            i = equ.index('^')
            q = equ[i - 1]
            for p in range(int(equ[i + 1]) - 1):
                equ[i - 1] *= q
            equ[i - 1:i + 2] = [equ[i - 1]]
            continue

        elif '/' in equ and '(' not in equ:
            i = equ.index('/')
            equ[i - 1:i + 2] = [equ[i - 1] / equ[i + 1]]
            continue
        elif '*' in equ and '(' not in equ:
            i = equ.index('*')
            equ[i - 1:i + 2] = [equ[i - 1] * equ[i + 1]]
            continue
        elif '+' in equ and '(' not in equ:
            i = equ.index('+')
            if equ[i-2] =='-':
                equ[i - 1:i + 2] = [equ[i - 1] - equ[i + 1]]
            else:
                equ[i - 1:i + 2] = [equ[i - 1] + equ[i + 1]]
                continue
        elif '-' in equ and '(' not in equ:
            i = equ.index('-')
            equ[i - 1:i + 2] = [equ[i - 1] - equ[i + 1]]
            continue
        elif len(equ) == 1:
            return int(equ[0])
        else:
            continue


def define_variable(i, variables):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    try:
        equ = i.split()
        equ = ''.join(equ)
        equ = equ.split('=')

        if len(equ) != 2:
            raise Exception('Invalid assignment')

        for char in equ[0]:
            if char.lower() not in alphabet:
                raise Exception('Invalid identifier')

        for char in equ[-1]:
            if char in alphabet:
                if equ[-1] not in variables.keys():
                    raise Exception('Invalid assignment')
                else:
                    variables[equ[0]] = variables[equ[-1]]
                    return variables

        variables[equ[0]] = equ[-1]

        return variables

    except ValueError:
        print('Invalid assignment')
    except Exception as e:
        e = str(e)
        if e == 'Invalid assignment':
            print('Invalid assignment')
        elif e == 'Invalid identifier':
            print('Invalid identifier')
        elif e == 'Unknown variable':
            print('Unknown variable')

while True:

    i = input()

    if i == '':
        continue

    elif i[0] == '/':
        if i == "/exit":
            print('Bye!')
            exit()
        elif i == '/help':
            print('This program will calculate the sum of a user'
                  'enter list of numbers separated by spaces.\n'
                  'It can calculate equations containing +, -, *, / (), ^ only. \n'
                  'You can assign variables using = to use in later question')
            continue
        else:
            print('Unknown command')
            continue
    if '=' in i:
        variables = define_variable(i, variables)

    else:

        equ = i.split()
        equ, breaks= convert(equ, variables)
        if breaks == False:
            print(solver(equ))
        else:
            continue

        #
        # except Exception as e:
        #     e = str(e)
        #
        #     if e == 'Unknown variable':
        #         print('Unknown variable')
        #     else:
        #         print('Invalid Expression')
