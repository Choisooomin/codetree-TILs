A = input()
B = input()
AB = "".join([A,B])
BA = "".join([B,A])

if AB == BA:
    print("true")
else:
    print("false")