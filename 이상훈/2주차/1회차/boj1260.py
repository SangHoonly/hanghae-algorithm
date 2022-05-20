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


# DFS (재귀)
dfs_visit = {V}

def dfs(cur_node):

    print(cur_node, end=' ')

    for next_node in graph[cur_node]:
        if next_node not in dfs_visit:
            dfs_visit.add(next_node)
            dfs(next_node)


# DFS (스택)
def dfs_stack(start_node):
    visit = set()
    stack = [start_node]

    while stack:
        cur_node = stack.pop()

        if cur_node in visit: # 만일 스택에서 꺼낸 노드가 방문한 적이 있다면, 첨으로 되돌아가 스택에서 다시 뽑음.
            continue

        visit.add(cur_node) # 방문 처리

        print(cur_node, end=' ')

        for next_node in graph[cur_node][::-1]: # 그래프의 노드들은 정렬되어 있으므로, 번호가 작은 순으로 스택을 채우려면 리스트를 뒤집어야 함
            stack.append(next_node)

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

dfs_stack(V)
print()
bfs(V)
