"""
1. 문제접근
1) 가지치기
- 길이가 2일때, 이전요소와 내가 같은지 확인한다.
- 길이가 홀수일 때는 넘어간다.
- 길이가 4일때, 4 // 2 = 2개 => arr[i-1]~arr[i]과 arr[i-3]~arr[i~2]가 같은지 확인한다.
- 길이가 6일때, 6 // 2 = 3개 => 
    temp_a = [0 for _ in range(cur)]
    cnt_a = 0
    temp_b = [0 for _ in range(cur)]
    cnt_b = 0
    for i in range(idx, idx - 몫,-1):
        temp_a[i] = arr[i]
        cnt_a += 1
    for j in range(idx-몫, idx-몫-몫, -1):
        temp_b[i]
        cnt_b += 1           
"""
import sys
input = sys.stdin.readline

N = int(input())

def check(cur, val):
    text = str(val)
    for i in range(1, (cur//2) + 1):
        if text[cur - i:] == text[cur - 2*i:cur - i]:
            return False
        
    return True

def recur(cur, val):
    global ans
    
    # 가지치기
    if not check(cur, val):
        return

    # 기저조건
    if cur == N:
        print(val)
        sys.exit()
    
    # 재귀호출
    for i in range(1, 4):
        total = val * 10 + i
        recur(cur+1, total)

recur(0, 0)
