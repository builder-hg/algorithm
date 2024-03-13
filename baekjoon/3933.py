import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def recur(now, goal, cnt):
    global ans 

    if goal < 0 or now > K:
        return
    
    if now ** 2 == goal:
        ans += 1

    recur(now + 1, goal - (now ** 2), cnt + 1)
    recur(now + 1, goal, cnt)

K = int(input())
ans = 0
recur(1, K, 0)
print(ans)

'''import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

while True:
    N = int(input())
    if N == 0:
        break

    ans = 0
    for i in range(1, N + 1):
        if i * i == N:
            ans += 1
            continue

        for j in range(i, N + 1):
            if i * i + j * j == N:
                ans += 1
                break

            for k in range(j, N + 1):
                if i * i + j * j + k * k == N:
                    ans += 1
                    break

                for l in range(k, N + 1):
                    if i * i + j * j + k * k + l * l == N:
                        ans += 1
                        break
                    
                    if i * i + j * j + k * k + l * l > N:
                        break

    print(ans)'''