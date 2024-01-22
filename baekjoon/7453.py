"""
[문제풀이전략]
1. 문제 이해 및 정리
- 크기 N (1<= N <= 4,000) 의 배열 4개가 주어진다.
- 배열 4개 중 원소 하나씩 골라서 그 합이 0이 되는 쌍의 개수를 구한다.

2. 팁
- 조를 2개로 만들어보기
    이 때 만들어지는 조의 크기는 n ** 2 쯤이다. 
- 중복에 대해서 생각해본다.

3. 아이디어
groupA, groupB에서 나올 수 있는 모든 합을 구한다. O(n^2)
groupC, groupD에서 나올 수 있는 모든 합을 구한다. O(n^2)
이 두 합(1이상 16,000,000이하)을 또 서로 순회하면서 0이되는 쌍을 구한다. 
O(n^2)


4. 문제 풀이 방향
"""
import sys

N = int(input())
lstA = []
lstB = []
lstC = []
lstD = []
for _ in range(N):
    a, b, c, d = map(int, sys.stdin.readline().split())
    lstA.append(a)
    lstB.append(b)
    lstC.append(c)
    lstD.append(d)


union_1 = []
union_2 = []
zero_1 = 0
zero_2 = 0

for i in range(N):
    for j in range(N):
        # union_1에 담긴 음수는 A와 B그룹에서 고른 친구들로 이루어진다.
        # union_1에 담긴 양수는 C와 D그룹에서 고른 친구들로 이루어진다.
        if lstA[i] + lstB[j] < 0:
            union_1.append(lstA[i] + lstB[j])
        elif lstA[i] + lstB[j] > 0:
            union_2.append(lstA[i] + lstB[j])
        else:
            zero_1 += 1
        # union_2에 담긴 음수는 C와 D 그룹에서 고른 친구들로 이루어진다.
        # union_2에 담긴 양수는 A와 B그룹에서 고른 친구들로 이루어진다.
        if lstC[i] + lstD[j] < 0:
            union_2.append(lstC[i] + lstD[j])
        elif lstC[i] + lstD[j] > 0:
            union_1.append(lstC[i] + lstD[j])
        else:
            zero_2 += 1
            
union_1.sort()
union_2.sort()


s = 0
e = len(union_1) - 1 
cnt_1 = 0
while s < e:
    if union_1[s] + union_1[e] == 0:

        # 중복된 구간 체크해서 건너뛰기 
        next_s = s+1
        double_s_cnt = 1
        while union_1[next_s] == union_1[s] and next_s < len(union_1):
            double_s_cnt += 1
            next_s += 1
    
        next_e = e-1
        double_e_cnt = 1
        while union_1[next_e] ==union_1[e] and next_e >= 0:
            double_e_cnt += 1
            next_e -= 1
        cnt_1 += (double_s_cnt * double_e_cnt)

        s = next_s
        e = next_e
    elif union_1[s] + union_1[e] < 0:
        s += 1
    else:
        e -= 1

x = 0
y = len(union_2) - 1 
cnt_2 = 0
while x < y:
    if union_2[x] + union_2[y] == 0:

        # 중복된 값이 있다면 답에 카운팅해주고 건너뛰어보장
        next_x = x + 1
        temp_cnt_x = 1
        while union_2[next_x] == union_2[x] and next_x < len(union_2):
            temp_cnt_x += 1
            next_x += 1 
        next_y = y - 1
        temp_cnt_y = 1
        while union_2[next_y] == union_2[y] and next_y >= 0 :
            temp_cnt_y += 1
            next_y -= 1

        cnt_2 += (temp_cnt_x * temp_cnt_y)

        x = next_x
        y = next_y
    elif union_2[x] + union_2[y] < 0:
        x += 1
    else:
        y -= 1

print(cnt_1 + cnt_2 + zero_2 * zero_1)