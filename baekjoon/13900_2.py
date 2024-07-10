import sys
input = sys.stdin.readline

"""
5
1 2 3 4 5 인 경우,
1,  (1 * 2) + (1 * 3) + (1 * 4) + (1 * 5) => 1 * (2 + 3 + 4 + 5)
2, +(2 * 3) + (2 * 4) + (2 * 5) => 2 * (3 + 4 + 5)
3, +(3 * 4) + (3 * 5) => 3 * (4 + 5)
4, +(4 * 5) => 4 * 5

위 식은 다음처럼 정리할 수 있다. 
arr[i]로 만들 수 있는 두 수의 곱의 합은, 
전체 합에서 arr[i]를 뺀 값 * arr[i]이다.
"""

N = int(input())
arr = list(map(int, input().split()))

total = sum(arr)
ans = 0
for val in arr:
    total -= val
    ans += val * total

print(ans)