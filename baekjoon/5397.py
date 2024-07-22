import sys
input = sys.stdin.readline

T = int(input())
while T:
    T -= 1

    raw = list(map(str, input().strip()))
    stackA = []
    stackB = []
    for i in range(len(raw)):
        if raw[i] == '<':
            if not len(stackA):
                continue

            stackB.append(stackA.pop())
        elif raw[i] == '>':
            if not len(stackB):
                continue

            stackA.append(stackB.pop())
        elif raw[i] == '-':
            if not len(stackA):
                continue
            stackA.pop()
        else:                   # 알파벳 대문자, 소문자, 숫자
            stackA.append(raw[i])

    print("".join(stackA), "".join(stackB[::-1]), sep="")