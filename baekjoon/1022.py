"""
최대한 범위의 수는 9876543210이다.
살펴볼 수 있는 자리수는 1의 자리수부터 10의 자리수까지이다.
감소하는 숫자를 조합으로 구한다. 자릿수: n, 1 <= n <= 10 
"""
import sys
input = sys.stdin.readline

def combination(arr, k):    # 조합할 대상, 선택 개수
    visited = [False for _ in range(len(arr))]

    ret = []
    def generate(chosen):
        if len(chosen) == k:    # 종료조건
            ret.append([*chosen])
            return 
        
        if chosen:
            s = arr.index(chosen[-1]) + 1
        else:
            s = 0

        for i in range(s, len(arr)):
            if visited[i]:
                continue

            visited[i] = True
            chosen.append(arr[i])
            generate(chosen)

            visited[i] = False
            chosen.pop()

    generate([])
    return ret

N = int(input())

arr = []
for i in range(1, 11):  # i는 감소하는 수의 자릿수이다.
    lst = combination([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], i)
    for item in lst: 
        num = ''.join(list(map(str, item)))
        arr.append(int(num))

arr.sort()
if N >= len(arr):
    print(-1)
else:
    print(arr[N])


"""
1.완전탐색

import sys
input = sys.stdin.readline

N = int(input())

arr = []
for i in range(9876543210):
    next = False

    if not (i // 10):
        arr.append(i)
        continue

    prv = i % 10
    cur = i // 10
    while cur:
        if cur <= prv:
            next = True
            break

        prv = cur % 10
        cur //= 10
    
    if next:
        continue

    arr.append(i)

if N >= len(arr):
    print(-1)
else:
    print(arr[N])
"""
