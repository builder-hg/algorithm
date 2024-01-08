"""
[문제풀이전략]
0. 완전탐색이란?
# 가능성이 있는 후보들을 고른다.
# 정답이 안되는 걸 거른다. 혹은 정답이 되는 걸 센다.

1. 문제 이해 및 정리
- 영수, 1~9 중 서로 다른 세 개로 구성된 세 자리수
- 민혁이가 답을 던지는데,
- 세 자리 수의 동일한 자리에 위치하면 스트라이크 한 번으로 센다. 다른 위치면 볼 한 번으로 센다.
- 질문횟수 N, 1<=N<=100
- 민혁이가생각한수, 스트라이크 수, 볼 수가 입력된다.

2. 문제 풀이 방향
[가능성 있는 후보들]
- 첫번째 위치할 수 있는 경우(9개), 두번째 위치할 수 있는 경우(9개) 그리고 세번째 위치할 수 있는 경우(9개) 각각 순회한다. (모든 수의 조합을 순회한다.)
이 때 첫번재 위치한 수는 두 번째, 세번째에 위치할 수 없다. 두 번째 위치한 수는 세번째에 위치할 수 없다.

[거름작업]
- 물어볼 숫자를 가지고 위 힌트들을 하나씩 살펴본다.
- 힌트숫자가 ABC로 이루어져 있다고 한다면

i) 살펴볼수가 324라면,
123 1 1 
- 324가 ABC 중 스트라이크 수 + 볼 수만큼 가지고 있어야 한다.(안 가지고 있으면 제외시킨다.)
- 힌트로 받은 수를 다음 리스트A, 살펴볼 수를 담은 리스트B를 이중 반복문을 통해 순회한다.
- 힌트 수가 살펴볼 수 안에 있으면서 인덱스(i)또한 일치한다면 스트라이크리스트(크기가 3인 0으로 이루어진 리스트)[i]에 해당 값을 넣고 스트라이크 cnt를 1씩 늘린다.
- 힌트 수가 살펴볼 수 안에 있으면서 인덱스(i)는 일치하지않는다면 금지된위치의 볼리스트(크기가 3인 0으로 이루어진 리스트)[i]에 해당 값을 넣고 볼 cnt를 1씩 늘린다.
- 볼 cnt와 스트라이크 cnt 수가 일치하는 지 판별한다.
- 금지된 볼 리스트에는 무조건 들어가야하는 볼의 정보와, 볼이 들어가지말아야 할 인덱스정보가 저장되어 있다.
- 123과 324를 비교해보았을 때, 스트라이크+볼수만큼 가지고 있으며, 두번째 위치한 2가 동일하며, 첫번째자리에 3이 들어가야한다는 것을 알 수 있다.

356 1 0
327 2 0
489 0 1

ii) 살펴볼 수가 453라면,
123 1 1 
-> ok
356 1 0
-> false  

정리하자면,
1) N 만큼 반복하며 확인할 수(checkpoint)를 주어진 조건(힌트)에 맞춰 걸러낸다. 
2) 힌트 수와 확인할 수를 순회하며(이중반복) (1)스트라이크리스트,히든볼리스트의 정보를 활용해 판별하고 (2)스트라이크 수와 볼 수 그리고 각각의 인덱스 정보를 저장한다.
- 스트라이크리스트순회, 인덱스 i에서, 스트라이크리스트[i]의 값을 valueS라고 한다면, valueS가 0이 아니라면, checkpoint[i]와 valueS를 비교한다. 같지 않은 경우 함수를 종료한다.
- 금지된위치의볼리스트순회, 인덱스 i에서, 금지된위치의볼리스트[i]의 값을 valueB라고 한다면, valueB가 0이 아니라면, checkpoint[i]와 valueB를 비교한다.  같은경우 함수를 종료한다. 
  이때, 볼리스트에 들어간 값이 checkpoint에 있음을 확인 할 경우 해당 반복문을 나간다.
- 힌트수의 특정 숫자가 확인할 수 안에 있으면서 인덱스(i)또한 일치한다면 스트라이크리스트(크기가 3인 0으로 이루어진 리스트)[i]에 해당 값을 넣고 스트라이크 cnt(cntS)를 1씩 늘린다.
- 힌트수의 특정 숫자가 확인할 수 안에 있으면서 인덱스(i)는 일치하지않는다면 금지된위치의 볼리스트(크기가 3인 0으로 이루어진 리스트)[i]에 해당 값을 넣고 볼 cnt(cntB)를 1씩 늘린다.
3) 내가 구한 cntS와 cntB가 영수의 답변과 일치하지 않는다면 함수를 종료한다.
4) 위 조건들에서 걸러지지 않는다면 possible 변수를 1씩 증가시킨다.
5) possible 변수를 출력한다.

[변수정리]
N # 힌트개수
hintWrap = [[힌트숫자, 스트라이크 수, 볼 수], ...] # 힌트에 대한 전체적인 정보 저장
hint = str(힌트숫자) # 주어진 힌트 숫자
hiddenBallList = [0 _ for in range(3)] # 무조건 들어가야하는 볼의 정보와, 볼이 들어가지말아야 할 인덱스정보가 저장되어있다.
requiredSList= [0 _ for in range(3)] # 스트라이크 정보와, 스트라이크가 위치해야할 인덱스 정보가 저장되어있다.
checkpoint # 살펴볼 수
possible # 가능성 있는 수, 초기값 0

"""
import sys

N = int(input())
hintWrap = []
possible = 0
for _ in range(N):
    hint, s, b = map(int, sys.stdin.readline().split())
    hintWrap.append([hint, s, b])

def check(i,j,k):
    checkpoint = str(i) + str(j) + str(k)
    hiddenBallList = [0 for _ in range(3)]
    requiredStrikeList = [0 for _ in range(3)]

    for i in range(N):
        hint, s, b = str(hintWrap[i][0]), hintWrap[i][1], hintWrap[i][2]
        cntS = 0 # 내가 구한 스트라이크 개수
        cntB = 0 # 내가 구한 볼의 개수
        
        for j in range(3):
            for k in range(3):
                if j == k and hint[j] == checkpoint[k]:
                    requiredStrikeList[j] = checkpoint[k]
                    cntS += 1
                if j != k and hint[j] == checkpoint[k]:
                    hiddenBallList[j] = checkpoint[k]
                    cntB += 1
        if s != cntS or b != cntB:
            return False

    return True


for i in range(1, 10):
    for j in range(1, 10):
        if i == j:
            continue
            
        for k in range(1, 10):
            if i == k:
                continue
            if k == j:
                continue
            
            if check(i, j, k): # check함수 내에서 모든 조건 통과시 true를 반환한다. 
                possible += 1  # 조건을 모두 성립하는 경우 가능성 있는 수로 볼 수 있다. 

print(possible)
