# https://leetcode.com/problems/longest-palindromic-substring
# 제한 사항 : s 길이 1000 이하.
# 문자열의 길이가 1000 이하기 때문에, 완전 탐색 n^2 알고리즘을 써도 무방.
# for 문을 돌며 특정 문자를 기준으로 앞뒤만 비교 & 반복하면 되므로, 본 코드에서는 조금 더 효율적으로 탐색하고자 투포인터 방식을 사용.

def solution(s: str) -> str:
    def get_max_palindrome(l_idx: int, r_idx: int) -> str:
        sub_str = s[l_idx:r_idx + 1]
        front = l_idx - 1
        rear = r_idx + 1

        while front >= 0 and rear < len(s) and s[front] == s[rear]:
            sub_str = s[front:rear + 1]
            rear += 1
            front -= 1

        return sub_str

    ret = s[0]

    for idx in range(len(s) - 1):
        if s[idx] == s[idx + 1]:
            ret = max(ret, get_max_palindrome(idx, idx + 1), key=len)
        ret = max(ret, get_max_palindrome(idx, idx), key=len)

    return ret
