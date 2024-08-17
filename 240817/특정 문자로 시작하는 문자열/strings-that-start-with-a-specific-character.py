n = int(input())
arr = [input() for _ in range(n)]
a = input()
cnt = 0
avg = 0

for elem in arr:
    if elem[0] == a:
        cnt+=1
        avg += len(elem)

avg = avg / cnt
print(f"{cnt} {avg:.2f}")