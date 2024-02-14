import sys
input = sys.stdin.readline

def binary_search(val, arr):
    s = 0
    e = len(arr) - 1
    ans = arr[(s+e)//2]

    while s <= e:
        mid = (s + e) // 2

        if arr[mid] == val:
            return val
        elif arr[mid] < val:
            s = mid + 1
        else:
            e = mid - 1

        if abs(arr[mid] - val) < abs(ans - val):
            ans = arr[mid]

    return ans


lenA, lenB, lenC = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))

result = 1 << 64

for i in range(lenA):
    if result == 0:
        break

    selectA = A[i]                                  # A 값을 선택한다.
    selectAB = binary_search(selectA, B)            # B리스트에서 선택한 A 값과 가장 값이 근처에 있는 값을 선택한다. 
    selectABC = binary_search(selectAB, C)          # 앞에서 고른 B값과 가장 근처에 있는 값을 선택한다.
    selectAC = binary_search(selectA, C)

    max_val = max(selectA, max(selectAB, selectABC))    # 이렇게 고른 세 가지 값의 최대값을 뽑는다.
    min_val = min(selectA, min(selectAB, selectABC))    # 이렇게 고른 세 가지 값의 최솟값을 뽑는다.
    result = min(result, abs(max_val - min_val))

    max_val = max(selectA, max(selectAB, selectAC))    # 이렇게 고른 세 가지 값의 최대값을 뽑는다.
    min_val = min(selectA, min(selectAB, selectAC))    # 이렇게 고른 세 가지 값의 최솟값을 뽑는다.
    result = min(result, abs(max_val - min_val))

print(result)