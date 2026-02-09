""" 
Given an integer array nums. return an output array res where, for each value nums[i],
res[i] is the first number to the right that's larger than nums[i]. If no larger number exists
to the right of nums[i], set res[i] to -1.

Example:
    Input: nums = [5, 2, 4, 6, 1]
    Output: [6, 4, 6, -1, -1]
"""


def solution(nums: list[int]):
    # the top of the stack represents the most recent candidate to the right of each
    # new number encountered
    stack = []
    res = [0] * len(nums)
    for i in range(len(nums)-1, -1, -1):
        cur_num = nums[i]
        # if not stack:
        #     res[i] = -1
        #     stack.append(cur_num)
        # if cur_num  > stack[-1]:
        while stack and stack[-1] <= cur_num:
            stack.pop()
        if stack:
            res[i] = stack[-1]
        else:
            res[i] = -1
        stack.append(cur_num)
        # if cur_num < stack[-1]:
        #     res[i] = stack[-1]
        #     stack.append(cur_num)
    return res


def main():
    print(solution([5, 2, 4, 6, 1]))


if __name__ == "__main__":
    main()
