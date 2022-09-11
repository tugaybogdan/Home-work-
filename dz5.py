n = int(input())
for i in range(1, n+1):
    for _ in range(i, 0, -1):
        print(_, end= ' ')
    print() 