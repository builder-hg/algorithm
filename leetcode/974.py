import sys
input = sys.stdin.readline

nums = [5]
k = 9

ans = 0
total = 0
_dict = {}
_dict[0] = 1 

for num in nums:
    total += num
    remainder = (total % k)
    ans += _dict.get(remainder, 0)
    _dict[remainder] = _dict.get(remainder, 0) + 1

print(ans)

# ans = 0
# N = len(nums)

# def recur(cur, cnt, total, change, continuous):
#     global ans

#     if cur == N:
#         if cnt > 0 and total % k == 0:
#             ans += 1

#         return

#     if change:
#         if continuous:
#             recur(cur + 1, cnt + 1, total + nums[cur], True, True)
            
#         recur(cur + 1, cnt, total, change, False)
#     else:
#         recur(cur + 1, cnt + 1, total + nums[cur], True, True)
#         recur(cur + 1, cnt, total, change, False)

# recur(0, 0, 0, False, True)

# print(ans)