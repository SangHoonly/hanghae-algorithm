from itertools import combinations
from typing import List

# 인풋이 max 3000 이라 완전탐색 n^3 코드가 타이트하게 통과할 줄 알았지만, 타임아웃 에러가 떴다.
# 따라서 투포인터 솔루션으로 해결하였다.

def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    ret = set()

    for idx in range(len(nums) - 2):
        left = idx + 1
        right = len(nums) - 1

        while left < right:
            three_sum = nums[idx] + nums[left] + nums[right]

            if not three_sum:
                ret.add((nums[idx], nums[left], nums[right]))
                right -= 1
                left += 1

            if three_sum > 0:
                right -= 1

            elif three_sum < 0:
                left += 1

    return [list(e) for e in list(ret)]

# 완전탐색 n^3 코드. sum(nC3) = 0 을 만족하는 case들을 찾으면 된다.
def threeSum2(nums: List[int]) -> List[List[int]]:
    return [list(c) for c in set([tuple(sorted(c)) for c in combinations(nums, 3)]) if not sum(c)]
