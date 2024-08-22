string = input()
for elem in string:
    if (elem >= 'A' and elem <= 'Z'):
        print(elem.lower(),end='')
    if (elem >= 'a' and elem <= 'z'):
        print(elem.upper(),end='')