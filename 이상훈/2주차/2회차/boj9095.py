def recur(n):
    return recur(n - 1) + recur(n - 2) + recur(n - 3) if n > 0 else 1 if not n else 0


T = int(input())

while T:
    print(recur(int(input())))
    T -= 1
