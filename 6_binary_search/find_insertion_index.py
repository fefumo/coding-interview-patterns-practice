""" 
You are given a sorted array that contains unique values, along with an integer target
• If the array contains the target value , return its index.
• Otherwise, return the insertion index. This is the index where the target would be if it
were inserted in order, maintaining the sorted sequence of the array.

Example 1:
    Input: nums = [1, 2, 4, 5, 7, 8, 9], target= 4
    Output: 2
Example 2:
    Input: nums = [1, 2, 4, 5, 7, 8, 9], target = 6
    Output: 4
Explanation: 6 would be inserted at index 4 to be positioned between 5 and 7: [1, 2, 4,
5, 6, 7, 8, 9].
"""


def find_insertion_index(numbers: list[int], target: int) -> int:
    left = 0
    right = len(numbers)
    while left < right:
        mid = (left + right) // 2
        if numbers[mid] >= target:
            right = mid
        else:
            left = mid + 1

    return left


def main():
    nums = [1, 2, 4, 5, 6, 7, 8, 9]
    target = 4
    res = find_insertion_index(nums, target)
    print(res)

    nums = [1, 2, 4, 5, 7, 8, 9]
    target = 6
    res = find_insertion_index(nums, target)
    print(res)


if __name__ == "__main__":
    main()
