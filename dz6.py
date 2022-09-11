n = int(input())
for i in range(-1, n+1):
    for _ in range(0, n-i):
        print(_, end= ' ')
    print() 