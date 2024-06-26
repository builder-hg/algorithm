import sys
input = sys.stdin.readline

def getIndex(val):
    ret = 0
    s = 0
    e = len(LMS) - 1
    while s <= e:
        mid = (s + e) // 2

        if LMS[mid] >= val:
            ret = mid
            e = mid - 1
        else:
            s = mid + 1

    return ret

N = int(input())
arr = list(map(int, input().split()))

LMS = [arr[0]]
for i in range(1, N):
    if arr[i] > LMS[-1]:
        LMS.append(arr[i])
    else:
        index = getIndex(arr[i])
        LMS[index] = arr[i]

print(len(LMS))