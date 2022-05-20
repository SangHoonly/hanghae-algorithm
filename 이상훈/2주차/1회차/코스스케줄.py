from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)

        for [a, b] in prerequisites:
            graph[b].append(a)


        def has_cycle(cur_node, visited):
            while graph[cur_node]:
                next_node = graph[cur_node].pop()

                if visited[next_node]:
                    return True

                visited[next_node] = True

                if has_cycle(next_node, visited):
                    return True

                visited[next_node] = False

            return False

        for start in list(graph.keys()):
            visited = defaultdict(bool)
            visited[start] = True

            if has_cycle(start, visited):
                return False

        return True
