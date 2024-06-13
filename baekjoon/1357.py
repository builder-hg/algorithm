import sys
input = sys.stdin.readline

def rev(k):
    ret = 0
    tmp = k
    lst = []
    """
    123 % 10 = 3, cnt = 1
    12 % 10 = 2, cnt = 2
    1 % 10 = 1, cnt = 3 # cnt는 자릿수
    """
    while tmp:
        lst.append(tmp % 10)
        tmp //= 10

    flag = False
    cnt = 0
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == 0 and not flag:
            continue
        if not flag and lst[i] != 0:
            flag = True
        
        ret += lst[i] * (10 ** cnt)
        cnt += 1

    return ret 

A, B = map(int, input().split())
retA = rev(A)
retB = rev(B)
ans = rev(retA + retB)
print(ans)