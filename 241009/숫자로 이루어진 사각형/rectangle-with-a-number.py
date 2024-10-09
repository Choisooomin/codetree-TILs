def print_num(n):
    num = 1
    for _ in range(n):
        for _ in range(n):
            print(num,end=" ")
            num = (num % 9) + 1
        print()

n = int(input())
print_num(n)