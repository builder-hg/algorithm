bloomDay = [7,7,7,7,12,7,7]
m = 2
k = 3

def chk(day):
    global m, k

    cnt = 0
    stream = 0
    for i in range(len(bloomDay)):
        if bloomDay[i] > day:
            stream = 0
            continue

        stream += 1

        if stream == k:
            cnt += 1
            stream = 0

    if cnt >= m:
        return True
    else:
        return False

N = len(bloomDay)
if N < m * k:
    print(-1)

ans = 0
s = 1                               # 개화 첫 날
e = max(bloomDay)                    # 개화 마지막날
while s <= e:
    mid = (s + e) // 2

    if chk(mid):
        ans = mid
        e = mid - 1
    else:
        s = mid + 1

print(ans)