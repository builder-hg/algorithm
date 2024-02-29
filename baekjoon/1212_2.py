import sys
input = sys.stdin.readline
# 시간초과


N = int(input())
arr = list(str(N))
cnt = 0
val = 0

# 2의 3승
# 3 1 4
# 10진수로 변환
for i in range(len(arr)-1, -1, -1):
    num = int(arr[i])
    val += (num * (8 ** cnt))
    cnt += 1

ans = []
share = val
# 2진수로 변환
while share > 1:
    ans.append(share % 2)
    share //= 2
ans.append(share)

print(*ans[::-1], sep="")
