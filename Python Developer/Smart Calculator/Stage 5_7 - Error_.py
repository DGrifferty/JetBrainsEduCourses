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
