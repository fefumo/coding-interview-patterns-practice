""" 
Given a 2D board of characters and an array of words, find all the words in the array that
can be formed by tracing a path through adjacent cells in the board. Adjacent cells are those
which horizontally or vertically neighbor each other. We can't use the same cell more than
once for a single word.
"""

# it says to review the Backtracking chapter before contiuing with this problem
# but i hope i will be able to understand it since we are going to use
# Tries i suppose


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


def is_within_bounds(r, c, board):
    return 0 <= r < len(board) and 0 <= c < len(board[0])


def dfs(board, r, c, node, res):
    if node.word:
        res.append(node.word)
        node.word = None

    temp = board[r][c]
    board[r][c] = '#'
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for d in dirs:
        next_r, next_c = r + d[0], c + d[1]
        if (is_within_bounds(next_r, next_c, board) and
                board[next_r][next_c] in node.children):
            dfs(board, next_r, next_c,
                node.children[board[next_r][next_c]], res)
    board[r][c] = temp  # mark as unvisited


def find_all_words_on_a_board(board, words):
    root = TrieNode()
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word
    res = []
    # start a dfs call from each cell of the board that contains a
    # child of the root node, which represents the first letter of
    # a word in the trie.
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] in root.children:
                dfs(board, r, c, root.children[board[r][c]], res)
    return res


def main():

    pass


if __name__ == "__main__":
    main()
