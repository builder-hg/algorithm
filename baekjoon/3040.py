import sys
input = sys.stdin.readline

raw = []
for _ in range(9):
    raw.append(int(input()))
arr = sorted(raw)

diff = sum(arr) - 100
rm1 = 0
rm2 = 0
s = 0
e = 8
while s < e:
    if arr[s] + arr[e] == diff:
        rm1, rm2 = arr[s], arr[e]
        for i in range(9):
            if raw[i] == rm1 or raw[i] == rm2:
                continue

            print(raw[i])
        break
    elif arr[s] + arr[e] > diff:
        e -= 1
    elif arr[s] + arr[e] < diff:
        s += 1