import sys
input = sys.stdin.readline

N = int(input())
order = []
for i in range(N):
    num = int(input())
    order.append(num)

num = 1
stack = []
op = []
flag = True
for i in range(N):      # order 순회
    while num <= order[i]:  # stack에 push하는 과정
        stack.append(num)
        op.append('+')
        num += 1

    if stack[-1] == order[i]:   # stack에 pop하는 과정, 
        stack.pop()
        op.append('-')
    else:
        flag = False
        break

if not flag:
    print("no")
else:
    for i in range(len(op)):
        print(op[i])
















"""
0. 문제 이해
- 1부터 N까지 순서대로 push할 수 있다.
1. 구현/설계
- 1부터 N까지 순회한다.
- 필요한 값이 stack에 있다면 나올 때 까지 pop한다.
- 필요한 값이 stack에 없다면 i를 push한다.
    만약 push할 값들 중 필요한 값이 존재하지 않는다면 NO를 출력한다.
- push, pop에 대한 연산을 기록한다.  

1-2. 완전탐색 재설계
1) stack에 들어갈 값은 1부터 N까지 1씩 증가하여 들어간다.
2) stack에 들어간 값을 다시 빼낸다.
3) 만들어야 할 수열[idx] 값에 따라 1) 을 반복할지 2)를 반복할지 선택한다.
- 만들어야할 수열의 값이 stack의 마지막에 들어와있는지 확인한다.(stack[-1] == 수열[idx])
- num = 1일때 만들어야할 수열의 값은 4이므로 num=1,2,3,4까지 증가하여 stack에 쌓인다. (연산 +)
- 만들어야할 수열의 값이 stack의 마지막에 들어와있다면 해당 값을 stack에서 제거한다. (연산 -)
- idx를 1 증가시킨다.
4) 만약, idx =1이고 num = 5, 수열[idx] = 3이라면,
num > 수열[idx]보다 크므로 stack에 해당 값이 들어있을수 있으므로 빼내준다.


import sys
input = sys.stdin.readline

N = int(input())
required = []
stack = []
calc = []
res = []
num = 1
idx = 0

for _ in range(N):
    i = int(input())
    required.append(i)

while num <= N+1:
    if idx == N:
        break
    if num <= required[idx]:
        stack.append(num)
        calc.append('+')
        num += 1
        continue
    
    
    if stack[-1] == required[idx]:
        res.append(stack.pop())
        calc.append('-')
        idx += 1
    else:
        print("NO")
        sys.exit()

for i in range(len(calc)):
    print(calc[i])
"""
