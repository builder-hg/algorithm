# 0 모듈러의 성질
- 모듈러 연산이란? 나머지 연산을 뜻한다. 
- 공식 : (a+b) % c == (a%c + b%c) % c
a = xc + y
b = wc + z
a + b = (x + w) * c + y + z
(a + b) % c = y + z = (a % c + b % c) % c
- 모듈러 연산은 +, *, -, // 연산에 대해서 수학적으로 되지만 //는 코딩할 때는 안된다고 생각하자.
- -에 있어서도 음수가 나오는 경우 원하는 답이 도출되지 않을 수 있기에 (a - b) % c == (a % c - b % c + k * c) % c로 계산하여 접근하자.
-번외, 1부터 1,000,000,000까지의 합을 1,000,000,007로 나눴을 때의 나머지를 구하자
```
total = 0
for i in range(1, 1000000001):
    total += 1
    total %= 1000000007
print(total)
```

# 소수 판정
- 자연수 하나를 입력 받아서 이 수가 소수면 1을, 소수가 아니면 0을 출력해보자.
- 소수 판정에서 주의할 점은 1이다.
## 완전탐색으로 소수한정하는 방법
- n 제한이 일반적으로 10^12 정도로 나오게 되는데, 이럴 경우 완탐으로 돌면 시간초과가 뜰 수 있다.
```
N = int(input())
cnt = 0
for i in range(1, n+1):
    if N % i == 0:
        cnt += 1
if cnt == 2: # 1과 자기자신만 존재하는 경우이므로
    print("1")
else:
    print("0")
```
## root N 까지만 탐색하자
- 1 ~ root n 까지의 약수가 정확히 하나인지 구한다.
- 12의 약수(1, 2, 3, 4, 6, 12)를 보면 (1, 12), (2, 6), (3, 4)의 순서쌍으로 이루어져 있다. 해당 순서쌍들의 첫번째 인자는 root N 이하임을 알 수 있다.
```
N = int(input())

cnt = 0
for i in range(1, n+1):
    # root N보다 큰 값은 더 이상 계산하지 않는다.
    # sqrt와 같은 실수 연산은 되도록 하지 말자.
    if i * i > N:
        break
    if N % i == 0:
        cnt += 1
    
if cnt == 1:
    print("1")
else:
    print("0)
```

# 약수 구하기
## 완전탐색으로 접근하는 방법
```
N = int(input())
prime = []

for i in range(1, N+1):
    if N % i == 0:
        prime.append(i)

print(*prime)
```

## 순서쌍으로 하는 방법
- 제곱수를 조심해야 한다.
- 약수의 개수가 홀수이다 = 제곱수랑 필요충분 조건이다.
```
N = int(input())
prime = []

for i in range(1, n+1):
    if i * i > n:
        break
    if N % i == 0:
        prime.append(i)
        if i * i != N:
            prime.append(N//i)

print(*prime)
``` 

# 소인수 분해
## 완전탐색으로 소인수 분해하기
```
N = int(input())
X = N
for i in range(2, N + 1):
    while X % i == 0:
        print(i)
        X //= i
```
## root N까지만 살펴보는 방법
- N => a * b * c * d * e 
- a, b, c, d, e 중에서 rootN 보다 크거나 같은 수는 하나이거나 없다.
```
N = int(input())
X = N
for i in range(2, N+1):
    if i * i > N:
        break
    while X % i == 0:
        print(i)
        X //= i

```

# 유클리드 호제법
## 최대공약수 구하기
- 두 자연수 a, b가 주어질 때 이 둘의 최대 공약수를 구한다.(log n)
- a < b 일 때 a와 b-a를 남기는 작업을 반복하면 된다.
```
a, b = map(int, input().split())
while b % a != 0:
    a, b = b, b % a
print(a)
```
## 최소 공배수 구하기
```
a, b = map(int, input().split()) # a < b라고 하자

A, B = a, b
while b % a != 0:
    a, b = b % a, a
print(A * B // a)
```

# 에라토스테네스의 체
## 1. 완전탐색으로, 1 ~ n 까지의 자연수 중 소수를 출력하는 방법
```
N = int(input())
isPrime = [True for i in range(n+1)] # 소수가 아닌 것들은 False로 바꾼다.
isPrime[0] = False
isPrime[1] = False # 1은 소수가 아니기에 False
for i in range(2, N+1):
    if isPrime[i] == False: # 소수가 이미 아니라고 판정난 것들은 살펴보지 않는다.
        continue
    for j in range(2*i, N+1, i):
        isPrime[j] = False

for i in range(N+1):
    if isPrime[i]:
        print(i)
```
## 2. 가지치기 방법으로, 1 ~ n 까지의 자연수 중 소수를 출력한다.
```
N = int(input())
isPrime = [True for _ in range(N+1)]
isPrime[0] = False
isPrime[1] = False
# 0과 1은 소수가 아니므로 False를 대입한다.
for i in range(2, N+1):
    if isPrime[i] == False:
        continue
    for j in range(i * i, N+1, i):
        isPrime[j] = False
for i in range(N+1):
    if isPrime[i]:
        print(i)
```
## 3. 응용하기
### 2 ~ N 까지의 자연수 각각의 가장 작은 소인수를 출력한다.
```
N = int(input())
prime = [-1 for i in range(N+1)]
for i in range(2, N+1):
    if prime[i] != -1: # 각각의 인덱스에 이미 가장작은 소인수가 들어가 있는 경우
        continue 
    prime[i] = i # 소인수를 대입한다.
    for j in range(i * i, N+1, i):
        if prime[i] == -1:
            prime[i] = i # 소인수를 대입한다.
print(*prime[2:])
```

# 빠른 거듭제곱
- 3 ** 28을 구할 때
```
ans = i
```