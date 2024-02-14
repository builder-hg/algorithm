"""
두번째시도(24.02.03)

하나를 고른다
얘랑 더해서 0에 제일 가까워지는 애를 구한다

일단 -5를 골랐다 치면
-3 1 4 5 중에 5에 제일 가까운걸 이진탐색으로 찾겠다는 뜻인데
mid는 1이고 일단 -5 + 1      이건 살펴봤는데 절댓값이 4네오케이 얘는 그냥 두고
얘보다 좋은게 있다면 어디 있을까 4, 5중에 있겠지 s = mid + 1 해주면 되겠네
다시 mid는 이제 4가 될거고 기존에 제일 좋았던건 -5 + 1이었는데
지금 mid를 보니 -5 + 4야 얘가 더 좋으니 갱신해주고
 더 좋은게 있다면 왼쪽일까 오른쪽일까? 그럼 5만 남았는데
mid는 5일거고 -5 + 5가 이제까지 제일 좋았던 -5 + 4보다 좋으니 갱신하고
더 좋은게 나올리가 없겠네


"""
import sys

N = int(sys.stdin.readline().rstrip())

arr = list(map(int, sys.stdin.readline().split()))

minV = 1 << 64
idx1 = 0
idx2 = N - 1

for idx in range(N - 1):
    s = idx + 1
    e = N - 1

    while s <= e:
        mid = (s + e) // 2
        temp = arr[mid] + arr[idx]

        if abs(temp) < minV:
            idx1 = idx
            idx2 = mid
            minV = abs(temp)
        
        if temp == 0:
            break
        elif temp < 0:
            s = mid + 1
        else:
            e = mid - 1

print(arr[idx1], arr[idx2])














"""
처음시도(실패)
- lower, upper 로 접근
- 그냥 아예 개념부터 틀림

arrA = [-99 -2 -1 4 98]
arrB = [-99 -2 -1 4 98]

lower_bound(arrB, 0): 두 원소의 합이 0 보다 크거나 같은 값 중 가장 앞의 인덱스를 찾는다.
    (0과 가장 가까운 양수값을 찾는다.)
upper_bound(arrB, 0): 두 원소의 합이 0 보다 큰 값들 중 가장 앞의 인덱스를 찾아서 해당 인덱스에 - 1 한 값을 구한다.
    (0과 가장 가까운 음수값을 찾는다.)

import sys
input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int, input().split())))
val = 1 << 64
ans = [0,0]

def lower_bound(arr, x):
    # 시작점이 x일 때 e만 움직여서 두 합이 0보다 크거나 같은 값 중 가장 앞의 인덱스가 되게끔 s 와 e 를 설정한다.
    s = x
    e = N - 1 
    ans = N - 1 

    while s <= e:
        change = False
        mid = (s + e) // 2

        if arr[s] + arr[mid] >= 0:
            change = True
            ans = mid
            e = mid - 1
        
        if change == False:
            break

    if s == mid:
        return [1 << 64, 1 << 64]
    
    print('lower', arr[s], arr[ans])

    return [arr[s], arr[ans]] 

def upper_bound(arr, x):
    # 시작점이 x일 때 e만 움직여서 두 합이 0보다 큰 값 중 가장 앞의 인덱스가 되게끔 s 와 e 를 설정한다.
    s = x
    e = N - 1
    ans = N - 1

    while s <= e:
        change = False
        mid = (s + e) // 2

        if arr[s] + arr[mid] > 0:
            change = True
            ans = mid
            e = mid - 1

        if change == False:
            break

    if s == ans - 1:
        return [1 << 64, 1 << 64]

    print('upper',arr[s], arr[ans-1])

    return [arr[s], arr[ans-1]]

for i in range(N):
    lower_index = lower_bound(arr, i)
    upper_index = upper_bound(arr, i)

    if abs(lower_index[0] + lower_index[1]) <= val:
        val = abs(lower_index[0] + lower_index[1])
        ans[0] = lower_index[0]
        ans[1] = lower_index[1]

    if abs(upper_index[0] + upper_index[1]) <= val:
        val = abs(upper_index[0] + upper_index[1])
        ans[0] = upper_index[0]
        ans[1] = upper_index[1]

print(*sorted(ans))
"""