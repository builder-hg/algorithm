import sys
input = sys.stdin.readline
alpha_dict = {}

arr = list(input().strip())
for i in range(len(arr)):
    if ord(arr[i]) > 96:
        val = ord(arr[i]) - 32
    else:
        val = ord(arr[i])

    alpha_dict[val] = alpha_dict.get(val, 0) + 1

ans = [key for key, value in alpha_dict.items() if max(alpha_dict.values()) == value]
if len(ans) > 1:
    print("?")
else:
    print(chr(ans[0]))

    