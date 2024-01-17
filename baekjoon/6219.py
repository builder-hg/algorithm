"""
[문제 풀이 전략]
1. 문제 이해 및 정리

2. 문제 풀이 방향
- 주어진 범위의 소수만 긁어모아 리스트를 생성한다. 
(1 이상 4,000,000 이하의 소수가 담겨져있다.)
- 해당 리스트를 순회하며 값(k)을 10으로 나눈 몫이 0이 될 때까지 나눈다.
- 이때 나머지나 몫이 d와 같다면 cnt를 1씩 증가시킨다.
"""
import sys

rangeS, rangeE, find_value = map(int, sys.stdin.readline().split())
ans = 0                                 
# rangeS: 살펴볼 범위의 시작지점, rangeE: 살펴볼 범위의 끝지점, find_value: 찾아야할 수
# ans: 

check = [True for _ in range(rangeE + 1)]
check[0] = False
check[1] = False
for i in range(rangeE + 1):
    if check[i] == False:
        continue
    for j in range(i * i, rangeE + 1, i):
        check[j] = False

for i in range(rangeS, rangeE + 1):
    if check[i] == False:
        continue
    # 소수라면 다음 과정을 거친다.
    share = i // 10
    remainder = i % 10

    if remainder == find_value:
        ans += 1
        continue

    while share > 0:
        remainder = share % 10
        share = share // 10

        if remainder == find_value:
            ans += 1
            break
print(ans)