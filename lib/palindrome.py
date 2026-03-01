def longest_palindromic_substring(s: str) -> str:
    """
    Given a string s, return the longest palindromic substring.
    """
    n = len(s)
    if n < 2:
        return s

    start = 0
    max_len = 1

    def expand_around_center(left: int, right: int) -> int:
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    for i in range(n):
        len1 = expand_around_center(i, i)
        len2 = expand_around_center(i, i + 1)
        curr = max(len1, len2)

        if curr > max_len:
            max_len = curr
            start = i - (max_len - 1) // 2

    return s[start:start + max_len]