string, q_num = input().split()
q_num = int(q_num)

# 문자열의 길이를 구합니다.
str_size = len(string)

# q개의 질의를 수행합니다.
for i in range(q_num):
	# 요청을 입력받습니다.
	q_type = int(input())

	if q_type == 1:
		# 문자열을 왼쪽으로 한 칸 쉬프트하고 문자열을 출력합니다.
		string = string[1:] + string[0]
		print(string)

	elif q_type == 2:
		# 문자열을 오른쪽으로 한 칸 쉬프트하고 문자열을 출력합니다.
		string = string[-1] + string[:-1]
		print(string)
		
	else:
		# 문자열을 좌우로 뒤집고 문자열을 출력합니다.
		string = string[::-1]
		print(string)