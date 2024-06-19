"""
1 2 3
=> 1, 2, 3, 4, 5, 6
7을 만들기 위해서는 total + 1의 값이 추가되어야 한다.

1 2 3 7
=> 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
14를 만들기 위해서는 total + 1의 값인 14가 추가되어야 한다.

1 5 7
=> 1, 5, 6, 7, 8, 12, 13
"""
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

total = 1
for val in arr:
    if total < val:
        break
        
    total += val

print(total)