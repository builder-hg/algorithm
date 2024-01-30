"""
아이디어
1. 가장 높은 값의 인덱스를 구한다.
2. 해당 인덱스의 양 옆으로 prefix의 값과 suffix의 값 그리고  그 차액을 누적하여 더한 값을 출력한다.

"""
import sys
input = sys.stdin.readline

H, W = map(int, input().split())
raw = list(map(int, input().split()))
maxHeight = max(raw)
maxHeightIndex = raw.index(maxHeight)
prefix = [0 for _ in range(W)]
suffix = [0 for _ in range(W)]
# prefix와 suffix를 구할 때 항상 헷갈린다. 양 옆에 패딩으로 0을 주는 부분이 헷갈린다.
prefix[0] = raw[0]
suffix[W-1] = raw[W-1]
valA = 0
valB = 0

for i in range(1, maxHeightIndex):
    if prefix[i-1] >= raw[i]:
        valA += (prefix[i-1] - raw[i])
        prefix[i] = prefix[i-1]
    else:
        prefix[i] = raw[i]
for i in range(W-2, maxHeightIndex, -1):
    if suffix[i+1] >= raw[i]:
        valB += (suffix[i+1] - raw[i])
        suffix[i] = suffix[i+1]
    else:
        suffix[i] = raw[i]
print(valA + valB)