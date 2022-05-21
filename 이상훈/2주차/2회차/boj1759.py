from itertools import combinations


def is_vowel_in_case(case):
    for vowel in vowels:
        if vowel in case:
            return True
    return False


def is_two_consonants_in_case(case):
    cnt = 0
    for char in case:
        if char in vowels:
            cnt += 1
    return len(case) - cnt > 1


L, C = map(int, input().split())

chars = list(input().split())

cases = combinations(chars, L)
vowels = ('a', 'e', 'u', 'i', 'o')
answer = []


for case in cases:
    if is_vowel_in_case(case) and is_two_consonants_in_case(case):
        answer.append(''.join(sorted(case)))

for ans in sorted(answer):
    print(ans)

