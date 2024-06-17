import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
ans = 0
dic = {}

for i in range(N):
    _key = arr[i]
    if dic.get(_key, 0) != 0:
        ans += 1
    
    dic[_key] = dic.get(_key, 0) + 1

print(ans)
