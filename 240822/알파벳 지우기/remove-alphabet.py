a = input()
b = input()
# 각 문자열에서 숫자 부분을 추출하여 이어붙이기
str1 = ''.join([elem for elem in a if elem.isdigit()])
str2 = ''.join([elem for elem in b if elem.isdigit()])

# 숫자로 변환
num1 = int(str1)
num2 = int(str2)

# 두 수의 합 구하기
result = num1 + num2

print(result)