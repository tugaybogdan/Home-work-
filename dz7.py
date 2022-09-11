n =int(input())
line = 1 
i = 1 
while i < n:
    for _ in range(line):
        print(i, end=' ')
        i += 1
        if i>= n:break
    line += 2
    print() 