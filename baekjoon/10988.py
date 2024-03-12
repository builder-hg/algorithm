import sys
input = sys.stdin.readline

def recur(s, e):
    global ans

    if arr[s] != arr[e]:
        ans = False
        return 
    
    if s == e or s + 1 == e:
        ans = True
        return 
    
    recur(s + 1, e - 1)

arr = list(input().strip())
leng = len(arr) - 1
ans = False
recur(0, leng)
if ans:
    print(1)
else:
    print(0)