"""
N×(N+1)/2
1 * 2 / 2 = 1
2 * 3 / 2 = 3
3 * 4 / 2 = 6
4 * 5 / 2 = 10
5 * 6 / 2 = 15


# 구간 get을 점 get으로 바꾼다.
1. 누적합 배열을 생성한다.
- prefix[i] - prefix[i-1] == k 에 해당되면 카운팅한다.
- 카운팅배열을 2,000,000,000 * 2까지 만들 수 없다.
2. 딕셔너리를 이용하여 필요한 부분들만 살펴본다.

4 * 5 / 2 = 10

연속부분합이라면,
2 5 6 8
한자리수 : 4개
두자리수 : 3개
세자리수 : 2개
네자리수 : 1개

연속부분합이 아니라면 2^N - 1
2 5 9
한자리수 : 3개
두자리수 : 3개
세자리수 : 1개

"""
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = [0] + list(map(int, input().split()))
ans = 0

prefix_lst = [0 for _ in range(N+1)]
prefix_dict = {}

for i in range(1, N+1):
    prefix_lst[i] = prefix_lst[i-1] + lst[i]

for i in range(1, N+1):
    print(prefix_lst[i])
    key = prefix_lst[i]
    new_key = key - K
    print(prefix_dict.get(new_key, 0) )
    ans += prefix_dict.get(new_key, 0) 
    prefix_dict[key] = prefix_dict.get(key, 0) + 1
print(ans)