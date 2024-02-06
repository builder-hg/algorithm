import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arrA = sorted(list(map(int, input().split())))
arrB = sorted(list(map(int, input().split())))

# 만들어진 2차원배열에서 x보다 작거나 같은 수가 k개 있는지 확인한다.

s = min(arrA) * min(arrB)
e = max(arrA) * max(arrB)
ans = 0

while s <= e:
    mid = (s + e) // 2  # B[?]의 값에 해당한다.
    cnt = 0

    row_start_idx = 0
    ros_end_idx = N

    for i in range(N):#i는 행
        temp = 0
        # 한 행에서 해당... 해당 mid값이 몇번째에 위치해있는지 확인한다.
        while row_start_idx <= ros_end_idx:
            row_mid_idx = (row_start_idx + ros_end_idx) // 2
            print("row_mid_idx", row_mid_idx)
            if arrB[row_mid_idx] * arrA[i] > mid:
                temp = row_mid_idx
                row_start_idx = row_mid_idx + 1
            else:
                ros_end_idx = row_mid_idx - 1
        cnt += temp
            


    if cnt < K-1:
        s = mid + 1
    else:
        ans = mid
        e = mid - 1

print(ans)