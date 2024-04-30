import sys
input = sys.stdin.readline

while True:
    arr = input().rstrip('\n')

    if not arr:
            break

    a, b, c, d = 0, 0, 0, 0  #  소문자, 대문자, 숫자, 공백의 개수
    for i in arr:
        now = ord(i)

        if now == 32:
            d += 1
        elif now >= 48 and now <= 57:
            c += 1
        elif now >= 65 and now <= 90:
            b += 1
        elif now >= 97 and now <= 122:
            a += 1

    print(a, b, c, d)