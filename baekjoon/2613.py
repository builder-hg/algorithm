import sys
input = sys.stdin.readline

def check(mid):
    global size

    total_ball_cnt = []
    group_cnt = 0
    i = 0

    while i <= N - 1:
        ball_sum = 0
        ball_cnt_per_group = 0

        while i <= N - 1:
            ball_sum += arr[i]
            ball_cnt_per_group += 1

            if ball_sum > mid:
                ball_cnt_per_group -= 1
                ball_sum -= arr[i]
                break

            if M - group_cnt == N - i:
                i += 1
                break

            i += 1

        total_ball_cnt.append(ball_cnt_per_group)
        group_cnt += 1

    if M >= group_cnt:
        size = total_ball_cnt

    return M >= group_cnt

        

def binary_search():
    s = max(arr)
    e = sum(arr)
    ans = 0

    while s <= e:
        mid = (s + e) // 2

        if check(mid):
            ans = mid
            e = mid - 1
        else:
            s = mid + 1

    return ans

N, M = map(int, input().split())
arr = list(map(int, input().split()))
size = []

print(binary_search())
print(*size)

# # 24.04.17
# import sys
# input = sys.stdin.readline

# def binary_search():
#     ans1 = (1 << 60)
#     s = max(arr)    # 소그룹의 합 중 최댓값은 해당 그룹의 최댓값 이상이여야 한다.
#     e = sum(arr)    

#     while s <= e:
#         mid = (s + e) // 2  # mid: 소그룹의 합 중 최댓값
#         lst = []            # lst: 소그룹의 합을 담을 리스트
#         group = []         # group: 소그룹의 개수를 저장할 리스트 
#         group_cnt = 0       # group_cnt : 소그룹 내의 인자들의 개수
#         cnt = 0             # cnt: 소그룹의 개수
#         total = 0           # total: 소그룹의 합

#         for i in range(N):
#             group_cnt += 1  # 소그룹의 인자가 하나씩 늘어난다.
#             total += arr[i] # 소그룹의 총합에 더해진다.

#             if total == mid:    # 총합이 최댓값과 같으면,
#                 cnt += 1        # 소그룹의 개수를 하나 증가시키고
#                 group.append(group_cnt) # 소그룹내의 인자의 개수를 저장한다.
#                 group_cnt = 0
#                 lst.append(total)   # 해당 소그룹의 총합을 저장한다.
#                 total = 0
#             elif total > mid:   # 총합이 최댓값을 넘어버리면,
#                 cnt += 1        # 소그룹의 개수를 하나 증가시키고
#                 group.append(group_cnt - 1) # 소그룹내의 인자의 개수를 저장하는데 이 때 넘치기 전까지의 개수만 저장한다.
#                 group_cnt = 1
#                 lst.append(total - arr[i])  # 해당 소그룹의 총합을 저장하는데 이 때 넘치기 전까지의 총합만 저장한다.
#                 total = arr[i]

#         if total != 0:  # 소그룹에 들어가지 않은 총합이 있다면,
#             cnt += 1    # 소그룹의 개수를 하나 증가시키고
#             lst.append(total)   # 해당 소그룹의 총합을 저장하고
#             group.append(group_cnt) # 소그룹내의 인자의 개수를 저장한다.
#             group_cnt = 0
#             total = 0

#         if cnt > M:         # 소그룹의 개수가 우리가 원하는 그룹의 개수보다 많다면
#             s = mid + 1     # s를 증가시켜 그룹의 최댓값을 키운다.
#         else:              # 소그룹의 개수가 우리가 원하는 그룹의 개수와 같다면
#             ans1 = mid
#             for j in range(len(group)):
#                 ans2[j] = group[j]
#             e = mid - 1             # e를 감소시켜 그룹의 최댓값을 줄인다.
#         # else:               # 소그룹의 개수가 우리가 원하는 그룹의 개수보다 적다면
#         #     e = mid - 1     # e를 감소시켜 그룹의 최댓값을 줄인다.

#     return ans1

# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
# ans2 = [0 for _ in range(301)]    # 소그룹 내 인자의 개수를 담을 리스트
# print(binary_search())
# print(*ans2)



