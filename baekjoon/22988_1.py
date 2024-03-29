"""
[문제풀이전략]
0. 문제 이해
- X만큼 차있는 것들은 따로 개수를 세놓고 수열에서 지운다. (X 미만인 것들만 있을때 잘 합치도록 한다.)

1. 테스트케이스
3 10
5 0
10
-> 1개

4 10
0 0 0 0
5 0 0
10 0
10
-> 1개

5 10
0 0 0 0 0
5 0 0 0
10 0 0
10 5
10 
-> 1개 

6 10
0 0 0 0 0 0
5 0 0 0 0
10 0 0 0
10 5 0
10 10
-> 2개

2. 테스트케이스를 통한 특징 관찰
- 용량의 가장 작은 값인 0을 넣어 관찰한 결과, 
    용기 3개로 꽉 찬 헤어에센스 용기 한 개를 만들 수 있다는 사실을 알아냈다.
- 연산의 특징을 통해 다음과 같이 접근할 수 있다.
    용기 두 개를 합쳐서 완성 가능한 애들은 최대한 합치도록 한다.
    나머지는 마구잡이로 세개씩 잡아서 교환하면 완제품이 된다.
    즉, 두개씩 매칭 가능한 쌍을 최대한 많이 만드는 문제로 변형되는 것이다.

3. 예제 이해
7 13
0 1 2 3 5 8 13
- 완제품인 13은 수열에서 제외한다. cnt를 1 증가시킨다.
- 제품 두개로 완제품을 만들 수 있는 경우를 확인한다.
    5, 8을 제외한다. cnt를 1 증가시킨다.
- 제품을 세개씩 묵느다.

4. 설계
1) 완전탐색
- 리스트를 2중으로 순회한다. 리스트의 총 길이를 leng에 담는다. 
- 원소의 값이 K인 경우 leng을 1 감소시키고 cnt를 1 증가시킨다.
- 2중으로 순회하며 두 개의 원소가 K//2 이상인 경우 leng을 2 감소시키고 cnt를 1증가시킨다.
- 남은 leng을 3으로 나누어 몫을 구한다.
- 구한 몫 + cnt를 출력한다.
2) 투포인터
- 리스트를 2중으로 순회하면 100,000 * 100,000으로 시간초과가 난다 -> 최적화
- 리스트를 오름차순으로 정렬한다.
- 두 개의 포인터(s, e)를 제일 앞, 제일 뒤에 두고 이동시킨다.
- 두 수의 합이 K//2이상인 경우를 찾아서 카운팅한다. leng -= 2
- 이 때 특정 수의 값이 K이면 카운팅하고 leng에서 그 수만큼 차감 후 포인터를 이동시킨다.
- 남은 leng을 3으로 나누어 몫을 구한다.
- 구한 몫 + cnt를 출력한다.
"""
import sys

N, K = map(int, sys.stdin.readline().split())
lst = sorted(list(map(int, sys.stdin.readline().split())))
s = 0
e = N-1
cnt = 0
leng = N

if s == e :
    if lst[s] == K:
        cnt += 1

while s < e:
    if lst[s] == K:
        cnt += 1
        leng -= 1
        s += 1

        if s == e and lst[e] == K:
            cnt += 1
            leng -= 1

        continue
    if lst[e] == K:
        cnt += 1
        leng -= 1
        e -= 1

        if s == e and lst[s] == K: 
            cnt += 1
            leng -= 1
        continue
    if lst[s] + lst[e] >= K/2:
        cnt += 1
        leng -= 2
        s += 1
        e -= 1
    else:
        s += 1
    
ans = cnt + (leng // 3)
print(ans)