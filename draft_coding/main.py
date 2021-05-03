A = [0,1,2,3,4,5]
B = []
C =[]
for i in range(0, len(A)):
    if i % 2 == 0:
        B.append(int(1))
        C.append(int(0))
    if i % 2 == 1:
        B.append(int(0))
        C.append(int(1))

print(B)
print(C)