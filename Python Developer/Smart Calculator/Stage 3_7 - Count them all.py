while True:
    q = 0
    i = input()

    if i == "/exit":
        print('Bye!')
        exit()
    elif i =='/help':
        print('This program will calculate the sum of a user'
              'enter list of numbers separated by spaces.')
    elif i == '':
        continue
    else:
        for num in i.split(' '):
            q += int(num)
        print(q)
