def calculate_scores(N, cards):
    scores = [0] * N  # 각 플레이어의 점수를 저장할 리스트 초기화

    for i in range(N):  # 모든 플레이어에 대해 결투를 진행
        for j in range(N):
            if i == j:  # 같은 플레이어끼리는 결투를 하지 않음
                continue
            if cards[j] % cards[i] == 0:  # 현재 플레이어의 카드로 다른 플레이어의 카드를 나누어 떨어지는 경우
                scores[i] += 1  # 현재 플레이어의 점수 1 증가
            elif cards[i] % cards[j] == 0:  # 다른 플레이어의 카드로 현재 플레이어의 카드를 나누어 떨어지는 경우
                scores[j] += 1  # 다른 플레이어의 점수 1 증가

    return scores

# 입력 받기
N = int(input())  # 플레이어의 수
cards = list(map(int, input().split()))  # 각 플레이어가 가지고 있는 카드에 적힌 수

# 점수 계산
scores = calculate_scores(N, cards)

# 결과 출력
print(*scores)