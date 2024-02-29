import sys
input = sys.stdin.readline

K, N = map(int, input().split())
arr = sorted(input().split())
ans = [0 for _ in range(K)]

def get_cnt(x):
    if x in 'aeiou':
        return 1, 0
    else:
        return 0, 1

def recur(cur, cnt, vowels, consonant):
    if cnt == K:
        if vowels < 1 or consonant < 2:
            return 

        print(*ans, sep="")
        return
    
    if cur == N:
        return
    
    cnt_vowels, cnt_consonant = get_cnt(arr[cur])

    ans[cnt] = arr[cur]
    recur(cur + 1, cnt + 1, vowels + cnt_vowels, consonant + cnt_consonant)
    recur(cur + 1, cnt, vowels, consonant)

recur(0, 0, 0, 0)