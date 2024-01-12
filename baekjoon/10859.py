"""
[문제풀이전략]

1. 문제 이해 및 정리
- 주어진 수가 소수이고 해당 수가 뒤집어졌을때도 소수인지 확인한다.
- 0, 1, 2, 5, 8은 뒤집어져도 동일하다
- 6과 9는 뒤집어지면 각각 9와 6이 된다.
- 3, 4, 7은 뒤집어지면 숫자가 아니다.
- 주어지는 수 N은 1이상 10^16이하이다.

2. 문제 풀이 방향
key) 에라토스테네스의 체를 이용하여 소수를 판별한다.
    - 2를 제외한 홀수를 대상으로 순회한다. -> 계산범위가 1 이상 10^8 이하로 줄어든다.
key) 주어진 수를 뒤집는 과정을 반복한다.
    - 1의 자리가 9로 나누어 떨어지면 제외한다.
    - 몫이 0이 될 때까지 순회하며 몫과 나머지에 3, 4, 7이 하나라도 있다면 제외된다.
    - 몫과 나머지를 활용하여 뒤집어진 수를 구한다.
key) 에라토스테네스의 체에 입력받은 N과 뒤집어진 수를 넣고 소수인지 판별한다.
"""
import sys

N = int(input())        # N은 1이상 10^16이하이다.
share = N // 10         # 몫
remainder = N % 10      # 나머지
reverse_value = 0 
if N == 1 :
    print("no")
    sys.exit()
if remainder == 6:      # 뒤집어진 수의 초기값은 나머지로 설정한다 이때 나머지가 6이라면 9로, 9라면 6으로 바꾼다.
    reverse_value = 9
elif remainder == 9:
    reverse_value = 6
else:
    reverse_value = remainder

while share != 0:                                   # N의 값이 10 이상일 때, 몫이 0이 될 때까지 계속 10으로 나누며 몫과 나머지를 확인한다. 
    if remainder == 3 or remainder == 4 or remainder == 7: 
        print("no")
        sys.exit()
    remainder = share % 10
    share = share // 10
    if remainder == 3 or remainder == 4 or remainder == 7: 
        print("no")
        sys.exit()
    if remainder == 6:
        remainder = 9
    elif remainder == 9:
        remainder = 6
        
    reverse_value = reverse_value * 10 + remainder

cnt_n = 0
cnt_reverse = 0

for i in range(1, N+1):                             # 주어진 수 N이 소수인지 판별한다.
    if i * i > N:
        break
    if N % i == 0:
        cnt_n += 1

for i in range(1, reverse_value + 1):               # 뒤집은수가 소수인지 판별한다.
    if i * i > reverse_value:
        break
    if reverse_value % i == 0:
        cnt_reverse += 1

if cnt_n == 1 and cnt_reverse == 1:
    print('yes')
else:
    print('no')



# for i in range(3, leng, 2):
#     if check[i] == False:   # 소수가 아니기에 더 살펴보지 않는다.
#         continue

#     for j in range(i*i, leng, i):    # 소수가 아닐 부분들을 미리 제거한다.
#         if j == N:
#             print("no")
#             sys.exit()
#         check[j] = False

# if check[N] == False or check[reverse_value] == False:
#     print("no")
# else:
#     print("yes")