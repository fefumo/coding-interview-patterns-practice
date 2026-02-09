""" 
A rotated sorted array is an array of numbers sorted in ascending order, in which
a portion of the array is moved from the beginning to the end.
For example, a possible rotation of [1, 2, 3, 4, 5] is [3, 4, 5, 1, 2], where the first two
numbers are moved to the end.

Given a rotated sorted array of unique numbers, return the index
of a target value. If the target value is not present, return -1.

Example:
    Input nums = [8, 9, 1, 2, 3, 4, 5, 6, 7], target = 1
    Output: 2
"""


def solution(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        # if the left subarray is sorted, check if
        # the target is in the range
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                # then the target is in the left subarray
                right = mid - 1
            else:
                # then the target is in the right subarray
                left = mid + 1

        # then, the left subarray is not sorted so check the right subarray
        else:
            if nums[mid] < target <= nums[right]:
                # then search the right subarray
                left = mid + 1
            else:
                right = mid - 1
    return left if nums[left] == target else -1


def main():
    nums = [8, 9, 1, 2, 3, 4, 5, 6, 7]
    target = 1
    res = solution(nums, target)
    print(res)


if __name__ == "__main__":
    main()
