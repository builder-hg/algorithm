"""
구현
1. 초깃값 index 0, index 1 비교하여 ascending, descending 설정
2. 1부터 N까지 순회하며 중간에 타입이 달라진다면 mixed 설정, 바뀌지 않는다면 초깃값 출력
"""
import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))
init_value = ''
if arr[0] < arr[1]:
    init_value = 'ascending'
else:
    init_value = 'descending'

for i in range(2, 8):
    temp = ''
    if arr[i] > arr[i-1]:
        temp = 'ascending'
    else:
        temp = 'descending'

    if init_value != temp:
        print("mixed")
        sys.exit()

print(init_value)