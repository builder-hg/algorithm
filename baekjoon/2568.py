import sys
input = sys.stdin.readline

def getIndex(val):
    ret = 0

    s = 0
    e = len(LIS) - 1
    while s <= e:
        mid = (s + e) // 2

        if LIS[mid] >= val:
            ret = mid
            e = mid - 1
        else:
            s = mid + 1

    return ret

N = int(input())
raw = []
for _ in range(N):
    a, b = map(int, input().split())
    raw.append([a, b])
raw.sort()
# print(raw)

LIS = [raw[0][1]]
dp = [[0, raw[0][1], raw[0][0]]]
for i in range(1, N):
    if raw[i][1] > LIS[-1]:
        dp.append([len(LIS), raw[i][1], raw[i][0]])
        LIS.append(raw[i][1])
    else:
        index = getIndex(raw[i][1])
        LIS[index] = raw[i][1]
        dp.append([index, raw[i][1], raw[i][0]])

indexLIS = len(LIS) - 1
ans = []
# print(dp)
for indexDP, val, position in dp[::-1]:
    if indexDP != indexLIS:
        ans.append(position)
        continue
    
    indexLIS -= 1

print(N - len(LIS))
for item in ans[::-1]:
    print(item)