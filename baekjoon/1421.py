"""
0. 문제정리
N: 나무 개수
cost : 한 번 자를 때 비용
price : 한 단위의 가격
per : 나무 토막 수
profit : 이윤
expense : 비용

1. 접근
1) 자르는 단위: 1부터 주어진 제일 긴 나무 길이만큼늘려본다.
2) 단위별로 잘랐을 때의 이윤을 구한다.
2-1) 주어진 나무를 단위로 나누어본다. 몫과 나머지가 구해진다.
2-2) 이윤은 판매가능한 나무 개수 * 가격 * 길이 - 비용
3) 기존에 구한 이윤보다 크다면 갱신한다. 
"""
import sys
input = sys.stdin.readline

N, cost, price = map(int, input().split())
arr = [int(input()) for _ in range(N)]
leng = max(arr)
ans = 0

for i in range(1, leng + 1):
    temp = 0

    for j in range(N):
        per = arr[j] // i
        rest = arr[j] % i

        if rest:
            expense = per * cost
        else:
            expense = (per - 1) * cost

        profit = ((per * i) * price) - expense
        if profit < 0:
            continue

        temp += profit
    
    if ans < temp:
        ans = temp

print(ans)
