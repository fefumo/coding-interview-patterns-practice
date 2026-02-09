""" 
Given an array of integers sorted in non-decreasing order,
return the first and last indexes of a target number.
If the target is not found, return [ -1, -1] .
Example 1:
    Input: nums = [1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 11], target = 4
    Output: [3,5]
Explanation: The first and last occurrences of number 4 are indexes 3 and 5, respectively.
"""


def first_and_last_occurences_of_a_number(numbers: list[int], target: int) -> list[int]:
    lower_bound = find_lower_bound(numbers, target)
    upper_bound = find_upper_bound(numbers, target)
    return [lower_bound, upper_bound]


def find_lower_bound(numbers: list[int], target: int):
    left = 0
    right = len(numbers)
    iteration = 0
    while left < right:
        mid = (left + right) // 2
        print(
            f'iteration: {iteration}, left = {left}, right = {right} mid = {mid}')
        if numbers[mid] == target:
            right = mid
        if numbers[mid] < target:
            left = mid + 1
        if numbers[mid] > target:
            right = mid - 1

        iteration += 1
    return left


def find_upper_bound(numbers: list[int], target: int):
    left = 0
    right = len(numbers)
    iteration = 0
    while left < right:
        mid = (left + right) // 2 + 1
        print(
            f'iteration: {iteration}, left = {left}, right = {right} mid = {mid}')
        if numbers[mid] == target:
            left = mid
        if numbers[mid] < target:
            left = mid + 1
        if numbers[mid] > target:
            right = mid - 1
        iteration += 1

    return right


def main():
    nums = [1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 11]
    target = 4
    res = first_and_last_occurences_of_a_number(nums, target)
    print(res)


if __name__ == "__main__":
    main()
