import sys 
input = sys.stdin.readline

matching = {
    'black':0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5,
    'blue': 6, 'violet': 7, 'grey': 8, 'white': 9
}

text = input().rstrip()
ans = str(matching.get(text, 0))
text = input().rstrip()
ans += str(matching.get(text, 0))
text = input().rstrip()
ans += matching.get(text, 0) * '0'

if ans[0] == '0':
    if ans[1] == '0':
        print(ans[2:])
    else:
        print(ans[1:])
else:
    print(ans)