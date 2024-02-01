"""
1. 완전탐색으로 접근한다면,
- 확인해볼 수 M개에 대해, 각각 상근이홀더에 있는지 확인한다. (M * N)
- M개는 확인해야하고(더 줄일 수 없고) 상근이 홀더에 있는지 확인하는 횟수를 줄여보자.

2.최적화하기, 홀더에 있는지 이진탐색으로 후보군을 줄여가면서 확인한다.
3. 


"""
import sys
input = sys.stdin.readline

N = int(input())
hasCard = sorted(list(map(int, input().split())))
M = int(input())
judgeCard = list(map(int, input().split()))

for i in judgeCard:
    ans = 0
    left = 0    # 찾고자 하는 값 중 가장 왼쪽에 위치한 인덱스
    right = -1   # 찾고자 하는 값 중 가장 오른쪽에 위치한 인덱스
                # 찾고자 하는 값이 없는 경우 -1에 1이 더해져 0이 나오게끔한다.

    # 가장 왼쪽에 위치한 인덱스 구하기
    s = 0
    e = N - 1
    while s <= e:
        mid = (s + e) // 2
        if hasCard[mid] == i:
            left = mid
            e = mid - 1
        elif hasCard[mid] < i:
            s = mid + 1
        else:
            e = mid - 1
    
    # 가장 오른쪽에 위치한 인덱스 구하기
    s = 0
    e = N - 1
    while s <= e:
        mid = (s + e) // 2
        if hasCard[mid] == i:
            right = mid
            s = mid + 1
        elif hasCard[mid] < i:
            s = mid + 1
        else:
            e = mid - 1

    ans = right - left + 1
    print(ans, end=" ")