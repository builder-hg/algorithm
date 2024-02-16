"""
8 3
5 4 2 6 9 3 8 7

가장 큰 그룹이 30 이하가 되도록 만들 수 있나?  o
가장 큰 그룹이 15 이하가 되도록 만들 수 있나?  x

[완전탐색]
1. 첫 그룹에 1~n개, 두번째 그룹에도 1~n, .... 
=> m - 1 중 반복문 구현해서 해결 가능. => 백트래킹
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int,  input().split()))
ans = [0 for _ in range(M)]

def recur(cur):
    if cur == N:
        print(ans)
        return
    
    for i in range(M):


recur(0)
