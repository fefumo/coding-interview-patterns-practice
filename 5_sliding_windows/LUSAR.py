""" 
Longest Uniform Substring After Replacements

A uniform substring is one in which all characters are identical. Given a string, determine the
length of the longest uniform substring that can be formed by replacing up to k characters.

Example:
Input: s = "aabcdcca", k = 2
Output: 5
Explanation: if we can only replace 2 characters, the longest uniform substring we can
achieve is "ccccc ", obtained by replacing b and d with c
"""


def longest_uniform_substring_after_replacements(s: str, k: int) -> int:
    freqs = {}
    highest_freq = max_len = 0
    left = right = 0
    while right < len(s):
        # Update the frequency of the character at the right pointer
        # and the highest frequency for the current window
        freqs[s[right]] = freqs.get(s[right], 0) + 1
        highest_freq = max(highest_freq, freqs[s[right]])
        # Calculate replacements needed for the current Window.
        num_chars_to_replace = (right - left + 1) - highest_freq
        # If the number of replacements is bigger than k, then slide the window.
        # The right pointer always gets advanced, so only advance left
        if num_chars_to_replace > k:
            freqs[s[left]] -= 1
            left += 1

        # Since the length of the current window increases or stays the
        # same , assign the length of the current window to 'max_ len'
        max_len = right - left + 1
        right += 1

    return max_len


def main():
    res = longest_uniform_substring_after_replacements("aabbcdcca", 2)
    print(res)


if __name__ == "__main__":
    main()
