import sys
input = sys.stdin.readline

def check(text):
    prev = text[0]
    dict[prev] = 1
    for i in range(1, len(text)):
        if text[i] == prev:
            continue

        if dict.get(text[i], 0) > 0:
            return 0
        
        prev = text[i]
        dict[text[i]] = dict.get(text[i], 0) + 1

    return 1

N = int(input())
arr = []
ans = 0
for _ in range(N):
    arr.append(input().strip())

for i in range(N):
    dict = {}
    ans += check(arr[i])

print(ans)