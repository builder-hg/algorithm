import sys
input = sys.stdin.readline

arr = []
for i in range(10):
    num = int(input())
    arr.append(num % 42)

arr = set(arr)
print(len(arr))