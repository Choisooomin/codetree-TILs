A = input()
result = 0

for elem in A:
    if (elem >= '0' and elem <= '9'):
        elem = int(elem)
        result += elem
print(result)