n = int(input())
arr = [input()for _ in range(n)]
tot_str = ""

for target_str in arr:
    tot_str += target_str
print(tot_str)