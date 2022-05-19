# https://www.acmicpc.net/problem/2164

from collections import deque

Q = deque([_ + 1 for _ in range(int(input()))])

while len(Q) > 1:
    Q.popleft()
    Q.append(Q.popleft())

print(Q[0])
