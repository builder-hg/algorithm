
"""
0. 완전탐색
1) M개의 그룹을 이루는 모든 경우를 탐색한다.
M = 3이고 그룹을 A, B, C라고 했을 때
A그룹에 1부터 N-2, B 그룹에 1, C 그룹에 1 씩 모두 넣어보는 것이다.
0-2. 고민
0-2-1.
1) grouping을 효과적으로 하는 방법을 생각해본다.
2) 정렬 후, 반복문으로 점 하나를 선택 후, 나머지 점 하나는 이진탐색으로 구한다.
3) 점 A, B, C에 대해 0~A-1까지, A~B-1까지, B~N-1까지의 합을 각각 구하면 어떨지 생각한다.
3-2) 위와 같이 grouping을 한다면 C그룹의 합이 엄청 커지기에 적합하지 않다.
0-2-2.
1) 합이 최소가 되려면 어떻게 구성해야할지 생각한다.
2) 합이 최소가 되려면 각 그룹별합의 최댓값과 최솟값의 차이가 작아야 한다.
    즉, 값이 비슷비슷해야한다는 의미다.
3) 최솟값부터 최댓값까지 순회한다. 이 때 이진탐색으로 순회한다. mid의 값이 특정 합에 해당한다.
4) 주어진 수열에서 우리가 구한 mid값(특정합)을 M개 만들 수 있는 지 없는 지 확인한다.
6) M개 이상 만들 수 있다면 s = mid + 1
7) M개 미만으로 만들 수 있다면 e = mid - 1

0. 완전탐색(리트라이)
- A 그룹에서 한 개 골랐을 때, B가 고를 수 있는 경우는 1부터 N-2개까지
- A 그룹의 수를 한 개씩 증가시키고 B가 고를 수 있는 경우는 1부터 N-2-i이다.
- 각 경우의 합을 구한다.
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))     # 입력받은 구슬 배열
prefix = [0 for _ in range(N+1)]                # 구슬의 누적합이 기록된 배열
prefix[1] = arr[1]

for i in range(2, N+1):
    prefix[i] = prefix[i-1] + arr[i]

group_a = 0
group_b = 0
group_c = 0
total = prefix[-1]
val = 1 << 64
ans = [0, 0, 0]

for i in range(1, len(arr)-2):
    group_a = prefix[i]
    for j in range(i+1, len(arr)-1):
        group_b = prefix[j] - prefix[i]
        group_c = total - group_a - group_b

        temp_max = max(group_a, group_b, group_c)
        if temp_max < val:
            val = temp_max
            ans[0], ans[1], ans[2] = i, j-i, N-j

print(val)
print(*ans)
"""
# 0-2-2.
# 1) 합이 최소가 되려면 어떻게 구성해야할지 생각한다.
# 2) 최솟값부터 최댓값까지 순회한다. 이 때 이진탐색으로 순회한다. mid의 값이 특정 합에 해당한다.
# 3) 주어진 수열에서 우리가 구한 mid값(특정합)을 M개 만들 수 있는 지 없는 지 확인한다.
# 4) M개 이상 만들 수 있다면 s = mid + 1
# 5) M개 미만으로 만들 수 있다면 e = mid - 1

import sys
import copy
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
val = 1 << 64
lst = []
ans = []

for i in range(1, 30001):
    prefix_sum = 0
    cnt = 0
    temp = []
    for j in range(N):
        prefix_sum += arr[j]

        if j == N-1:
            cnt += 1
            temp.append(prefix_sum)
            break

        if prefix_sum == i:
            cnt += 1
            temp.append(prefix_sum)
            prefix_sum = 0
        elif prefix_sum > i:
            cnt += 1
            temp.append(prefix_sum - arr[j])
            prefix_sum = arr[j]

    if cnt == M:
        if max(temp) < val:
            val = max(temp)
            lst = copy.deepcopy(temp)

idx = 0
for i in lst:
    while idx < N:
        i -= arr[idx]
        
        if i == 0:
            ans.append(idx)
            idx += 1
            break
        idx += 1

print(val)
print(ans[0]+1, end=" ")
for i in range(1, len(ans)):
    print(ans[i]-ans[i-1], end=" ")