# https://www.acmicpc.net/problem/1966

from collections import deque

T = int(input())

while T:
    N, M = map(int,input().split())
    que = deque(map(int, input().split()))
    cnt = 0

    while True:
        largest = max(que)
        if M == 0:
            if largest == que[0]:
                print(cnt + 1)
                break
            else:
                M = len(que)
        if largest == que[0]:
            que.popleft()
            cnt += 1
        else:
            que.append(que.popleft())
        M -= 1

    T -= 1
