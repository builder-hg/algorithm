import sys
input = sys.stdin.readline

lst = list(map(int, input().split()))
reverse = [0, 0]
for i in range(2):
    for _ in range(3):
        reverse[i] *= 10
        reverse[i] += lst[i] % 10
        lst[i] //= 10

ans = reverse[0]
if reverse[0] < reverse[1]: ans = reverse[1]

print(ans)