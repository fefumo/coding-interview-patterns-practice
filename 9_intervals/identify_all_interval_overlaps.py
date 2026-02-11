""" 
Return an array of all overlaps between two arrays of intervals; intervals1 and
intervals2. Each individual interval array is sorted by start value, and contains no
overlapping intervals within itself.

Example:
    Input: intervals1 = [[1, 4], [5, 6], [9, 10]],
        intervals2 = [[2, 7], [8,9]]
    Output: [[2, 4], [5, 6], [9, 9]]

Constraints:
    • For every index i in intervals1, intervals1[i].start < intervalsl[i].end.
    • For every index j in intervals2, intervals2[j].start < intervals2[j].end
"""


def identify(intervals1: list[list[int]], intervals2: list[list[int]]):
    i = j = 0
    overlaps: list[list[int]] = []
    while i < len(intervals1) and j < len(intervals2):
        # A = interval that starts first, B = the other one
        if intervals1[i][0] <= intervals2[j][0]:
            A, B = intervals1[i], intervals2[j]
        else:
            A, B = intervals2[j], intervals1[i]

        # check for an overlap
        if A[1] >= B[0]:
            overlaps.append([B[0], min(A[1], B[1])])

        # advance the pointer associated with the interval that ends first
        if intervals1[i][1] < intervals2[j][1]:
            i += 1
        else:
            j += 1

    return overlaps


def main():
    intervals1 = [[1, 4], [5, 6], [9, 10]]
    intervals2 = [[2, 7], [8, 9]]
    res = identify(intervals1, intervals2)
    print(res)


if __name__ == "__main__":
    main()
