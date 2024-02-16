import sys
input = sys.stdin.readline().rstrip

text = input()
cnt = 0

def check(arr):
    lstA = arr[:]
    lstB = arr[::-1]

    if lstA == lstB:
        return True
    else:
        return False

for i in range(len(text)):
    arr = text[i:]
    if check(arr): # 펠린드롬이라면
        break
    cnt += 1

print(len(text) + cnt)