"""
0 1 2  3 4  5  6  7 8 9
(  (  (  (  )  )  (  (  )  )
(  (  )  (  )  )  (  (  )  )
(  (  (  (  )  )  )  (  )  )
(  (  (  (  )  )  (   ) )  )
(  )  (  (  )  )  (  (  )  )

"""
import sys
input = sys.stdin.readline().rstrip

bracket = input()
open_cnt = 0
close_cnt = 0
open_stack = []
close_stack = []
open_prefix = [0 for _ in range(len(bracket))]
close_prefix = [0 for _ in range(len(bracket))]

for i in range(len(bracket)):
    if bracket[i] == '(':
        open_cnt += 1
        open_stack.append(i)
    else:
        close_cnt += 1
        if open_stack:
            open_stack.pop()
        else:
            close_stack.append(i)

    open_prefix[i] = open_cnt
    close_prefix[i] = close_cnt

# print(open_stack)
# print(open_prefix)
# print(close_prefix)

if open_cnt - close_cnt > 0:
    idx = open_stack[-1]
    print(open_cnt - open_prefix[idx] + 1)
elif open_cnt - close_cnt < 0:
    idx = close_stack[0]
    print(close_prefix[idx])
else:
    print(0)