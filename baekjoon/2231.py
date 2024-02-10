"""
어떤수 k + k의 각 자리수 합이 = N이 되도록 하는 가장 작은 k를 구하라.
0. 완전탐색
1부터 1000000까지 순회하며 합이 N이 되는 값 k를 찾는다.
"""
import sys
input = sys.stdin.readline

N = int(input())
for i in range(1, 1000001):
    val = i
    lst = list(str(i).strip())
    for j in range(len(lst)):
        val += int(lst[j])
    
    if val == N:
        print(i)
        sys.exit()

print(0)