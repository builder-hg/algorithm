"""
1층의 1호에는 0층의 ~1호까지의 사람들이 살아야 한다.
0: [1, 2, 3, 4, 5]
1: [1, 3, 6, 10, 15]
2: [1, 4, 10, 20, 35]
3: [1, 5, 15, 30, 55]
"""
import sys
input = sys.stdin.readline

Q = int(input())
arr = [[0 for _ in range(15)] for _ in range(15)]
for i in range(1, 15): # 0 층 세팅
    arr[0][i] = i
for i in range(15): # 1호 세팅
    arr[i][1] = 1

for i in range(1, 15):
    for j in range(1, 15):
        arr[i][j] = arr[i][j-1] + arr[i-1][j]

while Q:
    Q -= 1
    K = int(input())
    N = int(input())
    
    print(arr[K][N])