""" 
Design and implement a data structure that supports the following operations:
    • insert(word: str) -> None: Inserts a word into the data structure.
    • search.(word: str) -> bool: Returns true if a word exists in the data structure and
      false if not. The word may contain wildcards ('.') that can represent any letter.
Example:
    Input: [insert("band"), insert("rat"), search("ra. "), search("b.."),
    insert("ran"), search(".an")]
    Output (True, False, True]

Explanation:
    insert("band") # data structure has: "band"
    insert("rat") # data structure has: "band" and "rat"
    search("ra.") # "ra." matches "rat": return True
    search("b..") # no three-letter word starting with 'b' in the data structure:
                     return False
    insert("ran") # data structure has: "band", "rat", and "ran"
    search(".an") #".an" matches "ran": return True

Constraints:
    • Words will only contain lowercase English letters and (' . ') characters.
"""

from design_a_trie import Trie, TrieNode


class WildcardTrie(Trie):
    def search(self, word: str):
        return self.search_helper(0, word, self.root)

    # recursive function for finding words with wildrcards
    def search_helper(self, word_index: int, word: str, node: TrieNode):
        for i in range(word_index, len(word)):
            c = word[i]
            if c == '.':
                for child in node.children.values():
                    # recursively search for the rest of the word
                    # from each child node
                    if self.search_helper(i+1, word, child):
                        return True
                return False
            elif c in node.children:
                node = node.children[c]
            else:
                return False
        # after procesing the last character, return true if its
        # the end of a word
        return node.is_word


def main():
    t = WildcardTrie()
    t.insert("rat")
    t.insert("band")
    print(t.search("ra."))
    print(t.search("b.."))
    print(t.search("b..."))
    t.insert("ran")
    print(t.search(".an"))


if __name__ == "__main__":
    main()
