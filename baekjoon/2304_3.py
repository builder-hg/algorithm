"""
1. 가장 높은 값을 구한다.
2. 높은 값의 좌측에 위치한 막대기는 오름차순으로 순회하고,
    높은 값의 우측에 위치한 막대기는 내림차순으로 접근한다.
3. 동일한 높은 값이 여러개 있을 경우,
가장 왼쪽에 있는 막대기와 가장 우측에 있는 막대기를 고려한다.
- 가장 왼쪽 막대기의 좌측만 오름차순으로 순회한다.
- 가장 오른쪽 막대기의 우측만 내림차순으로 순회한다.
- 중간 값은 가장 오른쪽 막대기 - 가장 왼쪽 막대기 값이다. 
"""
import sys 
input = sys.stdin.readline

def getIndex(x, val):
    if arr[x] != val:
        return False

    return True

N = int(input())
arr = [0 for _ in range(1001)]
position = []               # 막대기의 위치가 담긴 리스트
for _ in range(N):
    a, b = map(int, input().split())

    position.append(a)
    arr[a] = b
position.sort()

left_index = -1
right_index = -1
for i in range(len(position)):
    if arr[position[i]] == max(arr):
        if left_index == -1:
            left_index = i
        
        right_index = i

ans = 0
prv_x = position[0]
prv_y = arr[position[0]]
for i in position[1:left_index + 1]:
    if prv_y > arr[i]:
        continue
    else:
        ans += (i - prv_x) * prv_y
        prv_x = i
        prv_y = arr[i]

prv_x = position[-1]
prv_y = arr[position[-1]]
for i in position[right_index:len(position) - 1][::-1]:
    if prv_y > arr[i]:
        continue
    else:
        ans += abs(i - prv_x) * prv_y
        prv_x = i
        prv_y = arr[i]

if left_index == right_index:
    ans += arr[position[left_index]]
else:
    ans += (position[right_index] - position[left_index] + 1) * arr[position[left_index]]

print(ans)