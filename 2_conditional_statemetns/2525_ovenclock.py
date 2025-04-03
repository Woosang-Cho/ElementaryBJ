H, M = input().split()
T = int(input())

M=int(M)
H=int(H)

if 60<M+T:
    print()
elif 0<=M+T<=60:
    print(H, M+T)
