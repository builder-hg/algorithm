"""
[문제풀이전략]
1. 문제 이해 및 정리
- 수열의 길이 N
- 수열 내 원소는 1 이상인 정수
- 수열 내 원소 중 최대 K번 삭제 가능
- 최대 K번 삭제하여 짝수로 이루어진 구간의 길이 중 가장 큰 값을 출력한다.

2. 문제 풀이 방향
8 2

1 2 3 4 5 6 7 8
      s
              e
0) ans=0, s=0, e=0, k = 1
1) e = 1, ans=1, k=1
2) e=2, ans=1,k=2
3) s=1,e=2, ans=1, k=1
4) s=1,e=3, ans=2, k=1
5) s=1,e=4, ans=2, k=2
6) s=2,e=4, ans=1, k=2
7) s=3,e=4, ans=1, k=1
8) s=3,e=5, ans=2, k=1
9) s=3,e=6, ans=2, k=2
10)

2 1 2 1 2 2 
어떤 구간까지의 짝수개수를 구한다.
해당 구간까지의 홀수개수를 구한다.
해당 구간에서의 최대 짝수개수를 구한다.
K번 다썼다면 충전시킬 때까지 s를 이동시킨다. 
덜 썼다면 e += 1
"""
import sys
N, remove_cnt = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
s = 0
e = 0
cnt = 0
if lst[0] % 2 == 0:
    cnt = 1
else:
    remove_cnt -= 1
ans = 0
while e < N:
    # 다음 지점으로 이동시킨 후에 혹은 이동시키기 전에 수행할 연산을 다룬다.
    if remove_cnt >= 0: # 더 삭제할 수 있거나 당장 삭제하지 않아도 되는 경우에 해당한다.
        e += 1          # 더 가도 되기에 직진 

        if e == N:
            ans = max(ans, cnt)
            break

        if lst[e] % 2 == 1: # 갈 곳이 홀수라면
            remove_cnt -= 1 # 삭제가능횟수가 줄어든다
        else:               # 짝수라면 
            cnt += 1
    else:               # 더 이상 삭제할 수 없는데 삭제해야만 할 경우에 해당한다.
        # 최대치로 왔으니 답이 될 수 있는지 체크한다.
        ans = max(ans, cnt)

        if lst[s] % 2 == 1:
            remove_cnt += 1
        else:
            cnt -= 1
        s += 1

print(ans)