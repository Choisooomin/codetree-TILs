a = input()
for elem in a:
    if(elem >= 'A' and elem <= 'Z') or (elem >= 'a' and elem <= 'z'):
        print(elem.upper(), end='')