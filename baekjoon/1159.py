"""
1. 주어진 배열을 순회하며 첫 글자를 카운팅한다 (딕셔너리 사용)
2. 딕셔너리를 순회하며 값이 5이상이라면 답에 더해준다.
3. 답의 길이가 1이상이라면 해당 답을 출력하고 그렇지 않다면 "PREDAJA"를 출력한다.
"""
import sys
input = sys.stdin.readline

N = int(input())
arr = []
dict = {}
ans = []
for _ in range(N):
    _str = input().strip()
    first = _str[0]
    arr.append(_str)
    dict[first] = dict.get(first, 0) + 1

for key in dict:
    if dict[key] >= 5:
        ans.append(key[0])

if len(ans) > 0:
    ans.sort()
    print(*ans, sep="")
else:
    print("PREDAJA")