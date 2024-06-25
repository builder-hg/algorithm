import sys
input = sys.stdin.readline

def getAlpha(whole, middle, N):
    left = (whole - middle) // 2

    if left >= N:
        return getAlpha(left, middle - 1, N)
    elif left + middle < N:
        return getAlpha(left, middle - 1, N - left - middle)
    else:
        if N - left - 1 == 0:
            return 'm'
        else:
            return 'o'


N = int(input())

leng = 3
nth = 0
while leng < N:
    nth += 1
    leng = leng * 2 + nth + 3

ans = getAlpha(leng, nth + 3, N)
print(ans)