"""
수열이 주어집니다.
두 수를 골라서 그 두개 대신 둘의 최솟값을 남기거나 둘의 최대공약수를 남기는 작업을 n - 1번 할겁니다. 그럼 수가 하나 남겠죠.
마지막에 남을 수 있는 수의 종류를 출력하면 됩니다!

6 9 12가 있으면
6 9 최소 남겨서 6 12
6 12 최소 남기거나 6 12 gcd 남기면 6 가능

9 12 gcd 남겨서 6 3
6 3 최소나 gcd 남기면 3

어떤식으로 하든 3이나 6이 남으니 두가지 가능해서 2가 답입니다!

n제한 2000까지, 수열에 있는 수는 10억 이하
===============================================================
두 수를 X, Y라고 했을때...
남는건 min(X,Y) 또는 gcd(X, Y)인데
gcd(X, Y) <= min(X,Y) 이기 때문에
마지막에 남게되는 수는 수열중 가장 작은 값보다 작거나 같을것 같다는 관찰을 해보았읍니다.
===============================================================
어떤 작업이 끝난 후 남는 수는 이전 두 수의 최솟값보다 작거나 같다.
결국 마지막에는 수열의 최솟값 보다 작거나 같다.
확인해보고 싶은 점
1. 주어진 수열들을 순회하며 가장 작은 최대공약수를 구해 계속해서 갱신한다.
2. 구한 최대공약수가 수열의 가장 작은 값보다 크다면 
===============================================================
4
8 2 12 6
순차적으로 살펴보자. 먼저 최솟값으로 남긴다.
2 12 6
2 6
2 

GCD로 남긴다.
2 12 6
2 6
2

7
30 28 33 49 27 37 48
최솟값으로 접근한다.
28 33 49 27 37 48
28 49 27 37 48
28 27 37 48
27
GCD
주어진 수열을 어떻게 묶냐에 따라 GCD가 달라진다.
남을 수 있는 경우의 수는 1 ~ minV, 위 수열에서는 27이니까 1부터 27까지 순회하면서 뭘해볼까

27 28 30 33 37 48 49
- 2가 되기 위해서는,
최대공약수 2가 있고 남은 수는 2보다 작아서는 안된다.
27 28 30 33 48  # 안봐도 될 부분은 날리면된다.
                # 2로 나눠떨어지지 않는 부분을 날린다. 
                    # 최대공약수로 2가나오기만하면되고, 
                    # 최대공약수로 k가 나오기 위해서는 무조건 수열 중에 k의 배수가 2개 이상 있어야 한다.
3 28 30 48
3 2             # 2를 고를 수 있다.
- 3이 되기 위해서는,
최대공약수로 3을 만들고 다른수는 3보다 크거나 같아야 한다.
27 30 33 37 48 49   # 28을, 2로만 나눠질 수 있는 수를 삭제한다.
27 30
3
- 4가 되기 위해서는,
최대공약수로 4를 만들고 나머지 수는 4보다 크거나 같게 만든다. 어? 만들기만 하면 4로 다 줄이면 되는거아님?최솟값으로?
27 28 30 33 37 48 49
4 27 30 33 37 49
- 5가 되기 위해서는, 최대공약수로 5를 만들 수 있냐 없냐(두개의 수가 필요하다.) 판별한다. 안된다.
- 6이 되기 위해서는, 된다.
- 7이 되기 위해서는, 된다.
"""
import sys
# 문제풀이방향)
# 답이 될 수 있는 경우는,
# 수열들로부터 구할 수 있는 최솟값보다 작은 최대공약수와 최솟값이다.
# 최솟값보다 작은 경우는 문제에서 주어진 것처럼 GCD 연산을 통해 남은 값들이며,
# 최대공약수 하나가 구해지면, 다른 수들은 최솟값보다 크기 때문에 해당 최대공약수로 모두 제거할 수 있기 때문이다.
# 따라서 최솟값보다 작은 최대공약수와 최솟값이 답이 될 수 있다.


