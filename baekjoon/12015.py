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

LMS = [arr[0]]   # 초깃값  
for i in range(1, N):
    if arr[i] > LMS[-1]:     # 마지막으로 저장한 값보다 크다면,
        LMS.append(arr[i])   # 해당 값을 저장한다.
    else:                       # 마지막으로 저장한 값보다 작을 때,
        idx = getIndex(arr[i])  # LMS내에서 해당 값의 순서(index)를 구한다.
        LMS[idx] = arr[i]       # 해당 순서의 값을 arr[i]로 갱신한다. 더 작은 수로 갱신함으로써
                                # 가장 긴 부분수열을 구할 수 있다.

print(len(LMS))