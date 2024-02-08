"""
0. 문제이해
- 모두 다 동일하게 만들어야 한다.
- 최댓값을 맞추어야 한다.
    최댓값보다 작은 값들을 모두 더했는데도 값을 일치시킬 수 없다면 두 개를 합쳐나간다.
1. 완전탐색
- 차례로 순회한다.
- 현재 값과 이전 값을 합쳤을 때 맥시멈값보다 작다면 더해주고 새로운 배열에 넣어준다.
- 새롭게 만든 배열을 순회한다.
- 위의 과정을 계속해서 반복한다.
- 시간초과. 새롭게 배열을 만들고 이를 계속 순회하는 과정이 오래 걸릴 것이다.
=> 배열을 새롭게 만들지 말고 그 자리에서 바로 반복하면 되지 않을까.

2. 관찰
raw = 2 2 3
prefix = 2 4 7
7의 약수는 하나

0 0 0 0 0
0의 약수가 되기 위해서는 별다른 조치를 취하지 않아도 된다.

3. 구현/설계
- 누적합을 구현한다.
- 제일 마지막 인덱스의 값을 구한다.
- 누적합에서 제일 마지막 인덱스의 약수의 개수를 구한다.
- 만약 제일 마지막 인덱스가 0이라면 답은 0이다.

4. 테스트케이스 재관찰
누적합이 = [2, 4, 8, 12]
답은 1이 돼야 한다.
하지만 첫번째로 내가 짠 코드는 2를 카운팅하지 않는 문제가 있다.
약수의 목록을 구해서 약수를 순회하며 순회가 가능하며 그 수가 작은 cnt를 출력한다.
"""
import sys
input = sys.stdin.readline

Q = int(input())
while Q:
    Q -= 1
    N = int(input())
    arr = list(map(int, input().split()))
    prime = []
    prefix = [0] * N
    prefix[0] = arr[0]
    acc = sum(arr)
    max_value = max(arr)
    s = 0

    if max_value == 0:
        print(0)
        continue

    for i in range(1, N+1):
        if i * i > acc:
            break
        if acc % i == 0:
            prime.append(i)
            if i * i != acc:
                prime.append(acc // i)

    prime.sort()

    for i in range(len(prime)):
        flag = True
        if prime[i] < max_value:
            continue

        prefix = 0
        for j in range(N):
            prefix += arr[j]
            if prefix == prime[i]:
                prefix = 0
            elif prefix > prime[i]:
                flag = False
                break
        if flag:
            print(N - acc // prime[i])
            break

"""
import sys
input = sys.stdin.readline

Q = int(input())

while Q:
    Q -= 1
    N = int(input())
    raw = list(map(int, input().split()))
    cnt = 0
    candid = []
    prefix = [0] * N
    prefix[0] = raw[0]
    for i in range(1, N):
        prefix[i] = raw[i] + prefix[i-1]
    maxV = max(prefix)
    if maxV == 0:
        print(0)
        continue

    prime = []
    for i in range(1, maxV+1):
        if i * i > maxV:
            break
        if maxV % i == 0:
            prime.append(i)
            if i * i != maxV:
                prime.append(maxV // i)
    prime.sort()

    print('prime', prime)

    for i in range(len(prime)):
        total = maxV // prime[i]
        temp = 0
        ans = 0
        for j in range(N):
            print('prefix[j]', prefix[j])
            print('prime[i]', prime[i])
            if j>0 and prefix[j] == prefix[j-1]:
                temp += 1
                ans += 1
                continue
            if prefix[j] % prime[i] == 0:
                temp += 1
            else:
                ans += 1
        if total == temp:
            candid.append(ans)
        
    print(min(candid))
"""