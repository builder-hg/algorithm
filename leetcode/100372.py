"""
N = 14, K = 13
1110, 1101

* 1을 0으로 변경할 수 있다.

풀이방법
01. 모두 2진수로 변경한다.
02. 전체를 순회하며 목표지점이 0이고 대상이 1이면 변경하고 횟수를 더한다.
   만약 목표지점이 1인데 대상이 0이면 -1을 출력한다.
"""
N = 14
K = 13

def getBinary(val):
    ret = ''
    while val // 2:
        r = val % 2
        ret += str(r)
        val = val // 2

    if val:
        ret += str(val)

    return ret[::-1]

now = getBinary(N)
target = getBinary(K)

if len(now) >= len(target):
    diff = len(now) - len(target)
    target = '0' * diff + target
else:
    print(-1)

ans = 0
leng = len(now)
for i in range(leng):
    if now[i] == '0' and target[i] == '1':
        print(-1)
        break
    
    if now[i] == '1' and target[i] == '0':
        ans += 1

print(ans) 