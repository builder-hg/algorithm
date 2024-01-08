"""
문제풀이전략

1 문제 이해 및 정리
- 여학생 : N, 남학생 : M, 제외인원 :K
- 2명의 여학생과 1명의 남학생 팀
- 최대 팀 수 구하기

2 문제 풀이 방향
- 주어진 여학생의 수를 2로 나눴을 때의 몫을 a라고 한다.
- 여학생 혹은 남학생의 수를 1씩 감소시키며 k번 만큼 반복한다.
- 여학생 수가 2보다 작거나 남학생 수가 1보다 작으면 0을 출력하고 종료한다.
1) 몫 a < 남학생 수
>> 남학생 수를 1 감소시킨다.
2) 몫 a >= 남학생 수
>> 여학생 수를 1감소시킨다.
3) 위 작업을 끝낸 후, 남은 여학생이 팀을 꾸릴 수 있는 개수와 남은 남학생이 팀을 꾸릴 수 있는 개수를 비교하여 작은 수를 출력한다.
"""
import sys

girls, boys, excpetNum = map(int, sys.stdin.readline().split())

for _ in range(excpetNum):
    if girls < 2 or boys < 1:
        print(0)
        sys.exit()
    if (girls // 2 < boys):
        boys -= 1
    else:
        girls -= 1

capableGirls = girls//2
capableBoys = boys
print(min(capableGirls, capableBoys))

