"""
0. 아이디어
- B[k] = x일때, B행렬에는 x보다 작거나 같은게 최소 k개 있다.
- x를 조정하여 x보다 작거나 같은게 k개 있도록 한다.
- Q) x보다 작은 원소들의 개수를 찾으려면 행렬을 만들어야 하지않나?
    A) 행마다 x // i (행 인덱스)를 구해서 더하면 된다.

3. 설계
- s = 1, e = N, mid = (s )

"""
import sys
input = sys.stdin.readline

N = int(input())
K = int(input())

# s, e 세팅.
s = 1
e = K
ans = 0

while s <= e:
    # mid 갱신. B[k]의 값에 해당한다.
    mid = (s + e) // 2 
    cnt = 0

    # mid보다 작거나 같은 원소들의 개수를 구해 cnt에 담는다.
    for i in range(1, N+1):
        if mid // i == 0:   # mid 보다 작은 원소가 존재하지 않는 행이라면 빠져나간다.
            break
        if (mid // i) > N:
            cnt += N
        else:
            cnt += (mid // i)

    if cnt < K:
        s = mid + 1
    elif cnt >= K:
        ans = mid 
        e = mid - 1

print(ans)