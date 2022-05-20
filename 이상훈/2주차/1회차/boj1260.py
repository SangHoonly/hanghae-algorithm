from collections import defaultdict, deque

N, M, V = map(int, input().split())

# 1. 먼저 그래프 만들고, 초기화 시키기.
# 1번 노드와 2, 3, 4번 노드가 연결되어 있다 치면
# {1 : [2, 3, 4]} 이런 식으로, key 노드 번호, value를 연결된 노드로 표현하는 것이 좋겠죠?

graph = defaultdict(list)

while M:
    node_1, node_2 = map(int, input().split())
    graph[node_1].append(node_2)
    graph[node_2].append(node_1) # 첫번째 노드와 두번째 노드가 연결되어 있으므로, 두번째 노드의 리스트에도 첫번째 노드를 넣어줌.

    M -= 1

for node in graph.keys():
    graph[node].sort()


# DFS
dfs_visit = {V}

def dfs(cur_node):

    print(cur_node, end=' ')

    for next_node in graph[cur_node]:
        if next_node not in dfs_visit:
            dfs_visit.add(next_node)
            dfs(next_node)


# BFS
bfs_visit = set()

def bfs(start_node):
    queue = deque([start_node])
    bfs_visit.add(start_node)

    while queue:
        cur_node = queue.popleft()

        print(cur_node, end=' ')

        for next_node in graph[cur_node]:
            if next_node not in bfs_visit:
                bfs_visit.add(next_node)
                queue.append(next_node)



# 두 함수 실행.
dfs(V)
print()
bfs(V)
