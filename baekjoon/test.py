n = int(input())
arrN = list(map(int, input().split()))
m = int(input())
arrM = list(map(int, input().split()))
arrN.sort()

def lower_bound(x):
    s = 0
    e = n-1
    ans = 0

    while s <= e:
        mid = (s+e) // 2
        if arrN[mid] >= x:
            ans = mid
            e = mid - 1
        else:
            s = mid + 1

    return ans

def upper_bound(x):
    s = 0
    e = n-1
    ans = -1

    while s <= e:
        mid = (s+e) // 2
        if arrN[mid] <= x:
            ans = mid
            s = mid + 1
        else:
            e = mid - 1

    return ans

for i in range(m):  
    a = upper_bound(arrM[i])
    b = lower_bound(arrM[i])
    if i == m-1:
        print(a-b+1)
    else:
        print(a-b+1, end=" ")