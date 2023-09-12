A, B, C = map(int, input().split())

D = [A, B, C]

D.sort()

if(D[0] == D[2]):
    print(10000 + D[0] * 1000)
elif(D[0] == D[1] or D[1] == D[2]):
    print(1000 + D[1] * 100)
else:
    print(D[2] * 100)