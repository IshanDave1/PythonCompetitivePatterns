from typing import Optional, Iterator

class LLNode:
    def __init__(self, data, next_node: Optional['LLNode'] = None):
        self.data = data
        self.next_node = next_node

class LinkedListIterator:
    def __init__(self, node: Optional[LLNode]):
        self.current = node

    def __iter__(self) -> 'LinkedListIterator':
        return self

    def __next__(self) -> int:
        if self.current is None:
            raise StopIteration
        data = self.current.data
        self.current = self.current.next_node
        return data

class LinkedList:
    def __init__(self, head: Optional[LLNode] = None):
        self.head = head
        self.size = 0

    def tail(self) -> Optional[LLNode]:
        return self.head.next_node if self.head else None

    def __iter__(self) -> LinkedListIterator:
        return LinkedListIterator(self.head)

    def __len__(self):
        return self.size

    def last(self) -> Optional['LLNode']:
        if self.head is None:
            return None
        itr = self.head
        while itr.next_node :
            itr = itr.next_node
        return itr

    def append(self,value):
        if self.head is None :
            self.head = LLNode(value)
        last_node = self.last()
        last_node.next_node = LLNode(value)
        self.size +=1

    # def __reversed__(self):

