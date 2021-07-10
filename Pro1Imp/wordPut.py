import random

with open('words.txt', encoding='UTF-8') as f:
    lines = f.readlines()
    no = 0
    while True:
        no = random.randint(0, len(lines)-1)
        line = lines[no].rstrip('\n')
        line_list = line.split('\u3000')
        bol = random.randint(0, 1)
        if bol == 0:
            print(line_list[0])
        else:
            print(line_list[1])
        c = input('你会吗')
        if c == 'y':
            continue
        else:
            print(line)
            print()


