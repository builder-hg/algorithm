"""
0. 특징
1) 소수점 이하 첫째자리에서 반올림한 값 출력을 위해 round 함수를 사용한다.
2) arr[N//2]
3) 딕셔너리로 관리한다.
    - 전달받은 값의 개수를 딕셔너리로 관리한다.
    - 딕셔너리를 순회하며 현재의 개수보다 더 많은 개수를 지녔다면, ans와 cnt의 값을 대체한다. 동일하다면 ans에 추가한다.
    - ans를 내림차순으로 정렬하여 두번째 값을 출력한다.
4) max(arr) - min(arr)
"""
import sys
input = sys.stdin.readline

N = int(input())
arr = []
dd = {}

for i in range(N):
    num = int(input())
    arr.append(num)
    dd[num] = dd.get(num, 0) + 1
candid = []
cnt = 0
for key, val in dd.items():
    if val == cnt:
        candid.append(key)
    elif val > cnt:
        cnt = val
        candid = [key]
candid.sort()
arr.sort()

first = round(sum(arr) / N)
second = arr[N // 2]
if len(candid) > 1:
    third = candid[1]
else:
    third = candid[0]
last = max(arr) - min(arr)
print(first)
print(second)
print(third)
print(last)