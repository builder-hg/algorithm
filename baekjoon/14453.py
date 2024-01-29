"""
[문제풀이전략]
- '언제, 어떤 제스쳐로 바꿔야하는가'
- P(보): S(가위), S(가위): H(묵), H(묵) : P(보)
- 가장 큰 답은 N이다.
ex)
P P H P S
    i
i지점에 위치한 요소의 카운터제스처가 이전에 몇 개 있었는지 센다.
- 고민하고 있는 점 : 어떤 지점에서 제스쳐를 바꾸는게 답을 최대로 만들 수 있는가?
- i지점까지 H를 고려했을 때, N-i개에 대해서 S 혹은 P로 이기는 수를 구한다.
- i를 1부터 N까지 증가시키며 가장 큰 값을 고른다.
"""
import sys

N = int(input())
ans = -1
raw = [0]
prefixH = [0 for _ in range(N+1)]
prefixS = [0 for _ in range(N+1)]
prefixP = [0 for _ in range(N+1)]
cntH = 0
cntS = 0
cntP = 0

for i in range(1,N+1):
    alpha = input()
    raw.append(alpha)
    if alpha == 'H':
        cntH += 1
    elif alpha == 'S':
        cntS += 1
    else:
        cntP += 1
    
    prefixH[i] = cntH
    prefixS[i] = cntS
    prefixP[i] = cntP

for i in range(1, N+1):
    # H를 고른다면,
    tempH = prefixH[i]
    tempHS = prefixS[N] - prefixS[i] 
    tempHP = prefixP[N] - prefixP[i]
    ans = max(ans, tempH + tempHS)
    ans = max(ans, tempH + tempHP)
    # S를 고른다면, 
    tempS = prefixS[i]
    tempSH = prefixH[N] - prefixH[i] 
    tempSP = prefixP[N] - prefixP[i]
    ans = max(ans, tempS + tempSH)
    ans = max(ans, tempS + tempSP)
    # P를 고른다면, 
    tempP = prefixP[i]
    tempPS = prefixS[N] - prefixS[i] 
    tempPH = prefixH[N] - prefixH[i]
    ans = max(ans, tempP + tempPS)
    ans = max(ans, tempP + tempPH)

print(ans)

# print(prefixH)
# print(prefixS)
# print(prefixP)

