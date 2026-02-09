""" 
You are given an array representing the heights of trees, and an integer k representing the
total length of wood that needs to be cut.

For this task, a woodcutting machine is set to a certain height, H. The machine cuts off the
top part of all trees taller than H, while trees shorter than H remain untouched. Determine
the highest possible setting of the woodcutter (H) so that it cuts at least k meters of wood,
Assume the woodcutter cannot be set higher than the height of the tallest tree in the array.

Example:
    Input: heights = [2, 6, 3, 8], k = 7
    Output: 3
"""


def cutting_wood(k: int, heights: list[int]):
    left, right = 0, max(heights)
    while left < right:
        mid = (left + right) // 2 + 1
        if cuts_enough_wood(mid,k,heights):
            left = mid
        else: 
            right = mid - 1

    return right

def cuts_enough_wood(H: int, k: int, heights: list[int]) -> bool:
    wood_collected = 0
    for height in heights:
        if height > H:
            wood_collected += (height - H)
    return wood_collected >= k

def main():
    print(cutting_wood(7, [2,6,3,8]))


if __name__ == "__main__":
    main()
