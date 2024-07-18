import sys
input = sys.stdin.readline

def recur(value):
    if value > N:
        return 0
    
    if value == N:
        return 1
    
    ret = recur(value + 1)
    ret += recur(value + 2)
    ret += recur(value + 3)

    return ret

Q = int(input())
while Q:
    Q -= 1

    N = int(input())
    ans = recur(0)
    print(ans)