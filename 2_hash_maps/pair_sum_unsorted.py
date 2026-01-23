""" 
Given an array of integers, return the indexes of any two numbers that add up to a target
The order of the indexes in the result doesn't matter. If no pair is found, return an empty
array.
Example:
Input: nums = [-1, 3, 4, 2], target = 3
Output: [0, 2]
Explanation: nums[0] + nums[2] = -1 + 4 = 3
Constraints:
• The same index cannot be used twice in the result
"""


def brute_force(nums: list[int], target: int) -> list[int]:
    """ go through every possible pair in the array to see if their sum is equal to the target; O(n^2)."""
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target and i != j:
                return [i, j]
    return []


def pair_sum(nums: list[int], target: int) -> list[int]:
    result = []
    num_map = {}

    for i, num in enumerate(nums):
        num_map[num] = i  # key = number, value = index

    for i, num in enumerate(nums):
        complement = target - num
        # so it's not the same object of array
        if complement in num_map and num_map[complement] != i:
            return [i, num_map[complement]]

    return result


def one_pass(nums: list[int], target: int) -> list[int]:
    """ key = number, value = index, but check if we have the complement on the fly """
    hashmap = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in hashmap:
            return [hashmap[complement], i]

        hashmap[num] = i

    return []


def main():
    assert brute_force([-1, 3, 4, 2], 3) == [0, 2]
    assert pair_sum([-1, 3, 4, 2], 3) == [0, 2]
    assert one_pass([-1, 3, 4, 2], 3) == [0, 2]


if __name__ == "__main__":
    main()
