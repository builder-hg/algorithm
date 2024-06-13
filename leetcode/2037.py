"""
case01)
seats: [1, 4, 5, 9] # sorting
students: [1, 2, 3, 6] # sorting

1: 0
2: 2
3: 2
4: 3

case02)
seats: [2, 2, 6, 6] # sorting
students: [1, 2, 3, 6] # sorting

1: 1
2: 0
3: 3
6: 0 
=> 4
"""
import sys
input = sys.stdin.readline

seats = [2,2,6,6]
students = [1,3,2,6]

seats.sort()
students.sort()

ans = 0
for i in range(len(seats)):
    ans += abs(seats[i] - students[i])

print(ans)