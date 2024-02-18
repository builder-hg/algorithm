# 4
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [i for i in range(N+1)]
for _ in range(K):
    index_a, index_b = map(int, input().split())
    
    temp = arr[index_b]
    arr[index_b] = arr[index_a]
    arr[index_a] = temp

print(*arr[1:])