"""
[완전탐색]
1. 세 수를 곱한다.
2. 세 수를 한자리씩 분해한다. 
    - str로 되는지 확인해본다.
3. 딕셔너리에 저장하여 카운팅한다.
"""
import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

total = A * B * C
arr = list(str(total))
num_dict = {}
for i in range(len(arr)):
    elem = arr[i]
    num_dict[elem] = num_dict.get(elem, 0) + 1
for i in range(10):
    val = num_dict.get(str(i), 0)
    print(val)