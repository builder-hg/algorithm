import sys
input = sys.stdin.readline

stack = []
"""
[a, b, c], '+' stack에 넣는다.
열린 괄호를 만나면 stack에 넣는다.
닫힌 괄호를 만날때까지 stack에 넣는다.
닫힌 괄호를 만나면 열린괄호를 제거할 때 까지 연산한다.
"""