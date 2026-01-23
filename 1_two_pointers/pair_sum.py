"""
Given an array of integers sorted in ascending order and a target value, return the indexes
of any pair of numbers in the array that sum to the target. The order of the indexes In the
result doesn't matter. If no pair is found, return an empty array.
"""

def brute_force(nums: list[int], target: int) -> list[int]:
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_pointers(nums: list[int], target: int) -> list[int]:
    right = len(nums) - 1
    left = 0
    while left < right:
        sum = nums[left] + nums[right]
        if sum < target:
            left += 1
        elif sum > target:
            right -= 1
        else:
            print(f"answer: {[left, right]}")
            return [left, right]

    print("answer: []")
    return []


def main() -> None:
    assert two_pointers([],0) == []
    assert two_pointers([1], 1) == []
    assert two_pointers([2,3],5) == [0,1]
    assert two_pointers([2,4],5) == []
    assert two_pointers([2,2,3],5) == [0, 2]
    assert two_pointers([-1,2,3],2) == [0, 2]
    assert two_pointers([-3, -2, -1],-5) == [0, 1]


if __name__ == "__main__":
    main()
