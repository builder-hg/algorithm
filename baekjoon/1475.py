"""
# 개수만큼 세트 수 + 1
1, 2, 3, 4, 5, 7, 8, 0 

# 6, 9 의 경우,
올(6과 9의 개수 / 2)
"""
import sys
input = sys.stdin.readline

arr = list(input().strip())

ans = 0
dic = {}
for i in range(len(arr)):
    dic[arr[i]] = dic.get(arr[i], 0) + 1

for i in range(10):
    key = dic.get(str(i), 0)
    if str(i) == '6' or str(i) == '9':
        keys = dic.get(str(6), 0)
        keys += dic.get(str(9), 0)

        s, r = divmod(keys, 2)
        if r:
            ans = max(ans, s + 1)
        else:
            ans = max(ans, s)
        continue

    if key >= 1:
        ans = max(ans, key)


print(ans)

