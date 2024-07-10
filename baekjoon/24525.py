import sys
input = sys.stdin.readline

raw = [0] + list(input().strip())       # 원본 배열
arr = [0 for _ in range(len(raw))]      # 치환한 값을 담을 배열
chk = [0 for _ in range(len(raw))]      # 인덱스 i 지점까지 S가 나온 횟수가 담긴 배열
for i in range(1, len(raw)):
    if raw[i] == 'K':                   # K라면 -1로 바꾼다.
        arr[i] = -1
        chk[i] = chk[i - 1] + 1         # S 또는 K가 나왔다면 1씩 증가시킨다.
    elif raw[i] == 'S':                 # S라면 2로 바꾼다.
        arr[i] = 2
        chk[i] = chk[i - 1] + 1         # S 또는 K가 나왔다면 1씩 증가시킨다.
    else:
        chk[i] = chk[i - 1]

prefix = [0 for _ in range(len(arr))]
for i in range(1, len(prefix)):         # 누적합 배열 생성
    prefix[i] = prefix[i - 1] + arr[i]  

dic = {}
ans = -1
for i in range(len(raw)):
    cur = prefix[i]
    if prefix[i] not in dic:
        dic[prefix[i]] = i
    else:
        prv_index = dic[prefix[i]]
        if chk[prv_index] == chk[i]:
            continue
        ans = max(ans, i - prv_index)


print(ans)