# """
# 0. 완전탐색
# 1) M개의 그룹을 이루는 모든 경우를 탐색한다.
# M = 3이고 그룹을 A, B, C라고 했을 때
# A그룹에 1부터 N-2, B 그룹에 1, C 그룹에 1 씩 모두 넣어보는 것이다.
# 0-2. 고민
# 0-2-1.
# 1) grouping을 효과적으로 하는 방법을 생각해본다.
# 2) 정렬 후, 반복문으로 점 하나를 선택 후, 나머지 점 하나는 이진탐색으로 구한다.
# 3) 점 A, B, C에 대해 0~A-1까지, A~B-1까지, B~N-1까지의 합을 각각 구하면 어떨지 생각한다.
# 3-2) 위와 같이 grouping을 한다면 C그룹의 합이 엄청 커지기에 적합하지 않다.
# 0-2-2.
# 1) 합이 최소가 되려면 어떻게 구성해야할지 생각한다.
# 2) 합이 최소가 되려면 각 그룹별합의 최댓값과 최솟값의 차이가 작아야 한다.
#     즉, 값이 비슷비슷해야한다는 의미다.
# 3) 최솟값부터 최댓값까지 순회한다. 이 때 이진탐색으로 순회한다. mid의 값이 특정 합에 해당한다.
# 4) 주어진 수열에서 우리가 구한 mid값(특정합)을 M개 만들 수 있는 지 없는 지 확인한다.
# 6) M개 이상 만들 수 있다면 s = mid + 1
# 7) M개 미만으로 만들 수 있다면 e = mid - 1

# 0. 완전탐색(리트라이)
# - A 그룹에서 한 개 골랐을 때, B가 고를 수 있는 경우는 1부터 N-2개까지
# - A 그룹의 수를 한 개씩 증가시키고 B가 고를 수 있는 경우는 1부터 N-2-i이다.
# - 각 경우의 합을 구한다.
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# arr = [0] + list(map(int, input().split()))     # 입력받은 구슬 배열
# prefix = [0 for _ in range(N+1)]                # 구슬의 누적합이 기록된 배열
# prefix[1] = arr[1]

# for i in range(2, N+1):
#     prefix[i] = prefix[i-1] + arr[i]

# group_a = 0
# group_b = 0
# group_c = 0
# total = prefix[-1]
# val = 1 << 64
# lst = [0, 0, 0]

# for i in range(1, len(arr)-2):
#     group_a = prefix[i]
#     for j in range(i+1, len(arr)-1):
#         group_b = prefix[j] - prefix[i]
#         group_c = total - group_a - group_b

#         temp_max = max(group_a, group_b, group_c)
#         if temp_max < val:
#             val = temp_max
#             lst[0], lst[1], lst[2] = i, j-i, N-j

# print(val)
# print(*lst)
# """
# # 0-2-2.
# # 1) 합이 최소가 되려면 어떻게 구성해야할지 생각한다.
# # 2) 최솟값부터 최댓값까지 순회한다. 이 때 이진탐색으로 순회한다. mid의 값이 특정 합에 해당한다.
# # 3) 주어진 수열에서 우리가 구한 mid값(특정합)을 M개 만들 수 있는 지 없는 지 확인한다.
# # 4) M개 이상 만들 수 있다면 s = mid + 1
# # 5) M개 미만으로 만들 수 있다면 e = mid - 1

# import sys
# import copy
# input = sys.stdin.readline

# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
# val = 1 << 64
# lst = []
# lst = []

# for i in range(1, 30001):
#     prefix_sum = 0
#     cnt = 0
#     temp = []
#     for j in range(N):
#         prefix_sum += arr[j]

#         if j == N-1:
#             cnt += 1
#             temp.append(prefix_sum)
#             break

#         if prefix_sum == i:
#             cnt += 1
#             temp.append(prefix_sum)
#             prefix_sum = 0
#         elif prefix_sum > i:
#             cnt += 1
#             temp.append(prefix_sum - arr[j])
#             prefix_sum = arr[j]

#     if cnt == M:
#         if max(temp) < val:
#             val = max(temp)
#             lst = copy.deepcopy(temp)

# idx = 0
# for i in lst:
#     while idx < N:
#         i -= arr[idx]
        
#         if i == 0:
#             lst.append(idx)
#             idx += 1
#             break
#         idx += 1

# print(val)
# print(lst[0]+1, end=" ")
# for i in range(1, len(lst)):
#     print(lst[i]-lst[i-1], end=" ")