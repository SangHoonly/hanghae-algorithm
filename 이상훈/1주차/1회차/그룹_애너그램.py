from typing import List
from collections import defaultdict


# https://leetcode.com/problems/group-anagrams/submissions/
# 제한 사항 : words 최대 길이 10000, 한 word의 최대 길이 100.
# words 길이를 n, word 길이를 m으로 두었을 시 m * m * n 혹은 m * log(m) * n의 알고리즘까지는 사용 가능.
# 여기서는 word를 정렬하는 방법으로 m * log(m) * m 알고리즘을 사용.


def solution(words: List[str]) -> List[List[str]]:
    mapper = defaultdict(list)

    for word in words:
        mapper["".join(sorted(word))].append(word)

    return list(mapper.values())
