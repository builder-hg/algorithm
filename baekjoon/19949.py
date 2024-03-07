import sys
input = sys.stdin.readline

lst = [-1] + list(map(int, input().split()))   # 실제 정답
arr = [0 for _ in range(11)]            # 영재의 답안지
ans_case_cnt = 0                        # 5점이상인 경우의 수

def recur(cur, cnt):                    # cur이 위치, cnt는 맞춘 답의 개수 
    global ans_case_cnt

    # 가지치기
    if cur >= 3:
        if arr[cur] == arr[cur-1] and arr[cur-1] == arr[cur-2]:
            return

    # 기저조건
    if cur == 10:    
        if cnt >= 5:   
            ans_case_cnt += 1
        return

    this_cnt = 0
    if lst[cur] == arr[cur]:
        this_cnt += 1

    for i in range(1, 6):
        arr[cur + 1] = i
        recur(cur + 1, cnt + this_cnt)

recur(-1, 0)
print(ans_case_cnt)
