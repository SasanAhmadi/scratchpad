class DLinkedListNode:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def _add_node(self, node: DLinkedListNode):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: DLinkedListNode):
        new_next = node.next
        prev = node.prev

        prev.next = new_next
        new_next.prev = prev

    def _pop_tail(self) -> DLinkedListNode:
        node = self.tail.prev
        self._remove_node(node)
        return node

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)

    def __init__(self, capacity: int):
        self.cache = {}
        self.size = 0
        self.capacity = capacity

        self.head, self.tail = DLinkedListNode(0,0), DLinkedListNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if not node:
            return -1

        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)

        if not node:
            node = DLinkedListNode(key, value)

            self._add_node(node)

            self.cache[key] = node

            self.size +=1
            if self.size > self.capacity:
                node = self._pop_tail()
                del self.cache[node.key]
                self.size -=1
        else:
            node.value = value
            self._move_to_head(node)


if __name__ == "__main__":
    cache = LRUCache(2)

    assert cache.put(1,1) == None
    assert cache.put(2,2) == None
    assert cache.get(1) == 1
    assert cache.put(3,3) == None
    assert cache.get(2) == -1
    assert cache.put(4,4) == None
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4

