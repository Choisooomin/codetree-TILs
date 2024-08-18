s = input()
leng = len(s)
arr = list(s)

while leng>1:
    n = int(input())
    if n >= leng:
        n = leng - 1
    arr.pop(n)
    leng-=1

    s = ''.join(arr)
    print(s)