N = int(input())
lst = list(map(int, sys.stdin.readline().split()))
ans = 0                
min_value = min(lst)   # 최솟값
candidate = {}     # 답이 될 수 있는 후보군이다. 중복된 후보군을 볼 필요가 없기에 set으로 선언한다. 
# 답이 될 수 있는 후보군들은 주어진 수열의 모든 약수들이다. 수열을 돌며 약수들을 구한다.
for num in lst:
    for i in range(1, num+1):
        if i * i > num:
            break
        if num % i == 0:
            if i > min_value:
                continue
            if i not in candidate:
                candidate[i] = num
            else:
                #GCD구하자
                numA = candidate[i]
                numB = num
                while numB:
                    numA, numB = numB, numA % numB
                candidate[i] = numA
            # 첫번째인자는 약수의 값(답이 될 수 있는 후보)이다. 두번째 인자는 해당 약수(첫번째인자)를 가진 수열들의 최대공약수를 기록하는 용도이다.
            if i * i != num:
                if num//i > min_value:
                    continue
                if num//i not in candidate:
                    candidate[num//i] = num
                else:
                    #GCD구하자
                    numA = candidate[num//i]
                    numB = num
                    while numB:
                        numA, numB = numB, numA % numB
                    candidate[num//i] = numA   
"""
# 주어진 후보군들(약수들, 첫번째인자)을 보면서(답이 될 수 있는 모든 범위이다.)
# 해당 약수(첫번째인자)를 가지는 모든 수에 대해서 최대공약수를 구하는 과정을 반복한다. 기존에 두 개일때만 보아서 놓친 부분들을 보강하기 위함이다.
# 최대 공약수를 구하는 과정에서, 해당 약수가 만들어진다면 더 이상 고려하지 않아도 된다.
for i in candidate: # 키(약수) 꺼낸다.
    for j in range(len(lst)):
        # i은 약수에 해당한다.
        # lst[j]는 수열의 원소다.

        if  i == candidate[i]:  # 이미 어떤 수들로부터 구한 최대공약수가 i인 경우이다. 벌써 답이 됐다. 더 안봐도 된다.
            break                            

        if lst[j] % i == 0:   # 수열의 원소가 해당 약수를 지녔다면, 이 약수를 지닌 다른 원소와의 최대공약수를 구해야 한다.
            # 기존에 구한 GCD값이 있다면 이것과 비교하면 되지만, 처음에는 -1이니까 초기값을 세팅한다.
            # 초기값은 다음에 올 원소와 GCD값을 구할 수 있게끔 원소의 값을 두번째 인자에 넣는다.
            # 두번째 인자는 해당 약수를 지닌 원소들의 최대 공약수이다. 이렇게 구한 최대 공약수가 첫번째 인자와 같아진다면 더 고려하지 않아도 된다. 그건 이미 답이다.
            
            if candidate[i] == -1:   # -1인 경우 초기값을 세팅해주어야 한다.
                candidate[i] = lst[j]
            else:                       # 다른 원소와 GCD를 구해야하는 경우이다.
                numA = candidate[i]  # 기존에 구해진 GCD 혹은 GCD를 구해야 할 초기값 -> 어쨌든 GCD 구해야 하는 작업이 필요한 경우
                numB = lst[j]
                while numB:
                    numA, numB = numB, numA % numB
                candidate[i] = numA  # 새롭게 구한 GCD로 갱신한다.
"""


# candidate을 순회하며 첫번째 인자를 최대공약수로 구할 수 있는지 판별한다.(candidate[i][0] == candidate[i][1] 인 경우이다.)
# 아 최솟값보다 작아야 한다. <- 위에서 미리 거름
for i in candidate:
    if i == candidate[i]:
        ans += 1
print(ans)










# for i in range(len(candidate)):
#     # i는 답이될 수 있는 수이다.
#     if i == 0: continue
#     for j in range(len(lst)):
#         # 이미 어떤 두 수로 구하고자 하는 GCD를 만족시켰다면 더 이상 살펴보지 않아도 된다.
#         if candidate[i]
        
#         # 기존에 있던 GCD값과 다른 원소의 값의 최대 공약수를 구한다. (기존에 놓쳤던 부분들에 대한 보강)
#         numA = candidate[i]
#         numB = lst[j]
#         while numB:
#             numA, numB = numB, numA % numB
#         candidate[i] = numA             
        

# import sys

# N = int(input())
# lst = list(map(int, sys.stdin.readline().split()))
# minV = min(lst)
# gcd_wrap = []
# ans = 1

# # for i in range(N):
# #     for j in range(i+1, N):
# #         numA=lst[i]
# #         numB=lst[j]
# #         while numB:
# #             numA, numB = numB, numA % numB
# #         if numA < minV:
# #             gcd_wrap.append(numA)

# # 안되는 애들은 뭐가있을까? 사실 후보에 들어가면 안되는 애들 뭐가 있을까? x
# # 답이 되는데 안 본 애들이 있다는 이야기다. 
# # 3개를 GCD 해보았을 때 a,b,c가 있을 때 (a,b),(a,c),(b,c) 뿐만아니라 (a,b,c)를 놓치고 있는게 아닐까?


# gcd_wrap = set(gcd_wrap)
# print(gcd_wrap)
# print(len(gcd_wrap) + 1)

# ===========================================================
# N = int(input())
# A = list(map(int, input().split()))

# def gcd(a, b):
#     if b: return gcd(b, a%b)
#     return a

# def divisors(n):
#     res = []
#     for i in range(1, n+1):
#         if i * i > n: break
#         if n % i != 0: continue
#         res.append(i)
#         if i * i != n:
#             res.append(n // i)
#     res.sort()
#     return res

# print("dict는 key를 약수로 가진 수들의 최대공약수다.")
# dict = {}
# for i in range(N):
#     # print("divisors","(A[",i,"])", divisors(A[i]));
#     for prime in divisors(A[i]):
#         # print("A[i]",A[i],"prime", prime)
#         if prime  in dict:
#             # print("dict", dict)
#             # print("기존 dict내 값",dict[prime], "새롭게 비교할 값", A[i])
#             dict[prime] = gcd(dict[prime], A[i])
#         else:
#             # print("새롭게 추가될 값", A[i])
#             dict[prime] = A[i]
# print(dict)
# ans = 0
# minA = min(A)
# for k, v in dict.items():
#     print(k, v)
#     if k == v and k <= minA:
#         ans += 1
# print(ans)