"""
customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3

1) 완전탐색
grumpy에서 minutes만큼 길이를 0으로 바꾸는 경우의 수 k = n - minutes + 1, k <= 20000
20,000개의 경우 중 가장 구간합이 큰 경우를 찾아보자. 
"""
customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
minutes = 3

N = len(customers)  # 영업시간
miss = 0            # 놓치고 있는 값

for i in range(minutes):    # 놓치고 있는 값 초기 세팅
    miss += customers[i] * grumpy[i]

tmp = miss
for i in range(minutes, N): # 놓치고 있는 값 중 가장 큰 값을 찾는다.
    tmp += customers[i] * grumpy[i]
    tmp -= customers[i - minutes] * grumpy[i - minutes]

    miss = max(tmp, miss)

ans = miss                  # 확실하게 가져갈 값과 놓치고 있는 값을 더하여 답을 출력하고자 한다. 먼저 놓치고 있는 값의 최대치를 초기값으로 세팅한다.
for i in range(N):
    ans += customers[i] * (1 - grumpy[i])

print(ans)