"""
A. :으로 구분하여 배열에 저장한다.
    - 2번 규칙이 적용되었는 지 파악한다. 배열의 길이가 8이 아니라면 그 차이(diff)를 저장한다.
    - 현재요소가 ''이 아니고 길이가 4보다 적다면 앞에 0을 채워 새로운 배열에 담아준다.
    - diff만큼 0000을 넣어준다.
"""
import sys
input = sys.stdin.readline

raw = list(map(str, input().rstrip().split(":")))
diff = 8 - len(raw)
for i in range(len(raw)):
    if not raw[i]:
        diff += 1

ans = ['' for _ in range(8)]
ri = 0
ni = 0
use = False
while ni < 8:
    padding_cnt = 4 - len(raw[ri])
    if not padding_cnt:
        ans[ni] = raw[ri]
    elif padding_cnt != 4:
        ans[ni] = '0' * padding_cnt + raw[ri]
    else:
        if use:
            ri += 1
            continue

        prv = ni
        while ni <= prv + diff - 1:
            use = True
            ans[ni] = '0000'
            ni += 1

        ri += 1
        continue
    
    ni += 1
    ri += 1

print(':'.join(ans))