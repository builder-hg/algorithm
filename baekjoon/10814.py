import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    age, name = input().split()
    arr.append([i, int(age), name])

arr.sort(key = lambda x:(x[1],x[0]))
for i in range(N):
    age, name = arr[i][1], arr[i][2]
    print(age, name)