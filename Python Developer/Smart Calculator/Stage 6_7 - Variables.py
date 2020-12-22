variables = dict()
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

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
        # assigning new varible
        try:
            equ = i.split()
            equ = ''.join(equ)
            equ = equ.split('=')

            if len(equ) != 2:
                # if len(equ) > 3 or len(equ) <= 1:
                raise Exception('Invalid assignment')
                # if len(equ) == 3:
                #     if equ[1] != [' ,']:
                #         raise Exception('Invalid assignment')

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
            # elif equ[0] in variables.keys():
            #     raise Exception('Invalid identifier')
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
                # if element in variables.keys():
                #     equ[index] = variables[element]  # replace elements in equation with the correct
                #     # values, taking care of + mand minues

                for char in element:
                    if char in alphabet and element not in variables.keys():
                        raise Exception('Unknown variable')
                if element in variables.keys():
                    equ[index] = variables[element]




            if '-' in equ[0]:
                try:
                    sum = -float(equ[0][1:])
                except:
                    # try:
                    #
                    #
                    #     t = equ[0].split('-')
                    #
                    #
                    #     sum = float(t[0]) - float(t[1])
                    # except:
                        sum = -float(equ[0][:-1])

                    # try:
                    #     equ[1] = -equ[1]
                    # except:
                    #     pass

            elif '+' in equ[0]:

                try:
                    sum = float(equ[0][1:])

                except:
                    sum = float(equ[0][:-1])
            else:
                sum = float(equ[0])

            if len(equ) != 1:
                for index, char in enumerate(equ):
                    if '+' in char:
                        sum += float(equ[index + 1])
                    if '-' in char and index != 0:
                        if len(char) % 2 == 0:
                            sum += float(equ[index + 1])
                        else:
                            sum -= float(equ[index + 1])

            print(int(sum))

        except Exception as e:
            e = str(e)

            if e == 'Unknown variable':
                print('Unknown variable')
            else:
                print('Invalid Expression') 
