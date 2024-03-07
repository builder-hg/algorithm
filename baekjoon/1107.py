import sys
input = sys.stdin.readline

# def get_click_cnt(end):
#     num = 0

#     for i in range(end):
#         num = ans[i] + num * 10
    
#     to_str = str(num)
#     return abs(N - num) + len(to_str)

def recur(cur, val):
    global press
    if cur > 0:
        press = min(press, abs(N - val) + cur)

    if cur == 7:
        return
    
    for i in range(len(arr)):
        recur(cur + 1, val * 10 + arr[i])

N = int(input())
M = int(input())
arr = [i for i in range(10)]
if M != 0:
    lst = list(map(int, input().split()))
    for i in lst:
        arr.remove(i)
ans = [0 for _ in range(7)]
press = abs(N - 100)

recur(0, 0)
print(press)