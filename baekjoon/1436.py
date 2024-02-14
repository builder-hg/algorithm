"""
0. 관찰
0번째 종말의 수 : 666
7번째 종말의 수 : 6660
8번째 종말의 수 : 6661
9번째 종말의 수 : 6662
10번째 종말의 수: 6663 
...
1. 특징파악
- 완전탐색으로 파악하는 경우를 생각해본다.
- N이 10,000이면 66,600,000 내에서 무조건 모두 살펴볼 수 있다.
- 6이 연속으로 붙어있어야 한다.
"""
import sys
input = sys.stdin.readline
cnt = 0

N = int(input())
for i in range(666, 6600001):
    num = i 
    temp = 0
    linear = 0
    while num:
        res = num % 10  
        if res == 6:
            linear += 1
            temp += 1 
        else:
            linear = 0
        num = num // 10

        if temp >= 3 and linear == 3:
            cnt += 1
            break
    if cnt == N:
        print(i)
        sys.exit()