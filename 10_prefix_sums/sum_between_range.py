""" 
Given an integer array, write a function which returns the sum of values between two
indexes.

Exmaple:
     Input: nums = [3, -7, 6, 0, -2, 5], [sum_range(0, 3), sum_range(2, 4),
     sum_range(2,2)]
     Output: [2,4,6]

Constraints:
    • nums contains at least one element
    • Each sum_range operation will query a valid range of the input array.
"""


class SumBetweenRange:
    def __init__(self, nums: list[int]) -> None:
        self.prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            self.prefix_sum.append(self.prefix_sum[-1] + nums[i])

    def sum_range(self, i: int, j: int) -> int:
        if i == 0:
            return self.prefix_sum[j]
        return self.prefix_sum[j] - self.prefix_sum[i - 1]


def main():
    nums = [3, -7, 6, 0, -2, 5]
    cl = SumBetweenRange(nums)
    print(cl.sum_range(0, 3), cl.sum_range(2, 4), cl.sum_range(2, 2))


if __name__ == "__main__":
    main()
