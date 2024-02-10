"""
0. 특징
- 파이썬의 sort 혹은 sorted를 사용시 대문자 오름차순 > 소문자 오름차순으로 정렬된다.

1. 고민
- 길이가 짧은 것을 어떻게 선별할 수 있을까.

2. 완전탐색 / 구현
1) 문자열의 길이만큼(51) 2차원 배열 구현 
2) 문자열의 길이에 맞게 해당 인덱스 배열에 넣는다.
3) 각 i행을 정렬한다.
4) 2차원 배열을 출력한다.
"""
import sys
input = sys.stdin.readline

N = int(input())
random = set()
arr = [[] for _ in range(51)]
ans = []

for i in range(N):
    word = input().strip()
    random.add(word)

random = list(random)
for i in range(len(random)):
    leng = len(random[i])
    arr[leng].append(random[i])

for i in range(51):
    if len(arr[i]) == 0:
        continue

    arr[i].sort()
    for j in range(len(arr[i])):
        print(arr[i][j])