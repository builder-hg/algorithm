import sys
input = sys.stdin.readline

arr = list(input().strip())
i = 0
ans = 0

while i < len(arr):
    cur = arr[i]

    if cur == 'c' and i + 1 < len(arr):
        nxt = arr[i + 1]
        if nxt == '=' or nxt == '-':
            ans += 1
            i += 2
    elif cur == 'd' and i + 1 < len(arr):
        nxt = arr[i + 1]
        if nxt == '-':
            ans += 1
            i += 2
        elif nxt == 'z':
            if i + 2 < len(arr):
                if arr[i + 2] == '=':
                    ans += 1
                    i += 3
            else:
                ans += 2
                i += 2
    elif cur == 'l' and i + 1 < len(arr):
        if 



    ans += 1
    i += 1

print(ans)