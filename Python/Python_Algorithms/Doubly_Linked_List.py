class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class Doubly_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def append(self, value):
        new_node = Node(value)
        if not self._length:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        self._length += 1
        return self

    def prepend(self, value):
        new_node = Node(value)
        if not self._length:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        self._length += 1
        return self

    def pop_left(self):
        if not self._length:
            raise Exception("List is empty")
        former_head = self.head
        if self._length == 1:
            self.head = self.tail = None
        else:
            self.head = former_head.next
            self.head.previous = former_head.next = None
        self._length -= 1
        return former_head.value

    def pop_right(self):
        if not self._length:
            raise Exception("List is Empty")
        former_tail = self.tail
        if self._length == 1:
            self.head = self.tail = None
        else:
            self.tail = former_tail.previous
            self.tail.next = former_tail.previous = None
        self._length -= 1
        return former_tail.value

    def remove(self, value):
        if not self._length:
            raise Exception("List is empty")
        if self.head.value == value:
            return self.pop_left()
        previous_node = self.head
        current_node = self.head.next
        while current_node is not None and current_node.value != value:
            previous_node = current_node
            current_node = current_node.next
        if current_node is None:
            raise ValueError("Item not in list")
        if current_node.next is None:
            return self.pop_right()
        current_node.next.previous = previous_node
        previous_node.next = current_node.next
        current_node.next = current_node.previous = None
        self._length -= 1
        return current_node.value




my_list = Doubly_Linked_List()
my_list.append(5)
my_list.append(4)
my_list.append(3)
my_list.append(2)
my_list.append(1)
print("***Append***")
print(my_list.head.value)
x=my_list.head.next.value
print(x)
y=my_list.tail.previous.value
print(y)
print(my_list.tail.value)
print(my_list._length)
print("\n")
print("***Prepend***")
my_list.prepend(6)
print(my_list.head.value)
z = my_list.head.next
print(z.value)
print(z.previous.value)
print(my_list.tail.value)
print(my_list._length)
print("\n")
print("***Pop Left***")
my_list.pop_left()
print(my_list.head.value)
print(my_list.tail.value)
print(my_list._length)
print("\n")
print("***Pop Left***")
my_list.pop_right()
print(my_list.head.value)
print(my_list.tail.value)
print(my_list._length)
