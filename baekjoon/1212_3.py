import sys
input = sys.stdin.readline

arr = input().strip()
val = ''

for i in range(1, len(arr) + 1):
    unit = ''
    
    share = int(arr[i - 1])
    # 2진수로 변환
    while share > 1:
        unit = str(share % 2) + unit
        share //= 2
    unit = str(share) + unit

    cnt = 3 - len(unit)
    if i == 1:
        val += unit
    else:
        val += ('0' * cnt + unit)

print(val)