"""
A                            0         0       1
B                             1        1        0
BA                           2         1        1
BAB                         3         2        1
BABBA                      4        3           2
BABBABAB                 5         5         3
BABBABABBABBA         6        8           5
"""
import sys
input = sys.stdin.readline

K = int(input())
B = [0 for _ in range(46)]
A = [0 for _ in range(46)]

B[0], B[1] = 0, 1
A[0], A[1], A[2] = 1, 0, 1

for i in range(2, 46):
    B[i] = B[i - 2] + B[i - 1]

for i in range(3, 46):
    A[i] = A[i - 2] + A[i - 1]

print(A[K], B[K])