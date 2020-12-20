while True:
    q = 0
    i = input()

    if i == "/exit":
        print('Bye!')
        exit()
    elif i == '/help':
        print('This program will calculate the sum of a user'
              'enter list of numbers separated by spaces.')
    elif i == '':
        continue
    else:
        equ = i.split()

        if '-' in equ[0]:
            sum = -float(equ[0][1:])
        else:
            sum = float(equ[0])

        for index, char in enumerate(equ):
            if '+' in char:
                sum += float(equ[index + 1])
            if '-' in char and index != 0:
                if len(char) % 2 == 0:
                    sum += float(equ[index + 1])
                else:
                    sum -= float(equ[index + 1])

        print(int(sum))
