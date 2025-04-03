H, M = map(int, input().split())

if 45<=M<=60:
    print(H, M-45)

elif H>0 and 45<=M<60:
    print(H, M-45)

elif H>0 and 0<=M<45:
    print(H-1, M+15)

else:
    print(int(23), M+15)
