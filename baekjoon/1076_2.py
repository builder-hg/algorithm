import sys
input = sys.stdin.readline

my_dict = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}


ans_lst = []

for i in range(3):
    query = input().strip()
    # 입력받을때마다 하나씩 ans_lst에 추가한다.
    # ans_lst가 비어있는데, black이 들어오는 경우에는 아무것도 담지 않기로 한다.
    if ans_lst == []:
        if my_dict.get(query, 0) == 0:
            continue
    
    ans_lst.append(my_dict.get(query, 0))

# 아무것도 담기지 않을경우 0을 출력한다.
if ans_lst == []:
    print(0)
    sys.exit()

if len(ans_lst) == 1:
    print(0)
    sys.exit()

for i in range(len(ans_lst)):
    # 마지막 값의 경우 곱해야할 값이므로, 그 값만큼 10을 곱해주면 된다.
    if i == (len(ans_lst) - 1):
        for _ in range(ans_lst[i]):
            print(0, end="")
        sys.exit()
    print(ans_lst[i], end="")