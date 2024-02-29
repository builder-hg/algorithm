import sys
input = sys.stdin.readline

raw = list(input().strip())

if raw == ['0']:
    print(0)
    sys.exit()
    
ans_lst = []
for i in range(len(raw)):
    num = int(raw[i])
    temp = []
    while num:
        temp.append(num % 2)
        num //= 2
    temp = temp[::-1]
    if i == 0:
        ans_lst.append(temp)
    else:
        leng = len(temp)
        required = 3 - leng
        bump = []
        for _ in range(required):
            bump.append(0)
        for j in range(leng):
            bump.append(temp[j])
        ans_lst.append(bump)

for i in range(len(ans_lst)):
    for j in range(len(ans_lst[i])):
        print(ans_lst[i][j], end="")