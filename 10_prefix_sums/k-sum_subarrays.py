""" 
Find the number of subarrays in an integer array that sum to k.

Example:
    Input: nums = [1, 2, -1, 1, 2], k = 3
    Output: 3
"""


def k_sum_subarrays(nums: list[int], k: int) -> int:
    n = len(nums)
    count = 0
    # the first element will be zero, the formula is `pf[j] - pf[i - 1] == k,
    # so that when i == 0, we don't get out of boundaries exception`
    prefix_sum = [0]
    for i in range(0, n):
        prefix_sum.append(prefix_sum[-1] + nums[i])

    for j in range(1, n + 1):
        for i in range(1, j + 1):
            if prefix_sum[j] - prefix_sum[i - 1] == k:
                count += 1
    return count

# optimized brainfuck


def k_sum_subarrays_optimized(nums: list[int], k: int) -> int:
    count = 0
    # Initialize the map with 0 to handle subarrays that sum to 'k'
    # from the start of the array
    prefix_sum_map = {0: 1}
    curr_prefix_sum = 0
    for num in nums:
        # Update the running prefix sum by adding the current number
        curr_prefix_sum += num
        # If a subarray with sum 'k' exists, increment count by the
        # number of times it has been found.
        if curr_prefix_sum - k in prefix_sum_map:
            count += prefix_sum_map[curr_prefix_sum - k]
        # Update the frequency of 'count_prefix_sum' in the hashmap
        freq = prefix_sum_map.get(curr_prefix_sum, 0)
        prefix_sum_map[curr_prefix_sum] = freq + 1
    return count


def main():
    nums = [1, 2, -1, 1, 2]
    print(k_sum_subarrays(nums, 3))
    print(k_sum_subarrays_optimized(nums, 3))


if __name__ == "__main__":
    main()
