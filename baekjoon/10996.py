import sys
input = sys.stdin.readline

N = int(input())
Q = N

for i in range(2*N):
    for j in range(N):
        if i % 2 == 0:
            if j % 2 == 0:
                print("*", end="")
            else:
                print(" ", end="")
        else:
            if j % 2 == 1:
                print("*", end="")
            else:
                print(" ", end="")
    print()