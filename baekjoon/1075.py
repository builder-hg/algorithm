import sys
input = sys.stdin.readline

N = input().strip()
temp = N[:-2] + '00'
num = int(temp)
K = int(input())
mid = num // K

if num % K == 0:
    print(str(num)[-2:])
else:
    print(str(K * (mid+1))[-2:])