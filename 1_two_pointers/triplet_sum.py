"""
Given an array of integers, return all triplets [a, b, c] such that a + b + c = 0. The
solution must not contain duplicate triplets (e.g., [ 1, 2, 3] and [ 2, 3, 1] are considered
duplicate triplets), If no such triptets are found, return an empty array.
Each triplet can be arranged in any order, and the output can be returned in any order.
"""


def brute_force(nums: list[int]) -> list[list[int]]:
    n = len(nums)
    triplets = set()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    triplets.add(triplet)

    return [list(triplet) for triplet in triplets]


def two_pointers_sum(nums: list[int], target: int) -> list[list[int]]:
    ''' Return a pair which sum matches the target on a **sorted list** '''
    left = 0
    right = len(nums) - 1
    pairs = []
    while left < right:
        sum = nums[left] + nums[right]
        if sum < target:
            left += 1
        elif sum > target:
            right -= 1
        else:
            pairs.append([nums[left], nums[right]])
            left += 1
            while left < right and nums[left] == nums[left - 1]:
                left += 1

    return pairs


def triplet_sum(nums: list[int]) -> list[list[int]]:
    """
    a + b + c = 0 -> b + c = -a 
    """
    nums = sorted(nums)
    res = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        a = nums[i]
        # optimization
        if a > 0:
            break
        pairs = two_pointers_sum(nums[i+1:], -a)
        if pairs:
            for pair in pairs:
                triplet = [a, pair[0], pair[1]]
                res.append(triplet)

    # print(res)
    return res


def main():
    assert triplet_sum([-2, -1, -1, 1, 2, 2]) == [[-1, -1, 2]]
    assert triplet_sum([]) == []
    assert triplet_sum([0]) == []
    assert triplet_sum([1, -1]) == []
    assert triplet_sum([0, 0, 0]) == [[0, 0, 0]]
    assert triplet_sum([1, 0, 1]) == []
    assert triplet_sum([0, 0, 1, -1, 1, -1]) == [[-1, 0, 1]]


if __name__ == "__main__":
    main()
