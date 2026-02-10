""" 
Design a data structure that supports adding integers from a data stream and retrieving the
median of all elements received at any point.
    • add(num: int) -> None: adds an integer to the data structure.
    • get_median() -> float: returns the median of all integers so far.

Example:
    Input: (add(3), add(6), get_median(), add(1), get_median()]
    Output: [4.5, 3.0]

Explanation:
    add(3) # data structure contains [3] when sorted
    add(6) # data structure contains [3,6] when sorted
    get_median () # median is (3 + 6) / 2 = 4.5
    add(1) # data structure contains [1, 3, 6] when sorted
    get_median () # median is 3.0

Constraints:
    • At least one value will have been added before get_median is called.
"""

import heapq


class MedianOfAnIntegerStream:
    def __init__(self):
        self.left_half = []  # max-heap
        self.right_half = []  # min-heap

    def add(self, num: int):
        # if num is less than the max of left-half, put it in the left-half
        # NOTE: heap is min-based by default, so to get the max_value, we negate it and address the 0-th item
        if not self.left_half or  num <= -self.left_half[0]:
            heapq.heappush(self.left_half, -num)
            # if size of left half is more than +1 of right half, rebalance the heaps
            if len(self.left_half) > len(self.right_half) + 1:
                heapq.heappush(self.right_half, -heapq.heappop(self.left_half)) # negate because right half is not of negative values
        # otherwise, it belongs to the right half
        else:
            heapq.heappush(self.right_half, num)
            # same rebalancing as in the previous case
            if len(self.right_half) > len(self.left_half):
                heapq.heappush(self.left_half, -heapq.heappop(self.right_half))

    def get_median(self)-> float:
        if len(self.left_half) == len(self.right_half):
            return ((-self.left_half[0]) + (self.right_half[0])) / 2
        else:
            return -self.left_half[0]


def main():
    cl = MedianOfAnIntegerStream()
    cl.add(3)
    cl.add(6)
    print(cl.get_median())
    cl.add(1)
    print(cl.get_median())


if __name__ == "__main__":
    main()
