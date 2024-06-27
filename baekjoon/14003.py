import sys
input = sys.stdin.readline

def getIndex(val):
    ret = 0

    s = 0
    e = len(LIS) - 1
    while s <= e:
        mid = (s + e) //2

        if LIS[mid] >= val:
            ret = mid
            e = mid - 1
        else:
            s = mid + 1

    return ret

N = int(input())
arr = list(map(int, input().split()))

LIS = [arr[0]]
dp = [[0, arr[0]]]     # i번째 원소는 arr[i]가 LIS에 위치한 인덱스와 arr[i]의 값으로 이루어져 있다.
for i in range(1, N):
    if arr[i] > LIS[-1]:
        dp.append([len(LIS), arr[i]])
        LIS.append(arr[i])
    else:
        index = getIndex(arr[i])
        LIS[index] = arr[i]
        dp.append([index, arr[i]])

indexLIS = len(LIS) - 1
ans = []
for indexDP, val in dp[::-1]:
    if indexDP != indexLIS:
        continue
    
    ans.append(val)
    indexLIS -= 1

print(len(LIS))
print(*ans[::-1])