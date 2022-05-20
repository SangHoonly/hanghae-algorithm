from itertools import combinations
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        # nums 리스트의 숫자 중 nCk 개를 택함.
        # k는 0부터 len(nums) 까지.
        for k in range(len(nums) + 1):
            cases = combinations(nums, k)
            for case in cases:
                result.append(list(case))


        return result
