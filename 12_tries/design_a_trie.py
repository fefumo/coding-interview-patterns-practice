""" 
Design and implement a trie data structure that supports the following operations:
    • insert(word: str) -> None: Inserts a word into the trle.
    • search(word: str) -> bool: Returns true if a word exists in the trie, and false if not.
    • has_prefix(prefix: str) -> bool: Returns true if the trie contains a word with
        the given prefix, and false if not.

Example:
    Input: [insert("top"), insert("bye"), has_prefix("to"), search("to"),
    insert("to"), search("to")]
    Output: (True, False, True]

Explanation:
    insert("top")       # trie has: "top"
    insert("bye")       # trie has: "top" and "bye"
    has_prefix("to")    # prefix "to" exists in the string "top": return True
    search("to")        # trie does not contain the word " to": return False
    insert("to")        # trie has: "top", "bye", and "to"
    search("to")        # trie contains the word "to": return True

Constraints:
    • The words and prefixes consist only of lowercase EngUsh letters.
    • The length of each word and prefix is at least one character
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for c in word:
            # For each char in the word, if it's not a child of the
            # current node, create a new node for that char
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        # the last node is the end of a word
        node.is_word = True

    def search(self, word: str):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_word

    def has_prefix(self, prefix: str):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True


def main():
    t = Trie()
    t.insert("top")       # trie has: "top"
    t.insert("bye")       # trie has: "top" and "bye"
    # prefix "to" exists in the string "top": return True
    print(t.has_prefix("to"))
    # trie does not contain the word " to": return False
    print(t.search("to"))
    t.insert("to")        # trie has: "top", "bye", and "to"
    print(t.search("to"))        # trie contains the word "to": return True


if __name__ == "__main__":
    main()
