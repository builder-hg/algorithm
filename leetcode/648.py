import sys
input = sys.stdin.readline

_dict = sorted(["cat","bat","rat"], key=len)
sentence = list("the cattle was rattled by the battery".split())

for i in range(len(_dict)):
    leng = len(_dict[i])
    for j in range(len(sentence)):
        now = sentence[j]
        if _dict[i] != now[:leng]: continue

        sentence[j] = _dict[i]

print(*sentence)
