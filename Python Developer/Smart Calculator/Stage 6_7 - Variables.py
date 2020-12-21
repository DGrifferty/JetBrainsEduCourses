variables = dict()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

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
        else:
            print('Unknown command')
    if '=' in i:
        # assigning new varible
        try:
            equ = i.split()
            equ = ''.join(equ)
            equ = equ.split('=')
            print(equ)

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

            if not clean:
                raise Exception('Invalid identifier')
            elif equ[0] in variables.keys():
                raise Exception('Invalid identifier')
            else:
                variables[equ[0]] = float(equ[-1])

        except ValueError:
            print('Invalid assignment')
        except Exception as e:
            print(e)

    else:

        try:
            equ = i.split()
            if '-' in equ[0]:
                # try:
                sum = -float(equ[0][1:])
                # except:
                #     sum = float(equ[0][:-1])

            elif '+' in equ[0]:

                sum = float(equ[0][1:])
                # except:
                #     sum = float(equ[0][:-1])

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


        except:
            print('Invalid Expression')
