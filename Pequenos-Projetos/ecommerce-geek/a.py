a = {'a': 1, 'b': 2, 'c': 3}

with open('a.txt', 'w+') as f:
    for x, y in a.items():
        f.write(f'R${x}..........{y}\n')
