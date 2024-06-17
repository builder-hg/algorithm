"""
[2,0] [7,1] [11,2] [15,3]

target = 9
s = 2
e = 15
17 > 9
2, 11
13 > 9
2, 7 = 9

# basic template, 문제에 맞게 응용해서 사용한다.
N = int(input())
arr = list(map(int, input().split()))
X = int(input())

cnt = 0
s = 0
e = N-1
while s < e:
	if arr[s] + arr[e] == X:[2,0] [7,1] [11,2] [15,3]

target = 9
s = 2
e = 15
17 > 9
2, 11
13 > 9
2, 7 = 9

# basic template, 문제에 맞게 응용해서 사용한다.
N = int(input())
arr = list(map(int, input().split()))
X = int(input())

cnt = 0
s = 0
e = N-1
while s < e:
	if arr[s] + arr[e] == X:
		cnt += 1
		s += 1
		e -= 1
	elif arr[s] + arr[e] < X:
		s += 1
	else:
		e -= 1

print(cnt)
		cnt += 1
		s += 1
		e -= 1
	elif arr[s] + arr[e] < X:
		s += 1
	else:
		e -= 1

print(cnt)
"""
nums = [3, 3]
target = 6

arr = []
for i in range(len(nums)):
    a, b = i, nums[i]
    arr.append([b, a])
arr.sort()

ans = [0, 0]
s = 0
e = len(nums) - 1
while s < e:
    ans[0] = arr[s][1]
    ans[1] = arr[e][1]

    if arr[s][0] + arr[e][0] == target:
        print(ans)
        break
    elif arr[s][0] + arr[e][0] > target:
        e -= 1
    elif arr[s][0] + arr[e][0] < target:
        s += 1