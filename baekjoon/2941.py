import sys
input = sys.stdin.readline

arr = input().strip()
lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for alpha in lst:
    arr = arr.replace(alpha, "1")

print(len(arr))