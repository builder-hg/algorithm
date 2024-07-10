import sys
input = sys.stdin.readline

s = [0] + list(input().strip())
prefix = [0] * (len(s))
cnt = [0] * (len(s))
minidx = {}

for i in range(1, len(s)):
    n = 0
    if s[i] == 'S':
        n = 2
    if s[i] == 'K':
        n = -1
    prefix[i] = prefix[i - 1] + n
    cnt[i] = cnt[i - 1] + (0 if n == 0 else 1)

ans = -1

for i in range(len(s)):
    cur = prefix[i]
    if prefix[i] not in minidx:
        minidx[prefix[i]] = i
    else:
        prv_index = minidx[prefix[i]]
        if cnt[prv_index] == cnt[i]:
            continue
        ans = max(ans, i - prv_index)

print(ans)