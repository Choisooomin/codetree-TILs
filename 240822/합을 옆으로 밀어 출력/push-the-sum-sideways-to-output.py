n = int(input())
result = 0
for _ in range(n):
    elem = int(input())
    result += elem

result = str(result)
result = result[1:]+result[0]
print(result)