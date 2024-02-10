import sys
input = sys.stdin.readline

N = int(input())
w, h = map(int, input().split())
cnt = 0

arr = []
for _ in range(N):
    x, y = map(int, input().split())
    arr.append([x, y])
arr.sort()

def binary_search(arr, val):
    s = 0
    e = len(arr) - 1

    while s <= e :
        mid = (s + e) // 2
        if arr[mid] == val:
            return True
        elif arr[mid] > val:
            e = mid - 1
        else:
            s = mid + 1
    return False

for i in range(N):
    x, y = arr[i]

    rb = [x + w, y]
    lt = [x, y + h]
    rt = [x + w, y + h]

    if binary_search(arr, rb) == False: continue
    if binary_search(arr, lt) == False: continue    
    if binary_search(arr, rt) == False: continue

    cnt += 1

print(cnt)