"""
N = 1, (2 * 2 배열)
sz = 1

N = 2,
sz =  2 ** (2 * 2 - 2) = 4
width = 2 = sz ** 0.5

3행 3열의 값 = 1행 1열의 값 + (sz * 3)

N = 3,
sz = 16 = 2 ** (2 * N - 2)
width = sz ** 0.5 = 4

5행 6열의 값 = 1행 2열 + (sz * 3)   # 열과 행이 동시에 바뀌면 sz + 3
2행 5열의 값 = 2행 1열 + (sz * 1)   # 열만 바뀌면 sz + 1
6행 2열의 값 = 2행 2열 + (sz * 2)   # 행만 바뀌면 sz + 2
"""
import sys
input = sys.stdin.readline

def getOrder(sz, x, y):
    width = int(sz ** 0.5)

    if sz == 1:
        return arr[x][y]

    if x < width and y < width:
        return getOrder(int(sz // 4), x, y)
    elif x < width and y >= width:
        return getOrder(int(sz // 4), x, y - width) + sz
    elif x >= width and y < width:
        return getOrder(int(sz // 4), x - width, y) + 2 * sz
    else:
        return getOrder(int(sz // 4), x - width, y - width) + 3 * sz


N, R, C = map(int, input().split())
arr = [[0, 1], [2, 3]]

if N == 1:
    print(arr[R][C])
    sys.exit()

ans = getOrder(2 ** (2 * N - 2), R, C)
print(ans)