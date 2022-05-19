from itertools import combinations
from typing import List


class Solution:
    cases = None
    k = None
    n = None

    def combination(self,case, depth) -> None:
        if self.k == len(case):
            self.cases.append(case)
            return

        for number in range(depth + 1, self.n + 1):
            case.append(number)
            self.combination(case[:], number)
            case.pop()
        return

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.k = k
        self.n = n
        self.cases = []

        for start in range(1, self.n + 1):
            self.combination([start], start)

        return self.cases



class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return [list(case) for case in combinations([i for i in range(1, n + 1)], k)]

