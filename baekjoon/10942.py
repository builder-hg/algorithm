import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def recur(s, e):
    if arr[s] != arr[e]:
        return 0
    
    if s == e or s + 1 == e:
        return 1
    
    if dp[s][e] != -1:
        return dp[s][e]
    
    ret = recur(s + 1, e - 1)

    dp[s][e] = ret

    return dp[s][e]

N = int(input())
arr = list(map(int, input().split()))
dp = [[-1 for _ in range(N)] for _ in range(N)]
M = int(input())
for _ in range(M):
    xs, xe = map(int, input().split())
    ans = recur(xs - 1, xe - 1)
    print(ans)



'''
import sys
input = sys.stdin.readline

def recur(s, e):
    global ans

    if arr[s] != arr[e]:
        ans = 0
        return 
    
    if s == e or s + 1 == e:
        ans = 1
        return 
    
    recur(s + 1, e - 1)

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
for _ in range(M):
    xs, xe = map(int, input().split())
    ans = 0
    recur(xs - 1, xe - 1)
    print(ans)
'''