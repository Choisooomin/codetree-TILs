str1 = input()
chr1 = input()
cnt=0

for i in range(len(str1)):
    if str1[i]==chr1:
        cnt+=1
print(cnt)