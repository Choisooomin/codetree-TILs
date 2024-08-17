n = int(input())
arr = input().split()
tot_str = ""

for i in range(n):
    tot_str += arr[i]

leng = len(tot_str)

for i in range(leng):
    print(tot_str[i],end='')
    if(i+1)%5 == 0:
        print()