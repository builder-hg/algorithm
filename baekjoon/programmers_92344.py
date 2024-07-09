board = [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]]
skill = [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]
answer = 0
    
raw = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
K = len(skill)
for i in range(K):
    type, sx, sy, ex, ey, degree = skill[i]
    
    if type == 1:
        degree = -degree
        
    raw[sx][sy] += degree
    if ex + 1 < len(board):
        raw[ex + 1][sy] -= degree   # 아래 갱신
    if ey + 1 < len(board[0]): 
        raw[sx][ey + 1] -= degree   # 오른쪽 갱신
    if ex + 1 < len(board) and ey + 1 < len(board[0]):
        raw[ex + 1][ey + 1] += degree # 이중 갱신 취소 

prefix = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
for i in range(len(board)): # 행 업데이트
    for j in range(len(board[0])):
        if j == 0:
            prefix[i][j] += raw[i][j]
            continue

        prefix[i][j] = prefix[i][j-1] + raw[i][j]
for j in range(len(board[0])):  # 열 업데이트
    for i in range(len(board)):
        if i == 0:
            continue

        prefix[i][j] += prefix[i - 1][j]
for i in range(len(board)): # 원본 값 반영
    for j in range(len(board[0])):
        prefix[i][j] += board[i][j]

ans = 0
for i in range(len(board)): 
    for j in range(len(board[0])):
        if prefix[i][j] > 0:
            ans += 1

print(ans)