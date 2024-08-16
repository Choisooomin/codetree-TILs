str1 = input()
str2 = input()
str3 = input()

n1 = len(str1)
n2 = len(str2)
n3 = len(str3)

if n1 > n2:
    if n1 > n3:
        if n2 > n3:
            print(n1 - n3)
        else:
            print(n1 - n2)
    else:
        print(n3 - n2)
else:
    if n1 > n3:
        print(n2-n3)
    else:
        if n2 > n3:
            print(n2 -n1)
        else:
            print(n3 - n1)