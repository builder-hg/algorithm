"""
[문제풀이전략]
1. 문제 이해 및 정리
- 최대 N개의 종류의 알파벳을 가진 연속된 문자열만 인식한다.
- 인식할 수 있는 최대 문자열의 길이를 출력한다.
- 입력: 알파벳종류 N(1<=N<=26), 문자열의 길이(1이상 100,000이하)

2. 문제 풀이 방향
type = [a] # type의 초기값은 arr[0]이다.

a b b c a c c b a
s
e
해당 요소의 타입이 리스트에 있는지 확인한다.
있다면 cnt를 1 증가시키고 e를 1 증가시킨다.
만약 타입리스트의 개수가 이미 N인상태에서,
다른 요소의 타입이라면 이전까지의 cnt를 저장하고
s의 위치를 옮기면서 타입개수와 종류를 구분한다.

type의 개수가 N보다 작다면 type을 추가한다.

arr[e] = b
type = [a, b]
e += 1
arr[e] = b # 타입에 현재 값이 있다면


b b a b b c d d 
      s
          e
"""
import sys
N = int(input())
str = input()
lst = list(str)
ans_wrap = []
dict = {}
cnt = 0
types = []    
s = 0               
e = 0
maxV = 0         

while e < len(lst):
    if lst[e] in types:  # 새로 이동한 지점에 위치한 타입이 기존에 있던 타입이라면
        cnt += 1        # cnt를 1증가시킨다.
        dict[lst[e]] += 1
        e += 1          # 끝지점을 한칸 뒤로 이동시킨다.
    else:               # 새로 이동한 지점에 위치한 타입이 기존에 없는 경우
        if len(types) < N:     # 1) 새롭게 타입을 추가해야하는 경우
            cnt += 1
            types.append(lst[e])
            dict[lst[e]] = 1
            e += 1
        else:                # 2) 기존타입을 삭제하고 추가해야 하는경우
            maxV = max(maxV, cnt)
            dict[lst[s]] -= 1
            cnt -= 1
            if dict[lst[s]] == 0:
                types.remove(lst[s])
            s += 1
maxV = max(cnt, maxV)
print(maxV)