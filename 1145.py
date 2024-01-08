"""
[문제풀이전략]

1. 문제 이해 및 정리
- 적어도 대부분의 배수란, 주어진 5개중 최소 3개로 나뉘어질 수 있어야 지며 그 중에서도 가장 작은 자연수이다. (따라서 3개의 최소공배수)
- 적어도 대부분의 배수를 출력해야 한다.
- 주어진 다섯개의 자연수들은 100보다 작거나 같은 자연수이며 서로 다른 수이다.

2. 문제 풀이 방향
1) 주어진 5개 중에서 3개를 고른다 (5C3 = 5 * 4 * 3 / 3* 2 * 1 = 10)
2) 고른 3개(a, b, c)의 최소 공배수를 구해 리스트에 담는다.
2-1) a, b, c -> a와 b의 최소공배수(d)를 구한다. d와 c의 최소 공배수를 구한다. 그것이 바로 a, b, c의 최소공배수
2-2) a, b의 최소공배수는 a * b / a와 b의 최대공약수 
2-3) a와 b의 최대공약수는
i : 1 ~ a,
A가 i로 나눠지면서
B또한 i로 나눠지면 
공약수에 i를 대입한다.
마지막 공약수가 최대 공약수에 해당한다.
3) 이 중 가장 작은 값을 출력한다.

"""
import sys

numbers = list(map(int, sys.stdin.readline().split()))

LCMList = []
for i in range(5):
    for j in range(i+1, 5):
        # 먼저 뽑은 두수의 최소공배수를 구한다.
        numA = numbers[i]
        numB = numbers[j]
        ABGCD = 0
        for divisorCnt in range(1, numA + 1):
            # 최소 공배수를 구하기 위해 numA와 numB의 공약수를 구한다.
            # 마지막에 대입되는 값이 최대공약수다.
            if numA % divisorCnt == 0 and numB % divisorCnt == 0:
                ABGCD = divisorCnt
                
        ABLCM = int(numA * numB / ABGCD)

        for k in range(j+1, 5):
            numC = numbers[k]
            ABCGCD = 0
            # 앞서 구한 A와B의 최소공배수와 C의 최소공배수를 구한다. 즉, A와 B의 C의 최소공배수를 구한다.
            for divisorCnt in range(1, ABLCM + 1):
                # 최소공배수를 구하기 위해 공약수를 구한다.
                if ABLCM % divisorCnt == 0 and numC % divisorCnt == 0:
                    ABCGCD = divisorCnt
            ABCLCM = int(ABLCM * numC / ABCGCD)
            LCMList.append(ABCLCM)

print(min(LCMList))