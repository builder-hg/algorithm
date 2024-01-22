"""
[문제풀이전략]
1. 문제 이해 및 정리
- 눈덩이 개수: N, 눈덩이 수열: H(각 원소는 눈덩이의 크기)
- 눈사람은 눈덩이 2개로 만들 수 있다.
- 눈사람의 크기는 눈사람을 이루는 눈덩이의 합이다.
- 눈사람 두개를 만들고 두 눈사람의 키 차이 중 최솟값을 구한다.
- 4<=N<=600, 1<=크기<=10^9

2. 문제 풀이 방향
1) 수열을 정렬한다.
2) 첫번째 눈사람을 만든다.(2중 반복문 활용)
3) 첫번째 눈사람과의 차이가 최소가 되는 두 수의 합을 구한다.
    - 투포인터 s=0, e=n-1을 활용하여 후보가 아닌 것들을 제외한다.
주의할 점)
    - 서로다른 눈덩이를 사용해야 한다.
"""
import sys

N = int(input())
H = sorted(list(map(int, sys.stdin.readline().split())))
ans = 1 << 64

for i in range(N):
    for j in range(N):
        if i == j: 
            continue
        s = 0
        e = N-1
        snowmanA = H[i] + H[j]
        while s < e:
            snowmanB = H[s] + H[e]
            
            if s == i or s == j:
                s += 1
                continue
            if e == i or e == j:
                e -= 1
                continue

            # 이전에 구한 차이값과 새롭게 구한 차이값 중 작은 값을 담는다.
            ans = min(ans, abs(snowmanA - snowmanB))

            if snowmanB < snowmanA:
                s += 1
            else:
                e -= 1

print(ans)