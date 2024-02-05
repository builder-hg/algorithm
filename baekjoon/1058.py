import sys
input = sys.stdin.readline

N = int(input())
arr = [list(input().strip()) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
ans = []

for i in range(N):
    friends = []
    candid = []
    cnt = 0

    for j in range(N):
        if i == j:
            continue

        if arr[i][j] == 'Y':
            print(i,'의 친구는 ',j,'이다')
            cnt += 1
            friends.append(i)
        else:
            candid.append(i)

    for friend in friends:
        for j in candid:
            if arr[friend][j] == 'Y':
                print(i,'의 친구 ', friend, '의 친구중에',j,'가 있다.')
                cnt += 1

    ans.append(cnt)
print(max(ans))
