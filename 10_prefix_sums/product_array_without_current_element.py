"""
Given an array of intege rs, return an array res so that res[i] is equal to the product of all
the elements of the input array except nums[i] itself.

Example:
    Input: nums = [2, 3, 1, 4, 5]
    Output: [60, 40, 120. 30, 24]
"""


def straight_forward(nums: list[int]) -> list[int]:
    total_product = 1
    for num in nums:
        total_product *= num

    res = []
    for num in nums:
        res.append(total_product//num)

    return res


# Again, brainfuck...
def using_prefix_products(nums: list[int]) -> list[int]:
    n = len(nums)
    res = [1] * n
    for i in range(1, n):
        res[i] = res[i - 1] * nums[i - 1]

    right_product = 1
    for i in range(n - 1, -1, -1):
        res[i] *= right_product
        right_product *= nums[i]
    return res


def main():
    nums = [2, 3, 1, 4, 5]
    print(straight_forward(nums))
    print(using_prefix_products(nums))


if __name__ == "__main__":
    main()
