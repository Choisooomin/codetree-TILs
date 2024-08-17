s = input()
arr1 = list(s)
arr2 = list(s)
for i in range(len(arr2)):
    if arr2[i] == arr1[0]:
        arr2[i] = arr1[1]
    elif arr2[i] == arr1[1]:
        arr2[i] = arr1[0]
s = ''.join(arr2)
print(s)