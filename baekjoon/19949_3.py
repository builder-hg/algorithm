import sys
input = sys.stdin.readline

lst = list(map(int, input().split()))
arr = [0 for _ in range(10)]
ans = 0

def check(cur):
    if cur < 3:
        return True

    if arr[cur - 1] == arr[cur - 2] and arr[cur - 2] == arr[cur - 3]:
        return False

    return True

def recur(cur, score):
    global ans

    # 가지치기, 기존에 채워진 값이 3개 이상일 경우 확인한다.
    if not check(cur):
        return

    # 기저조건
    if cur == 10:
        if score >= 5:
            ans += 1
        return
    
    for i in range(1, 6):
        arr[cur] = i
        
        add = 0
        if arr[cur] == lst[cur]:
            add = 1

        recur(cur + 1, score + add)


recur(0, 0)
print(ans)