# chose not to use numpy or array modules

rows, columns = input('Enter the number of rows and columns in the matrices you want to add').split(' ')
rows, columns = int(rows), int(columns)
print(rows, columns)


def get_matrix_2d(r, c):
    m = list()
    for i in range(r):
        while True:
            m.append(input(f'Enter row {i+1}').split(' '))
            if len(m[-1]) != c:
                m.pop()
                print('Please enter the correct number of columns!')
            else:
                break
    return m

def convert_matrix_int_2d(m):
    for row in range(len(m)):
        for column in range(row):
            m[row][column] = int(m[row][column])

    return m

def add_matrix_2d(ma, mb):
    r = len(ma)
    if len(mb) != r:
        return print('The matrices should have the same number of rows')
    c = len(ma[0])
    for row in ma:
        if len(row) != c:
            return print('The rows should all be the same length')
    for row in mb:
        if len(row) != c:
            return print('The rows should all be the same length')
    row_sum = list()
    matrix_sum = list()
    for r, i in enumerate(ma):
        for j in range(len(i)):
            row_sum.append(int(ma[r][j]) + int(mb[r][j]))

        matrix_sum.append(row_sum)
        row_sum = list()


    return matrix_sum


print('Enter matrix a')

ma = get_matrix_2d(rows, columns)
ma = convert_matrix_int_2d(ma)
print(ma)

print('Enter matrix b')

mb = get_matrix_2d(rows, columns)
mb = convert_matrix_int_2d(mb)
print(mb)

print(add_matrix_2d(ma, mb))
