"""
nums = [1,5,10], n = 20
patch = [2, 4]
=> [1, 2, 4, 5, 10]
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,16, 17, 18, 19, 20

기존에는
1, 5, 6, 10, 11,15
"""

nums = [1, 3]
n = 6

total = 0
cnt = 0
for i in range(len(nums)):
    while total < n and total + 1 < nums[i]:
        total += (total + 1)
        cnt += 1

    total += nums[i]

while total < n:
    total += total + 1
    cnt += 1

print(cnt)