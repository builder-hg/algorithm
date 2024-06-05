import sys
input = sys.stdin.readline

arr = list(input().strip())
arr = sorted(arr, reverse=True)
print(*arr, sep="")