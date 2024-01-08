"""
[문제 풀이 전략]

1. 문제이해 및 정리
- 순서 N
- 중복되는 수를 제거 했을 때 K번째 위치한 수를 출력한다.
- 0을 입력하면 프로그램이 종료된다.

2. 문제풀이 방향
K를 10으로 나눴을 때 몫(share)이 9보다 작거나 같을 때까지 계속 나누기를 반복한다.
각각의 연산에서 나온 나머지(remainder)를 활용해서 check[remainder]에 1을 대입한다. 
만약 check[remainder]이 이미 1이면 cnt를 증가시키지 않고 다음 숫자를 살펴본다.
또한, check[10보다 작은 몫] 이 이미 1이면 cnt를 증가시키지 않고 다음 숫자를 살펴본다.
모든 조건을 통과하면 cnt를 1씩 증가시키고 한신이의 리스트[cnt]에 i 값을 넣는다.

식으로 정리하면 다음과 같다.
cnt = 0 # 초기 선언
한신이의 리스트 = [0,0,0,0 ... ], 백만개 사이즈. # 초기선언
한신이의 리스트[i]의 값은 i번째 반복되지 않는 수이다.
1-0) K에 i가 대입된다. 사이즈가 10인 check리스트는 모든 값이 0으로 초기화된다.
1-1) 
while K >= 10:
  remainder = K % 10
  K = K // 10
  if check[remainder] == 1:
    break
1-3)
if check[K] == 1:
  break
1-4) 
cnt += 1
한신이의 수[cnt] = i
"""
import sys

cnt = 0
hansin = [0 for _ in range(1000010)]
i = 0
while cnt <= 1000000:
    i += 1
    K = i
    check = [0 for _ in range(11)]
    ProceedToNext = False

    if K < 10:
        cnt += 1
        hansin[cnt] = i
        continue

    while K >= 10:
        remainder = K % 10
        K = K // 10
        if check[remainder] == 1:
            ProceedToNext = True
            break
        check[remainder] = 1
    if ProceedToNext:
        continue
    if check[K] == 1:
        continue
    cnt += 1
    hansin[cnt] = i

while True:
    N = int(input())
    if N == 0:
        sys.exit()
    print(hansin[N])