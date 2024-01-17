"""
[문제풀이전략]
1. 문제 이해 및 정리
- 입력: 첫 번째 수가 시작 범위, 두 번째 수가 끝 범위
- 출력: 범위 내에서 소수이며 팰린드롬인 수를 구한다.
- 출력: 오름차순으로 출력하며 마지막 줄에는 -1을 출력한다.

2. 문제 풀이 방향
- 에라토스테네스의 체로 소수를 판별한다.
- 10으로 나누고 나머지를 더한 값을 다시 10으로 곱하고 최종적으로 구한 값과 처음 주어진 값이 일치하는지 본다.
"""
import sys

start, end = map(int, sys.stdin.readline().split())
check = [True for _ in range(end + 1)]
check[0] = False
check[1] = False 

for i in range(end + 1):
    if check[i] == False:
        continue
    if i * i > end:
        break
    for j in range(i * i, end+1, i):
        check[j] = False

for i in range(start, end+1):
    if check[i] == False:
        continue
    share = i // 10
    remainder = i % 10
    palindrome = remainder

    while share > 0:
        remainder = share % 10
        share = share // 10
        palindrome = palindrome * 10 + remainder
    
    if i == palindrome:
        print(i)

print(-1)