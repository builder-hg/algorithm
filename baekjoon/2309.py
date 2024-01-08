"""
문제풀이전략

1. 문제 이해 및 정리
- 아홉명의 키가 주어진다.
- 주어진 키는 100을 넘지않는 자연수다.
- 키는 서로 다르다.
- 일곱명의 키의 합이 100인 경우를 출력한다.
- 정답이 여러 가지인 경우 아무거나 출력한다.
- 정답을 오름차순으로 출력한다.

2. 문제 풀이 방향
1) 아홉명의 키를 모두 더한다.
2) 모두 더한 합에서 100을 빼 차이값을 구한다.
3) 두 사람의 키의 합이 차이값이 되는 경우를 구한다.
4) 해당되는 사람들을 뺀 나머지 사람들의 키를 출력한다.
"""
import sys

heightList = []
for _ in range(9):
    heightList.append(int(input()))

difference = sum(heightList) - 100
for i in range(len(heightList) - 1):
    for j in range(i + 1, len(heightList)):
        if heightList[i] + heightList[j] == difference:
            delA = heightList[i]
            delB = heightList[j]
            heightList.remove(delA)
            heightList.remove(delB)
            print(*sorted(heightList))
            sys.exit()