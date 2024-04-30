import sys
input = sys.stdin.readline

def recursion(arr, s, e):
    global cnt
    ans = 1

    if s >= e:
        return ans, cnt
    elif arr[s] != arr[e]:
        ans = 0
        return ans, cnt
    else:
        cnt += 1
        return recursion(arr, s + 1, e - 1)

    return ans

def isPalindrome(arr):
    global cnt

    cnt += 1
    return recursion(arr, 0, len(arr) - 1)

Q = int(input())
while Q:
    Q -= 1

    cnt = 0
    arr = input().rstrip()
    print(*isPalindrome(arr))