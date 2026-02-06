'''
Design and implement a data structure for the Least Recently Used (LRU)
cache that supports following operations:
    - LRUCache(capacity: int): Initialize an LRU cache with the specified capacity.
    - get(key:int) -> int: Return the value associated with a key. Return -1 if the key doesn't exist
    - put(key:int, value:int) -> None: Add a key and its value to the cache.
      If adding the key would result in the cache exceeding its size capacity,
      evict the least recently used element. If the key already exists in the cache, update its value.

Example:
    Input:
        [put(1,100), put(2,250), get(2), put(4, 300),
        put(3, 200), get(4), get(1)],
    capacity = 3
    Output: [250, 300, -1]
'''

from __future__ import annotations


class DoublyLinkedListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self
        self.next = self


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = DoublyLinkedListNode(-1, -1)
        self.tail = DoublyLinkedListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_tail(self, node: DoublyLinkedListNode):
        prev_node = self.tail.prev
        node.prev = prev_node
        node.next = self.tail
        prev_node.next = node
        self.tail.prev = node

    def remove_node(self, node: DoublyLinkedListNode):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        self.remove_node( self.hashmap[key])
        self.add_to_tail(self.hashmap[key])
        return self.hashmap[key].val

    def put(self, key: int, value: int):
        if key in self.hashmap:
            self.remove_node( self.hashmap[key])
        node = DoublyLinkedListNode(key, value)
        self.hashmap[key] = node
        if len(self.hashmap) > self.capacity:
            del self.hashmap[self.head.next.key]
            self.remove_node(self.head.next)
        self.add_to_tail(node)


def main():
    cache = LRUCache(3)
    cache.put(1,100)
    cache.put(2,250)
    print(cache.get(2))
    cache.put(4,300)
    cache.put(3,200)
    print(cache.get(4))
    print(cache.get(1))

if __name__ == "__main__":
    main()
