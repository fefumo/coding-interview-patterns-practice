""" 
Given a string. determine the length of its longest substring that
consists only of unique characters.

Example 1:
    Input: s = "abcba"
    Output: 3

Explanation: Substring "abc" is the longest substring of length 3 that contains unique
characters ("cba" also fits this description).
"""


def brute_force(s: str) -> int:
    max_count = 0
    for i in range(len(s)):
        count = 0
        charset = set()
        for j in range(i, len(s)):
            ch = s[j]
            if ch in charset:
                break
            charset.add(ch)
            count += 1
        max_count = max(count, max_count)

    return max_count


def sliding_window(s: str) -> int:
    charset = set()
    left = right = 0
    max_len = 0
    while right < len(s):

        # if we enctounter a duplicate, shirk the window until there are no duplicates
        while s[right] in charset:
            charset.remove(s[left])
            left += 1
        # once there are no more duplicates, update max_len if the cur_window is longer
        max_len = max(max_len, right - left + 1)
        charset.add(s[right])
        right += 1
    return max_len


def optimised_sliding_window(s: str) -> int:
    max_len = 0
    prev_indexes = {}
    left = right = 0
    while right < len(s):
        # if a prev index of the current character is present in
        # the current window, it's a duplicate in the window
        if (s[right] in prev_indexes and prev_indexes[s[right]] >= left):
            left = prev_indexes[s[right]] + 1

        max_len = max(max_len, right - left + 1)
        prev_indexes[s[right]] = right
        right += 1
    return max_len


def main():
    res = brute_force("abcba")
    res2 = sliding_window("abcba")
    res3 = optimised_sliding_window("abcba")
    print(res, res2, res3)


if __name__ == "__main__":
    main()
