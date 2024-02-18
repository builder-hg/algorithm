# 5
import sys
input = sys.stdin.readline

K = int(input())

if K == 0:
    print(0)
    sys.exit()

if K == 1:
    print(1)
    sys.exit()

def recur(prev2, prev1, cur):
    # 기저조건
    if cur == K:
        print(prev2 + prev1)
        return
    
    recur(prev1, prev2 + prev1, cur + 1)

recur(0, 1, 2)