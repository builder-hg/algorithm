import sys
input = sys.stdin.readline

N = int(input())   
arr = list(map(int, sys.stdin.readline().split())) + [0]
diff = 1 << 64
ans = 0 
for mid in range(1, N):
    left = mid - 1
    right = mid
    groupA = arr[left]
    groupB = arr[right]

    while left >= 0 and right <= N-1:
        if groupA <= groupB:   
            if diff > (groupB - groupA): 
                diff = (groupB - groupA)  
                ans = groupA + groupB  
            elif diff == (groupB - groupA):
                diff = (groupB - groupA) 
                ans = max(ans, groupA + groupB) 
            left -= 1
            groupA += arr[left]
        else:                  
            if diff > (groupA - groupB): 
                diff = (groupA - groupB) 
                ans = groupA + groupB 
            elif diff == (groupA - groupB):
                diff = (groupA - groupB) 
                ans = max(ans, groupA + groupB) 
            right += 1
            groupB += arr[right]

print(ans)
