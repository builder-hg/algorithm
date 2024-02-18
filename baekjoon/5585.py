# 8
import sys
input = sys.stdin.readline

pay = int(input())
rest = 1000 - pay
arr = [0,0,0,0,0,0] # 500, 100, 50, 10, 5, 1

if rest >= 500:
    arr[0] += 1
    rest -= 500

if rest // 100 > 0:
    arr[1] = rest // 100
    rest -= arr[1] * 100

if rest // 10 >= 5:
    arr[2] = rest // 50
    rest -= 50

if rest // 10 > 0:
    arr[3] = rest // 10
    rest -= arr[3] * 10

if rest >= 5:
    arr[4] = rest // 5
    rest -= 5

arr[5] = rest

print(sum(arr))
    