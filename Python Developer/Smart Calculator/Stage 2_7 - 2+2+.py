while True:
    q = 0
    i = input()

    if i == "/exit":
        print('Bye!')
        exit()
    elif i == '':
        continue
    else:
        for num in i.split(' '):
            q += int(num)
        print(q)

