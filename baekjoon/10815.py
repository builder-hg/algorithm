"""
완전탐색부터 고려하자.
1) 확인할 수 하나하나씩 주어진 수열에 있는지 없는지 한번씩 확인한다. (N * M = 250,000,000,000)
    - 수열을 순회한다(N)
    - 주어진 수 하나하나 살펴본다(M)

최적화하기, 주어진 수 하나하나 살펴보지 않는다. => 이진탐색을 한다.
- 수열들을 정렬한다. 
- 길이가 M인 수열의 정중앙에 위치한 값을 구한다. (mid = (s + e) // 2, hasCard[mid])
"""
import sys
input = sys.stdin.readline

N = int(input())
hasCard = sorted(list(map(int, input().split())))
M = int(input())
judgeCard = list(map(int, input().split()))

for i in judgeCard:
    ans = 0
    s = 0
    e = N - 1
    while s <= e:
        mid = (s + e) // 2
        if hasCard[mid] == i:
            ans = 1
            break
        elif hasCard[mid] < i:
            s = mid + 1
        else:
            e = mid - 1

    print(ans, end=" ")