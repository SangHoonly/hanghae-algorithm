def dfs(x:int, y:int) -> int:
    cnt = 1
    graph[x][y] = 0

    for idx in range(4):
        nx, ny = x + dx[idx], y + dy[idx]

        if not (0 <= nx < N and 0 <= ny < N and graph[nx][ny]):
            continue

        cnt += dfs(nx, ny)

    return cnt

# input 받는 코드
N = int(input())
graph = []
complexes = []
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

for i in range(N):
    graph.append(list(map(int, input())))


for x in range(N):
    for y in range(N):
        if graph[x][y]:
            complexes.append(dfs(x, y))
complexes.sort()

print(len(complexes))
for i in complexes:
    print(i)
