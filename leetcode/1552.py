"""
position = [1,2,3,4,7], m = 4
[1, ]


"""
position = [5,4,3,2,1,1000000000]
m = 2

def chk(dis):
    prev = position[0]
    cnt = 1
    for cur in position[1:]:
        if cur - prev >= dis:
            prev = cur
            cnt += 1
        
    return cnt >= m

position.sort()
s = 1
e = position[-1]
ans = 0

while s <= e:
    mid = (s + e) // 2

    if chk(mid):
        ans = mid
        s = mid + 1
    else:
        e = mid - 1

print(ans)