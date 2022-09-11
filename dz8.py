n =int(input())
line = 1 
i = 1 
while i < n:
    s = ''
    for _ in range(line):
        s = str(i) + " " + s
        i += 1
        if i>= n:break
    print(s)
    line += 1
    