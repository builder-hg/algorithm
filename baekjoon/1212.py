# 6
import sys
input = sys.stdin.readline

text = input().rstrip()
lst = []
ans = ''

for i in range(len(text)-1, -1, -1):
    num = int(text[i])
    rest = num
    temp =''

    while rest:
        temp += str(rest % 2)
        rest //= 2
    
    temp = temp[::-1]
    if len(temp) < 3:
        temp = (3 - len(temp)) * '0' + temp
        lst.append(temp)
        continue
    lst.append(temp)
    
for i in range(len(lst)-1, -1, -1):
    ans += lst[i]

if ans[0] == '0':
    print(ans[1:])
else:
    print(ans)

