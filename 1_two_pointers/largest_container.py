'''
You are given an array of numbers, each representing the height of a vertical line on a graph,
A container can be formed with any pair of these lines, along with the x-axis of the graph,
Return the amount of water which the largest container can hold

Input heights = [2, 7, 8, 3, 7, 6]
Output: 24
'''


def brute_force(heights: list[int]) -> int:
    n = len(heights)
    max_water = 0
    for i in range(n):
        for j in range(i+1, n):
            water = min(heights[i], heights[j]) * (j-i)
            max_water = max(water, max_water)

    return max_water


def two_pointers_approach(heights: list[int]) -> int:
    # we get the most width by placing pointers at the ends of the array, so start from there
    left = 0
    right = len(heights)-1
    max_water = 0
    while left < right:
        water = min(heights[left], heights[right]) * (right - left)
        max_water = max(water, max_water)
        if heights[left] < heights[right]:
            left += 1
        elif heights[left] > heights[right]:
            right -= 1
        else:
            break

    return max_water


def main():
    assert two_pointers_approach([]) == 0
    assert two_pointers_approach([1]) == 0
    assert two_pointers_approach([0, 1, 0]) == 0
    assert two_pointers_approach([3, 3, 3, 3]) == 9
    assert two_pointers_approach([1, 2, 3]) == 2
    assert two_pointers_approach([3, 2, 1]) == 2
    assert two_pointers_approach([2, 7, 8, 3, 7, 6]) == 24


if __name__ == "__main__":
    main()
