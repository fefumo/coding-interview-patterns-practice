"""
Given two strings, s and t, both consisting of lowercase English letters, return the number
of substrings in s that are anagrams of t.
An anagram is a word or phrase formed by rearranging the letters of another word or
phrase, using all the original letters exactly once.

Example:
    Input: s = "caabab", t = "aba"
    Output: 2

Explanation: There is an anagram of t starting at index 1 ("cAABab") and another starting at
index 2 ("caABAb")
"""


def substring_anagrams(s: str, t: str) -> int:
    expected_freqs, window_freqs = [0]*26, [0] * 26
    count = 0
    len_s, len_t = len(s), len(t)
    if len(t) > len(s):
        return 0

    # find out which characters we will have to look for
    for ch in t:
        expected_freqs[ord(ch) - ord('a')] += 1

    left = right = 0
    while right < len_s:
        # before sliding the window, add the characters
        # at the right pointer to wndow_freqs
        window_freqs[ord(s[right]) - ord('a')] += 1
        # when we're at the right length of the window, slide it
        if right - left + 1 == len_t:
            if window_freqs == expected_freqs:
                count += 1

            # move left
            window_freqs[ord(s[left]) - ord('a')] -= 1
            left += 1

        right += 1

    return count


def main():

    pass


if __name__ == "__main__":
    main()
