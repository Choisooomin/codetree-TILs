while True:
    n = input()
    if n == 'END':
        break
    leng = len(n)

    for i in range(leng-1, -1, -1):
        print(n[i],end='')
    print()