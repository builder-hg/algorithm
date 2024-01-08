"""
[문제 풀이 전략]

1. 문제이해 및 정리
- 순서 N
- 중복되는 수를 제거 했을 때 K번째 위치한 수를 출력한다.
- 0을 입력하면 프로그램이 종료된다.

2. 문제풀이 방향
1) ?만큼 순회하면서 cnt를 1씩 증가시킨다.
2) 조건은 다음과 같다.
2-1) 인덱스 i의 값을 문자열(letter)로 바꾸어 리스트에 담는다.
2-2) 문자열의 개수를 leng에 담는다. 리스트를 set 자료형으로 변환 후의 개수를 setLeng에 담는다.
2-3) leng과 setLeng의 개수가 다르다면 cnt를 증가시키지 않는다.
3) cnt가 N와 같아지는 지점의 값을 출력한다.
"""
import sys

N = int(input())
cnt = 0
idx = 0

while True:
    N = int(input())
    cnt = 0
    idx = 1

    if N == 0:
        sys.exit()

    while cnt < N:
        idx += 1
        letter = list(str(idx))
        leng = len(letter)
        setLeng = len(set(letter))

        if leng != setLeng:
            continue
        else:
            cnt += 1
            
    print(idx)