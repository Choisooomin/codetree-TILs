s = input()
index = s.find('e')
arr = list(s)
arr.pop(index)
s = ''.join(arr)
print(s)