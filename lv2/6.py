A, B = map(int, input().split())
C = int(input())

if( B + C >= 60 ):
    A = A + int((B + C) / 60)
    if(A >= 24):
        A = A - 24
        B = (B + C) % 60
        print(A, B)
    else:
        B = (B + C) % 60
        print(A, B)
else:
    B = B + C
    print(A, B)