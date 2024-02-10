import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arrA = sorted(list(map(int, input().split())))
arrB = sorted(list(map(int, input().split())))
ans = 0

s = arrA[0] * arrB[0]
e = arrA[N-1] * arrB[N-1]

def countFn(arrA, arrB, val):
    res = 0

    for i in range(N): # 행마다 카운팅해야한다.
        s = 0
        e = N-1
        cnt = 0

# 여기도문제가있다. 이진탐색 ㅠ.ㅠ.ㅠ.ㅠ.ㅠ.ㅠㅠ..ㅠㅠ.ㅠ..ㅠㅠ..ㅠ.ㅠ.ㅠ.ㅠ.ㅠ.ㅠ.ㅠㅠㅠ.ㅠ.ㅠ.ㅠ.
        
        while s <= e:
            mid = (s + e) // 2
            if arrA[i] * arrB[mid] <= val:
                cnt = mid + 1 
                s = mid + 1
            else:
                e = mid - 1
        
        res += cnt

    return res

while s <= e :
    mid = (s + e) // 2
    cnt = countFn(arrA, arrB, mid)

# 아래도 고치고 
    
    if cnt < K:
        s = mid + 1
    else :
        ans = mid
        e = mid - 1

print(ans)

