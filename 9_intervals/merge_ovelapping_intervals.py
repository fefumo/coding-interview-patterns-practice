""" 
Merge an array of intervals so there are no overlappoing intervals, and return the resultant
merged intervals.

Example:
    Input: intervals = [[3, 4], [7, 8], [2, 5], [6, 7], [1, 4]]
    Output: [[1 , 5], [6 , 8]]

Constraints:
    The input contains at least one interval
    For every index i in the array, intervals[i].start <= intervals[i].end. 
"""


def merge(intervals: list[list[int]]):
    if len(intervals) == 1:
        return intervals

    merged: list[list[int]] = []
    intervals.sort()
    cur_interval = intervals[0]

    for i in range(1, len(intervals)):
        a_start = cur_interval[0]
        a_end = cur_interval[1]
        b_start = intervals[i][0]
        b_end = intervals[i][1]

        if a_end >= b_start:
            # merge intervals
            cur_interval = [a_start, max(a_end, b_end)]
        if a_end < b_start:
            # no overlap. add cur_interval to the merged list
            merged.append(cur_interval)
            cur_interval = [b_start, b_end]
    merged.append(cur_interval)
    return merged


def main():
    intervals = [[3, 4], [7, 8], [2, 5], [6, 7], [1, 4]]
    res = merge(intervals)
    print(res)


if __name__ == "__main__":
    main()
