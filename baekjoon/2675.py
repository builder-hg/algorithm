"""
구현
1. 테스트 케이스 입력
2. 글자를 순회하며 R번 곱하여 출력한다.
"""
import sys
input = sys.stdin.readline

Q = int(input())
while Q:
    Q -= 1

    R, alpha = input().split()
    R = int(R)
    for elem in alpha:
        print(elem*R, end="")
    print()