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

N = int(input())
lst = list(map(int, sys.stdin.readline().split()))
minV = min(lst)
GCD_wrap = []
ans = 1     # 최솟값을 포함하고 시작한다.

# 필요한 연산, 1부터 N-1까지의 수 중 최대공약수로 만들 수 있는 경우를 생각한다.


for i in range(N):
    for j in range(i, N):
        numA = lst[i] 
        numB = lst[j]
        while numB:
            numA, numB = numB, numA % numB
        GCD_wrap.append(numA)

GCD_wrap = set(GCD_wrap)
for i in range(1, minV):
    if i in GCD_wrap:
        ans += 1

print(ans)