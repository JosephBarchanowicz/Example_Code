class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __len__(self):
        def __len__(self):
            return self._size

    def enqueue(self, value):
        new_node = Node(value)
        if not self._size:
            self.head = self.tail = None
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1
        return self

    def dequeue(self, value):
        if not self._size:
            raise Exception("Queue is empty")
        former_head = self.head
        self.head = former_head.next
        former_head.next = None
        self._size -= 1
        if not self._size:
            self.tail = None
        return former_head

    def clear(self):
        self.head = self.tail = None
        self._size = 0
        return self

    def peek(self):
        if self.head:
            return self.head.value
        return None

