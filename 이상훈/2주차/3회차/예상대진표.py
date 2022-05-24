import math


def solution(n, A, B):
    cnt = 0

    a, b = min(A, B) - 1, max(A, B) - 1

    while b // 2 != a // 2:
        a /= 2
        b /= 2
        a = math.floor(a)
        b = math.floor(b)
        cnt += 1

    return cnt + 1
