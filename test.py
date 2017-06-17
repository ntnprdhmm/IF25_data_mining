length = 10

for i in range(length):
    for j in range(i, length):
        if i != j:
            print('%d %d' % (i, j))
