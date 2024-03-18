import sys
input = sys.stdin.readline

N = int(input())
cnt = 1
remainder = N % 10
share = N // 10
new_number = (remainder * 10) + ((share + remainder) % 10)


while True:
    if new_number == N:
        break

    remainder = new_number % 10
    share = new_number // 10
    new_number = (remainder * 10) + ((share + remainder) % 10)

    cnt += 1

print(cnt)