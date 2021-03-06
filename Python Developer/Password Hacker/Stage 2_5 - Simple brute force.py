import sys, socket

def split(string):
    return [char for char in string]

def pass_gen(prev_pass):
    char_set = 'abcdefghijklmnopqrstuvwxyz0123456789'
    if prev_pass == None:
        return 'a'
    prev_pass = [char for char in prev_pass[::-1]]

    if prev_pass[0] != '9':
        prev_pass[0] = char_set[char_set.index(prev_pass[0]) + 1]
        return ''.join(prev_pass[::-1])
    elif all(char in '9' for char in prev_pass):
        prev_pass = ['a'] * (len(prev_pass) + 1)

    else:
        if '9' in prev_pass:
            for index, char in enumerate(prev_pass):
                if char == '9':
                    prev_pass[index] = 'a'
                    continue
                else:
                    prev_pass[index] = char_set[char_set.index(char) + 1]
                    break
        else:
            prev_pass[1] = char_set[char_set.index(prev_pass[1]) + 1]
    return ''.join(prev_pass[::-1])



password = None
data = 'Wrong password!'
args = sys.argv
if len(args) > 2:
    ip = args[1]
    port = int(args[2])

with socket.socket() as s:
    s.connect((ip, port))
    while data == 'Wrong password!':
        password = pass_gen(password).encode()
        s.send(password)
        data = s.recv(1024)
        data = data.decode()
        password = password.decode()


print(password)
