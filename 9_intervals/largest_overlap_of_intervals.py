""" 
Given an array of intervals , determine the maximum number of intervals that overlap at any
point. Each interval is half-open, meaning it includes the start point but excludes the end
point.

Example:
    Input: intervals = [[1, 3], [2 , 6], [4, 8], [6, 7] , [5, 7]]
    Output: 3

Constraints:
    • The input will contain at least one interval.
    • For every index i in the array, intervals[i].start < intervals[i].end.
"""


def largest_overlap(intervals: list[list[int]]) -> int:
    points = []
    for i in intervals:
        points.append((i[0], 'S'))
        points.append((i[1], 'E'))
    # Sort by the first value, then prioritize 'E' first (if numbers are equal)
    points.sort(key=lambda x: x[0])
    active_intervals = 0
    max_overlaps = 0
    for time, point_type in points:
        if point_type == 'S':
            active_intervals += 1
        else:
            active_intervals -= 1
        max_overlaps = max(max_overlaps, active_intervals)

    return max_overlaps


def main():
    intervals = [[1, 3], [2, 6], [4, 8], [6, 7], [5, 7]]
    print(largest_overlap(intervals))


if __name__ == "__main__":
    main()
