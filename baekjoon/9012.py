import sys
input = sys.stdin.readline

arr = list(input().strip())
lst = []
for i in range(len(arr)):
    if arr[i] == '(':
        lst.append(i)
    else:
        print(lst.pop())

"""import sys
input = sys.stdin.readline

arr = list(input().strip())
check = [True for _ in range(len(arr))]
cnt = 0

for i in range(len(arr)):
    if arr[i] == ')':
        check[i] = False

        for j in range(i-1, -1, -1):
            if check[j] == False:
                continue

            print(i, '의 짝은', j,'이다.')
            check[j] = False
            break
"""


"""import sys
input = sys.stdin.readline

Q = int(input())
while Q:
    Q -= 1
    arr = list(input().strip())
    cnt = 0

    for i in range(len(arr)):
        if arr[i] == ')':
            cnt -= 1
        else:
            cnt += 1

        if cnt < 0:
            break
        
    if cnt != 0:
        print("NO")
    else:
        print("YES")"""