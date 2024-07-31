import sys
input = sys.stdin.readline

arrVowel = ['a', 'i', 'y', 'e', 'o', 'u']
arrConsonant = ['b', 'k', 'x', 'z', 'n', 'h', 'd', 'c', 'w', 'g', 'p', 'v', 'j', 'q', 't', 's', 'r', 'l', 'm', 'f']

lines = sys.stdin.readlines()

for line in lines:
    raw = line.rstrip()
    ans = ''

    for item in raw:
        if not item.isalpha():
            ans += item
            continue

        isUpper = item.isupper()
        
        tmp = ''
        if item.lower() in arrVowel:
            idx = arrVowel.index(item.lower())
            tmp = arrVowel[(idx + 3) % len(arrVowel)]
        else:
            idx = arrConsonant.index(item.lower())
            tmp = arrConsonant[(idx + 10) % len(arrConsonant)]

        if isUpper:
            ans += tmp.upper()
        else:
            ans += tmp

    print(ans)