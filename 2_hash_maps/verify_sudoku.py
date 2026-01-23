""" 
Given a partially completed 9x9 Sudoku board, determine if the current state of the board
adheres to the rules of the game:
• Each row and column must contain unique numbers between 1 and 9, or be empty
(represented as 0).
• Each of the nine 3x3 subgrids that compose the grid must contain unique numbers
between 1 and 9, or be empty.
Note: You are asked to determine whether the current state of the board is valid given
these rules, not whether the board is solvable.
"""


def brute_force():
    """
    Take each number in the row and search the row to see if that number appears again.
    Performing a linear search for each number would result in O(n^2) time complexity.
    """
    result = []

    return result


def verify_sudoku(sudoku: list[list[int]]):
    rows = [set() for _ in range(9)]
    columns = [set() for _ in range(9)]
    subgrids = [[set() for _ in range(3)] for _ in range(3)]

    for i in range(len(sudoku)):
        for k in range(len(sudoku)):
            cur_num = sudoku[i][k]

            if cur_num == 0:
                continue
            if cur_num in rows[i]:
                return False
            if cur_num in columns[k]:
                return False
            # to find a subgrid, we have to divide the i,k by 3
            if cur_num in subgrids[i//3][k//3]:
                return False

            # key = index, value = value
            rows[i].add(cur_num)
            columns[k].add(cur_num)
            subgrids[i//3][k//3].add(cur_num)

    return True


def main():
    board = [
        [3, 0, 6, 0, 5, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [1, 0, 2, 5, 0, 0, 3, 2, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [0, 3, 0, 0, 0, 8, 2, 5, 0],
        [0, 0, 5, 2, 0, 6, 0, 0, 0]
    ]
    assert verify_sudoku(board) == False


if __name__ == "__main__":
    main()
