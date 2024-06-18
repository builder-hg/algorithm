"""
3,2,1,2,1,7

1 1 2 2 3 7
1 2 3 4 5 6
2 3 4 5 6 8
  1 1 2 2
"""

import sys
input = sys.stdin.readline

nums = [1,2,2]
nums.sort()

ans = 0
id = nums[0]
visited = [False for _ in range(200010)]
for i in range(len(nums)):
    if visited[nums[i]]:    # 이미 왔던 곳이라면,
        visited[id] = True

        ans += id - nums[i]
        id += 1
    else:                   # 처음 오는 곳이라면,
        visited[nums[i]] = True

        id = nums[i] + 1

print(ans)