"""
Input: nums = [1,2,2,4]
Output: [2,3]
"""
nums = [1,1]
dic = {}
ans = [0, 0]

for i in range(len(nums)):
    dic[nums[i]] = dic.get(nums[i], 0) + 1

    if dic.get(nums[i], 0) != 1:
        ans[0] = nums[i]
    
for i in range(1, len(nums) + 1):
    if dic.get(i, 0) == 0:
        ans[1] = i

print(ans)