from collections import defaultdict, Counter
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def is_all_ticket_used(itinerary):
            return len(tickets) + 1 == len(itinerary)


        def dfs(departure, ticket_counts, itinerary):

            if is_all_ticket_used(itinerary):
                return itinerary

            for arrival in graph[departure]:
                if not ticket_counts[(departure, arrival)]:
                    continue
                itinerary.append(arrival)
                ticket_counts[(departure, arrival)] -= 1

                result = dfs(arrival, ticket_counts, itinerary[:])

                if result:
                    return result

                ticket_counts[(departure, arrival)] += 1
                itinerary.pop()

            return []


        graph = defaultdict(list)
        ticket_counts = Counter([(dep, arr) for [dep, arr] in tickets])
        tickets.sort()


        for [dep, arr] in tickets:
            graph[dep].append(arr)

        return dfs("JFK", ticket_counts, ["JFK"])
