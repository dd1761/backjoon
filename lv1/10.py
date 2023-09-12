A = int(input())
B = int(input())

C = list(map(int, str(B)))

print(A * C[2])
print(A * C[1])
print(A * C[0])
print(A * B)