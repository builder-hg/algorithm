"""
5개
5개와 모든 부분문자열을 다 지우면 이긴다.

4개
3개를 지워버리면 1개가 남는다. 필연적으로 이긴다.

0개
진다.

=> SUMMARY
1) 홀수개의 모음이 주어진다면,
앨리스가 모두 지우면 밥이 더 이상 플레이 할 수 가 없으므로 앨리스가 이긴다.

2) 짝수개의 모음이 주어진다면,
앨리스가 주어진 짝수 - 1개를 지운다.
밥이 운 좋게 자음만 삭제한다 하여도, 다음 턴에서 앨리스가 전체 문자열을 지우므로 앨리스가 이긴다.

3) 0개의 모음이 주어진다면,
앨리스는 지울게 없으므로 패배한다.

=> TESTCASE
01. "ooo", true
02. "xxo", true
03. "xxox", true
04. "xxx", false
05. "oxox", true
06. "oxoxoxox", true
07. "x", false

"""
s = "leetcoder"
cnt = 0
for i in s:
    if i in ['a', 'e', 'i', 'o', 'u']:
        cnt += 1

if cnt == 0:
    print(-1)
else:
    print(true)