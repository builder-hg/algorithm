import sys
input = sys.stdin.readline

N = int(input())
arr = []
lstX = []
lstY = []
for i in range(N):
    x, y = map(int,input().split())
    arr.append([x, y])
arr = sorted(arr)
for i in range(len(arr)):
    print(*arr[i])

# lstX.sort()
# lstY.sort()