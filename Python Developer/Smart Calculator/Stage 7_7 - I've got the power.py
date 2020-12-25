from typing import List
variables = dict()
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '1234567890'

def calc(sum, equ, index):
    if '+' in char:
        sum += float(equ[index + 1])
    if '-' in char and index != 0:
        if len(char) % 2 == 0:
            sum += float(equ[index + 1])
        else:
            sum -= float(equ[index + 1])
    if '*' in char:
        sum += float(equ[index + 1])
    if '/' in char:
        sum /= float(equ[index + 1])
    return sum

def is_negative(equ: List, index: int) -> bool:
    if '-' not in str(equ[index]):
        return False
    else:
        for i, char in enumerate(str(equ[index])):
            if char != '-':
                if (i) % 2 == 0:
                    return False
                else:
                    return True

def mult_divide_scan()
    should be a function used in calc
    if * or / found mult/divide ones next to each other, retun
    answers and +/-'s unreplaced to calc'

def bracket_scan():
    count = int
    index_of_open, index_of_closed = [], []

    for index, char in equ:
        if char == '(':
            index_of_open.append(index)



    if count of open inside > 1
        find more than one close
    if bracket closed found send to calc
        doing internal things first,
send results and indices to replace to priority
    return result and indicies to replace


# def priority():
#     b, d, m, a, s = [], [], [], [], []
#     open_brackets, closed_brackets = []
#     for i, char in enumerate(equ):
#         if char == '(':
#             bracket_scan(equ, i)
#
#             get bracket indices send to calculate function
#             send next bracket with the previous bracket replaced by its result

def convert(equ):
    symbols = '()*/+-='
    for index, char in enumerate(equ):
        if char not in symbols:
            equ[index] = float(char)


def solver(equ):
    solved = False
    while not solved:
            if '(' in equ:
                # send to bracket scanner
                # bracket scanner then sends the primary bracket back
                # and this returns the answer to replace that bracket with
            if '*' in equ:
                i = equ.index('*')
                equ[i-1, i + 1] = equ[i-1] * equ[i+1]
                continue
            elif '/' in equ:
                i = equ.index('/')
                equ[i-1, i + 1] = equ[i-1] / equ[i+1]
            elif '+' in equ:
                i = equ.index('+')
                equ[i-1, i + 1] = equ[i-1] + equ[i+1]
            elif '-' in equ:
                i = equ.index('-')
                equ[i-1, i + 1] = equ[i-1] + equ[i+1]
            else:
                return equ[0]





def define_variable():



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
                  'It can calculate equations containing plus and minus only.')
            continue
        else:
            print('Unknown command')
            continue
    if '=' in i:
        try:
            equ = i.split()
            equ = ''.join(equ)
            equ = equ.split('=')

            if len(equ) != 2:
                raise Exception('Invalid assignment')

            clean = True

            for char in equ[0]:
                if char.lower() not in alphabet:
                    clean = False
                    break
            for char in equ[-1]:
                if char in alphabet:
                    if equ[-1] not in variables.keys():
                        raise Exception('Invalid assignment')

            if not clean:
                raise Exception('Invalid identifier')
            else:
                if equ[-1] in variables.keys():
                    variables[equ[0]] = variables[equ[-1]]
                else:
                    variables[equ[0]] = equ[-1]


        except ValueError:
            print('Invalid assignment')
        except Exception as e:
            print(e)

    else:

        try:
            equ = i.split()

            for index, element in enumerate(equ):

                for char in element:
                    if char in alphabet and element not in variables.keys():
                        raise Exception('Unknown variable')
                if element in variables.keys():
                    equ[index] = variables[element]

            if '-' in equ[0]:
                try:
                    sum = -float(equ[0][1:])
                except:
                        sum = -float(equ[0][:-1])

            elif '+' in equ[0]:

                try:
                    sum = float(equ[0][1:])

                except:
                    sum = float(equ[0][:-1])
            else:
                sum = float(equ[0])

            if len(equ) != 1:
                for index, char in enumerate(equ):
                    sum = calc(sum, equ, index)
                    if '(' in char:
                        pass


            print(int(sum))

        except Exception as e:
            e = str(e)

            if e == 'Unknown variable':
                print('Unknown variable')
            else:
                print('Invalid Expression')

