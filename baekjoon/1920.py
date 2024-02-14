"""
0. 완전탐색
- N개의 집합과 M개의 집합을 전체 순회하면 10,000,000,000를 넘을 수 있다. 시간초과가 난다.
- M개는 필수적으로 순회해야 한다. 
- N을 순회하는 횟수를 줄인다.
1. 이진탐색
- N개의 집합을 정렬한다.
- 이진탐색을 통해 찾아야할 수 K가 있는지 없는지 확인한다.
"""
import sys
input = sys.stdin.readline

N = int(input())
lst = sorted(list(map(int, input().split())))
M = int(input())
finding = list(map(int, input().split()))
ans = []

def check(arr, val):
    s = 0
    e = len(arr) - 1

    while s <= e:
        mid = (s + e) // 2

        if arr[mid] == val:
            return 1
        elif arr[mid] < val:
            s = mid + 1
        else:
            e = mid - 1

    return 0 

for i in range(M):
    val = finding[i]
    res = check(lst, val)

    ans.append(res)

for i in range(len(ans)):
    print(ans[i])