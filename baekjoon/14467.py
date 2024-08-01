import sys
input = sys.stdin.readline

dic = {}
N = int(input())
ans = 0
for _ in range(N):
    a, b = map(int, input().split())        # 소의 번호 a, 소의 위치 b
    cur = dic.get(a, -1)

    if cur < 0 :                            # 처음 소의 위치가 정해지는 경우
        dic[a] = b
    else:                                   # 소의 위치가 이미 지정되어 있는 경우
        if cur != b:
            ans += 1
            dic[a] = b

print(ans)