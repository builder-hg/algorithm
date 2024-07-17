import sys
input = sys.stdin.readline

def recur(cur, start):
    if cur == N:
        tmp = 0
        for item in log[:N]:
            tmp += dic[item]
        ans.append(tmp)
        return
    
    for i in range(start, len(raw)):
        log[cur] = raw[i]
        recur(cur + 1, i)

N = int(input())
raw = ['I', 'V', 'X', 'L']
log = ['' for _ in range(N)]
ans = []
dic = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50
}
recur(0, 0)

ans = list(set(ans))
print(len(ans))