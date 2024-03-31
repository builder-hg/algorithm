import sys
import copy
input = sys.stdin.readline

def dfs(cur):
    visited[cur] = True

    for nxt in arr[cur]:
        first.add(cur)
        second.add(nxt)

        if first == second:
            res.extend(list(first))
        
        if visited[nxt]:
            continue

        dfs(nxt)


N = int(input())
arr = [[] for _ in range(N + 1)]
first = set()
second = set()
res = []
for i in range(1, N + 1):
    arr[i].append(int(input()))

for i in range(1, N + 1):
    visited = [False for _ in range(N + 1)]

    dfs(i)

# res = set(res)
# res = list(set(res))
res.sort()
print(res)


# import sys
# import copy
# input = sys.stdin.readline

# def recur(cur, cnt, first, second):
#     global ans
#     global lst
#     global res

#     if cur == N:
#         if first != second:
#             return
        
#         if ans < cnt:
#             res = copy.deepcopy(first)
#             ans = cnt

#         return

#     new_first = copy.deepcopy(first)
#     new_first.append(cur + 1)
#     new_first = sorted(new_first)
#     new_second = copy.deepcopy(second)
#     new_second.append(lst[cur])
#     new_second = sorted(new_second)

#     recur(cur + 1, cnt + 1, new_first, new_second)
#     recur(cur + 1, cnt, first, second)

# N = int(input())
# lst = [int(input()) for _ in range(N)]
# ans = -1
# res = []

# recur(0, 0, [], [])
# res.sort()

# print(ans)
# for i in range(len(res)): print(res[i])