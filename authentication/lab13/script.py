print("[", end='')
with open('password.txt', 'r')as f:
    for line in f.readlines():
        print('"' + line.strip() + '",', end='')
