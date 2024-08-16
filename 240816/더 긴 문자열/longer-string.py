string1,string2 = input().split()

n1 = len(string1)
n2 = len(string2)

if n1 > n2:
    print(string1,n1)
elif n1<n2:
    print(string2,n2)
else:
    print("same")