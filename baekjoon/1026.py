"""
정렬된 A, 정렬된 B, 원본 B, 매핑 딕셔너리

5
1 1 1 6 0
2 7 8 3 1
"""
import sys
input = sys.stdin.readline

N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse=True)

total = 0
for i in range(N):
    total += A[i] * B[i]

print(total)

# _dict = {} 
# for i in range(N):
#     _key = sorted_B[i]
#     if _dict.get(_key, 0) != 0:
#         _dict[_key].append(sorted_A[i])
#     else:
#         _dict[_key] = [sorted_A[i]]

# print(_dict)