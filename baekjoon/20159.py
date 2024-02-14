import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
max_sum = -(1 << 64)
stack = []

# 한 번의 밑장 빼기를 고려하여 가능한 모든 경우를 탐색
for i in range(N):
    # i번째 카드를 밑장으로 빼는 경우
    card_sum = 0
    stack.append(arr[i])
    required_plus = False
    for j in range(0,N,2):
        if j == i:
            required_plus = True
        if j != i:  # 밑장을 빼는 경우는 건너뜀
            card_sum += arr[j]
    if required_plus:
        card_sum += arr[i]
    max_sum = max(max_sum, card_sum)

print(max_sum)