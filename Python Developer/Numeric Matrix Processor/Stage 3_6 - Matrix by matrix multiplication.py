# chose not to use numpy or array modules

def get_matrix_2d(r, c):
    m = list()
    for i in range(r):
        while True:
            m.append(input().split(' '))
            if len(m[-1]) != c:
                m.pop()
                print('Not the right amount of elements in that row, try again')
            else:
                break
    return m


def convert_matrix_int_2d(m):
    for row in range(len(m)):
        for column in range(len(m[row])):
            m[row][column] = float(m[row][column])
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
            row_sum.append(float(ma[r][j]) + float(mb[r][j]))

        matrix_sum.append(row_sum)
        row_sum = list()
    return matrix_sum


def multiply_matrix_integer_2d(m, c):

    for row in range(len(m)):
        for column in range(len(m[row])):
            m[row][column] = c * float(m[row][column])
    return m


def print_matrix_2d(m):
    for row in m:
        for i in range(len(row)):
            if i == len(row) - 1:
                print(row[i])
            else:
                print(row[i], end=' ')


def get_size_2d(prompt = ''):
    rows, columns = input(prompt).split(' ')
    rows, columns = int(rows), int(columns)
    return rows, columns


def multiply_matrix_matrix_2d(ma, mb):
    m = list()
    mrows = len(ma)
    mcols = len(mb[0])

    for i in range(mrows):
        col = list()
        for i in range(mcols):
            col.append(0)
        m.append(col)

    for i in range(mrows):
        for j in range(mcols):
            for k in range(len(mb)):
                m[i][j] += float(ma[i][k]) * float(mb[k][j])

    for i in range(len(ma)):
        for j in range(len(mb[0])):
            m[i][j] = round(m[i][j], 7)

    return m


def menu():
    return int(input('''1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
0. Exit'''))


if __name__ == '__main__':

    while True:

        choice = menu()

        if choice == 1:
            # add
            # rows, columns = get_size_2d('Enter size of matrices: ')
            # need to ask for size of both matrices to pass
            rowsa, columnsa = get_size_2d('Enter size of first matrix: ')
            print('Enter first matrix.')
            ma = get_matrix_2d(rowsa, columnsa)
            rowsb, columnsb = get_size_2d('Enter size of second matrix')
            print('Enter second matrix.')
            mb = get_matrix_2d(rowsb, columnsb)
            if rowsa != rowsb or columnsa != columnsb:
                print('The operation cannot be performed')
            else:
                add = add_matrix_2d(ma, mb)
                print('The result is:')
                print_matrix_2d(add)

        elif choice == 2:
            # multiply by constant
            rows, columns = get_size_2d('Enter size of matrix: ')
            print('Enter matrix.')
            ma = get_matrix_2d(rows, columns)
            c = int(input('Enter constant: '))
            multc = multiply_matrix_integer_2d(ma, c)
            if multc:
                print('The result is:')
                print_matrix_2d(multc)

        elif choice == 3:
            # multiply
            rows, columns = get_size_2d('Enter size of first matrix: ')
            print('Enter first matrix.')
            ma = get_matrix_2d(rows, columns)
            rows, columns = get_size_2d('Enter size of second matrix')
            print('Enter second matrix.')
            mb = get_matrix_2d(rows, columns)
            multm = multiply_matrix_matrix_2d(ma, mb)
            if multm:
                print('The result is:')
                print_matrix_2d(multm)

        elif choice == 0:
            exit()
