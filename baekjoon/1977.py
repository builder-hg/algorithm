
import sys
input = sys.stdin.readline

start = int(input())
end = int(input())
arr = [0 for _ in range(10001)]
cnt = 0
total = 0
min_value = 0

# 제곱수 저장하기
for i in range(1, 10001):
    if i * i > 10001:
        break
    
    arr[i * i] += 1

# 완전제곱수 카운팅
for i in range(start, end + 1):
    if arr[i] == 0:
        continue

    if cnt == 0:
        min_value = i
    
    cnt += 1
    total += i

if cnt == 0:
    print(-1)
    sys.exit()

print(total)
print(min_value)