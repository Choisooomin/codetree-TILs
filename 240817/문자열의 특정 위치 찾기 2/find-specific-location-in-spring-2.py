arr = ["apple", "banana", "grape", "blueberry", "orange"]
cnt = 0
n = input()

for i in range(len(arr)):
	for j in range(len(arr)):
		if j==2 or j==3:
			if arr[i][j]==n:
				cnt+=1
				print(arr[i],end = '\n')
print(cnt)