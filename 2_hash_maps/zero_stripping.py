""" 
For each zero in an m x n matrix,
set its entire row and column to zero in place.
"""


def zero_stripping(matrix: list[list[int]]):
    '''If a number is in a column or a row containing zero, it will also become zero'''
    zero_rows = set()
    zero_columns = set()

    for row in range(len(matrix)):
        # matrix is n*m size, so m = matrix[0]
        for col in range(len(matrix[0])):
            num = matrix[row][col]
            if num == 0:
                zero_rows.add(row)
                zero_columns.add(col)

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if r in zero_rows or c in zero_columns:
                matrix[r][c] = 0


'''
    then there is a second more optimal implementation
    which i decided not to write because it seemed to be an overkill
    to me which i wouldnt have found in a million years
'''


def main():
    pass


if __name__ == "__main__":
    main()
