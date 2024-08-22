a,b = tuple(input().split())
idx1 = 0
idx2 = 0

for elem in a:
    if (elem >= '0' and elem <= '9'):
        idx1 += 1
    else:
        break

for elem in b:
    if (elem >= '0' and elem <= '9'):
        idx2 += 1
    else:
        break
str1 = a[:idx1]
str2 = b[:idx2]
	
# 합쳐진 문자열을 숫자로 바꿉니다.
str1 = int(str1)
str2 = int(str2)

# 두 숫자의 합을 출력합니다.
print(str1 + str2)