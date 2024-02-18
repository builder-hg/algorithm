import sys
input = sys.stdin.readline

K = input().rstrip()
matching = {
    '0':0,'1':1, '2': 2,'3': 3, '4': 4, '5': 5,'6':6,'7':7,'8':8,'9':9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

length = len(K)
cnt = 0
ans = 0
for i in range(length - 1, -1, -1):
    ans += (matching[K[i]] * (16 ** cnt))
    cnt += 1

print(ans)