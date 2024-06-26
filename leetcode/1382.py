import sys


def assemble(s, e):
    if s > e:
        return

    mid = (s + e) // 2
    left = assemble(s, mid - 1)
    right = assemble(mid + 1, e)

    print([arr[mid], left, right])

    return [arr[mid], left, right]

arr = [4, 3, 2, 1]
assemble(0, 3)