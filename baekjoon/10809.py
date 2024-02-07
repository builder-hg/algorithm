import sys
input = sys.stdin.readline
alpha ='abcdefghijklmnopqrstuvwxyz'
text = list(input())

for elem in alpha:
    if elem not in text:
        print(-1, end=" ")
        continue
    print(text.index(elem), end=" ")