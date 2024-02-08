import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
max_value = -1
s = 0
e = N - 1

if e - s == 1:
    print(0)
    sys.exit()

while e - s > 1:
    per = e - s - 1
    max_value = max(max_value, per * min(arr[s], arr[e]))

    if arr[s] <= arr[e]:
        s += 1
    else:
        e -= 1
print(max_value)

"""import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
max_value = -(1 << 64)

for i in range(N):
    for j in range(i + 1, N):
        diff = j - i - 1
        A = arr[i]
        B = arr[j]

        temp = diff * min(A, B)
        max_value = max(temp, max_value)

print(max_value)
"""