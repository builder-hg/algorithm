import sys
input = sys.stdin.readline

Q = int(input())
dic = {}
while Q:
    Q -= 1

    query = list(map(str, input().split()))
    if query[0] == 'add':
        cur = dic.get(query[1], 0)
        if not cur:
            dic[query[1]] = 1
    elif query[0] == 'remove':
        cur = dic.get(query[1], 0)
        if cur:
            dic[query[1]] = 0
    elif query[0] == 'check':
        cur = dic.get(query[1], 0)
        if cur:
            print(1)
        else:
            print(0)
    elif query[0] == 'toggle':
        cur = dic.get(query[1], 0)
        if cur:
            dic[query[1]] = 0
        else:
            dic[query[1]] = 1
    elif query[0] == 'all':
        dic = {'1': 1, '2': 1, '3': 1, '4':1, '5':1,
        '6': 1, '7': 1, '8': 1, '9':1, '10':1,
        '11': 1, '12': 1, '13': 1, '14': 1, '15': 1,
        '16': 1, '17': 1, '18': 1, '19': 1, '20': 1}
    elif query[0] == 'empty':
        dic = {'1': 0, '2': 0, '3': 0, '4':0, '5':0,
        '6': 0, '7': 0, '8': 0, '9':0, '10': 0,
        '11': 0, '12': 0, '13': 0, '14': 0, '15': 0,
        '16': 0, '17': 0, '18': 0, '19': 0, '20': 0}
