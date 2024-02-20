"""
0. 문제이해
- 캔의종류 N, 일수 K
- can은 종류별 캔의 개수(i, 인덱스가 캔의 종류이다.)
- range_arr, 캔에 대한 선호도
- marry_arr, 캔에 대한 선호도
- 하루마다, 고양이한테 캔을 줄 때마다 can의 개수를 줄여나간다.

1. 풀이전략
- 길이 K인 ans_range배열이 의미하는 바는 i(일 수), ans_range[i]는 i일자에 랑이의 만족도
1) 

"""
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
can = list(map(int, input().split()))
