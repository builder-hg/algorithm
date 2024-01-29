import sys
N = int(input())
str = input()
lst = list(str)
ans_wrap = []
dict = {}
cnt = 0
types = []    
s = 0               
e = 0
maxV = 0         

while s <= e < len(lst):
    if lst[e] in types:  # 새로 이동한 지점에 위치한 타입이 기존에 있던 타입이라면
        cnt += 1        # cnt를 1증가시킨다.
        dict[lst[e]] += 1
        e += 1          # 끝지점을 한칸 뒤로 이동시킨다.
    else:               # 새로 이동한 지점에 위치한 타입이 기존에 없는 경우
        if len(types) < N:     # 1) 새롭게 타입을 추가해야하는 경우
            cnt += 1
            types.append(lst[e])
            dict[lst[e]] = 1
            e += 1
        else:                # 2) 기존타입을 삭제하고 추가해야 하는경우
            
            # maxV = max(maxV, cnt)
            # dict[lst[s]] -= 1
            # cnt -= 1
            # if dict[lst[s]] == 0:
            #     types.remove(lst[s])
            # s += 1
maxV = max(cnt, maxV)
print(maxV)