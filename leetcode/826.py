difficulty = [2,4,6,8,10]
profit = [10,20,30,40,50]
worker = [4,5,6,7]

lst = [[0, 0]]
for i in range(len(difficulty)):
    lst.append([difficulty[i], profit[i]])
lst.sort()  # 작업난이도 순으로 정렬

for i in range(len(lst) - 1):   # lst의 profit 값 재정의
    lst[i + 1][1] = max(lst[i][1], lst[i+1][1])       # 해당 난이도보다 쉬운 난이도 내에 존재하는 이윤 중 큰 값을 저장한다.


ans = 0
for i in range(len(worker)):
    s = 0
    e = len(lst) - 1

    while s <= e:
        mid = (s + e) // 2

        if lst[mid][0] > worker[i]:
            e = mid - 1
        else:
            tmp = lst[mid][1]
            s = mid + 1

    ans += tmp

print(ans)
"""
# 이진탐색과 완전탐색 결합, 시간초과

lst = []
for i in range(len(difficulty)):
    a, b = difficulty[i], profit[i]
    lst.append([a, b])
lst.sort()

print(lst)

ans = 0
for i in range(len(worker)):
    nth = -1
    s = 0 
    e = len(lst) - 1
    while s <= e:
        mid = (s + e) // 2

        if lst[mid][0] > worker[i]:
            e = mid - 1
        else:
            nth = mid
            s = mid + 1

    if nth == -1:
        ans += 0
    else:
        ans += max(lst[:nth + 1], key= lambda x:x[1])[1]

print(ans)
"""

"""
# 완전탐색, 시간초과
ans = 0
for i in range(len(worker)):
    for j in range(len(lst)):
        if lst[j][1] > worker[i]:
            continue

        ans += lst[j][0]
        break

print(ans)
"""