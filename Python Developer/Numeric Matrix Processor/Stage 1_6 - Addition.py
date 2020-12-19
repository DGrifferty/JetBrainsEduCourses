# chose not to use numpy or array modules

rows, columns = input().split(' ')
rows, columns = int(rows), int(columns)


def get_matrix_2d(r, c):
    m = list()
    for i in range(r):
        m.append(input().split(' '))
    return m


def convert_matrix_int_2d(m):
    for row in range(len(m)):
        for column in range(row):
            m[row][column] = int(m[row][column])

    return m


def add_matrix_2d(ma, mb):
    r = len(ma)
    if len(mb) != r:
        return print('ERROR')
    c = len(ma[0])
    for row in ma:
        if len(row) != c:
            return print('ERROR')
    for row in mb:
        if len(row) != c:
            return print('ERROR')
    row_sum = list()
    matrix_sum = list()
    for r, i in enumerate(ma):
        for j in range(len(i)):
            row_sum.append(int(ma[r][j]) + int(mb[r][j]))

        matrix_sum.append(row_sum)
        row_sum = list()
    return matrix_sum


ma = get_matrix_2d(rows, columns)
ma = convert_matrix_int_2d(ma)

rows, columns = input().split(' ')
rows, columns = int(rows), int(columns)

mb = get_matrix_2d(rows, columns)
mb = convert_matrix_int_2d(mb)

ADD = add_matrix_2d(ma, mb)
if ADD:
    for row in ADD:
        for i in range(len(row)):
            if i == len(row) - 1:
                print(row[i])
            else:
                print(row[i], end=' ')
