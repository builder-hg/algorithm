# 7
import sys
input = sys.stdin.readline

arr = [0 for _ in range(5)]
for i in range(5):
    num = int(input())
    arr[i] = num

arr.sort()
print(sum(arr) // 5)
print(arr[2])