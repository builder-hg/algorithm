t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    dp = [[[0 for _ in range(2)] for _ in range(k+100)] for _ in range(n+100)]
    
    dp[n][k][0] = 0
    dp[n][k][1] = 0

    for i in range(n)[::-1]:
        for j in range(k)[::-1]:
            for l in range(2):
                dp[i][j][l] = dp[i+1][j][0] + dp[i+1][j+l][1]
                
       
    print(dp[0][0][0])
