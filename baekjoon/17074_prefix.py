import sys
input = sys.stdin.readline

N = int(input())
raw = list(map(int, input().split()))
ans = 0

prefix = [False for _ in range(N)]
suffix = [False for _ in range(N)]
prefix[0] = True
suffix[N-1] = True

for i in range(1, N):
    if prefix[i-1] == False:
        prefix[i] = False
        continue

    if raw[i-1] > raw[i]:
        prefix[i] = False
    else:
        prefix[i] = True

for i in range(N-2,0,-1):
    if suffix[i+1] == False:
        suffix[i] = False
        continue

    if raw[i+1] < raw[i]:
        suffix[i] = False
    else:
        suffix[i] = True

if N == 2:
    print(N)
    sys.exit()

for i in range(1, N):
    if i == 1 and suffix[i+1]:
        ans += 1
        continue
    if i == N-1 and prefix[i-1] == True:
        ans += 1
        break
    if prefix[i-1] == True and suffix[i+1] == True and raw[i-1] <= raw[i+1]:
        ans += 1

print(ans)

# import sys
# input = sys.stdin.readline

# N = int(input())
# raw = [0] + list(map(int, input().split()))
# upsideA = 0
# tempA = 0
# upsideB = 0
# tempB = 0
# cnt = 0

# prefix = [0 for _ in range(N+1)]
# suffix = [0 for _ in range(N+1)]
# suffix[N] = raw[N]

# for i in range(1, N+1):
#     if upsideA >= 2:
#         print(0)
#         sys.exit()

#     if prefix[i-1] > raw[i]:
#         upsideA += 1
#         tempA += 1
#         prefix[i] = prefix[i-1]
#     else:
#         prefix[i] = raw[i]

# if upsideA == 0:
#     cnt += N
# else:
#     cnt += tempA

# for i in range(N-1,0,-1):
#     if upsideB >= 2:
#         print(0)
#         sys.exit()

#     if suffix[i+1] < raw[i]:
#         upsideB += 1
#         tempB += 1
#         suffix[i] = suffix[i+1]
#     else:
#         suffix[i] = raw[i]

# if suffix != prefix and upsideB == 0:
#     cnt += N
# else:
#     cnt += tempB

# print(cnt)