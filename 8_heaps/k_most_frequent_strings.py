import heapq

""" 
Find the k most frequently occurring strings in an array, and return them sorted by
frequency in descending order. If two strings have the same frequency, sort them in
lexicographical order.

Example:
    Input: strs = ["go", "coding" , "byte", "byte" , " go", "interview", "go"],
            k = 2
    Output: ["go", "byte"]

Explanation: The strings "go" and "byte" appear the most frequently, with frequencies of
3 and 2 , respectively.

Constraints:
    • k <= n, where n denotes the length of the array.
"""


class Pair:
    def __init__(self, s, freq):
        self.s = s
        self.freq = freq

    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq > other.freq

        return self.s < other.s

    def __repr__(self):
        return f'Pair: ({self.s}, {self.freq})'


def find_most_freq_strs(strs: list[str], k: int):
    hashtable = {}
    for s in strs:
        if s in hashtable:
            hashtable[s] += 1
        else:
            hashtable[s] = 1
    # print(hashtable.items())

    arr = [Pair(s, freq) for s, freq in hashtable.items()]
    heapq.heapify(arr)
    # print(*arr, sep='\n')
    top = [heapq.heappop(arr).s for _ in range(k)]
    return top


def main():

    strs = ["go", "coding", "byte", "byte", "go", "interview", "go"]
    k = 2
    print(find_most_freq_strs(strs, k))


if __name__ == "__main__":
    main()
