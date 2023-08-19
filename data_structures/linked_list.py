class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value=None) -> None:
        if value is not None:
            new_node: Node = Node(value)
            self.head: Node = new_node
            self.tail: Node = new_node
            self.length: int = 1
        else:
            self.head: Node = None
            self.tail: Node = None
            self.length: int = 0

    def prepend(self, value) -> bool:
        new_node: Node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def append(self, value) -> bool:
        new_node: Node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self) -> Node:
        if self.length == 0:
            return None
        else:
            pointer: Node = self.head
            removed_node: Node = self.tail
            while pointer.next is not self.tail and pointer.next is not None:
                pointer = pointer.next
            self.tail = pointer
            self.length -= 1
            if self.length == 0:
                self.head = None
                self.tail = None
            return removed_node

    def pop_first(self) -> Node:
        if self.length == 0:
            return None
        else:
            removed_node: Node = self.head
            self.head = self.head.next
            removed_node.next = None
            self.length -= 1
            if self.length == 0:
                self.tail = None
            return removed_node

    def get(self, index: int) -> Node:
        if index < 0 or index >= self.length:
            return None
        else:
            pointer: Node = self.head
            for _ in range(index):
                pointer = pointer.next
            return pointer

    def set(self, index: int, value) -> Node:
        pointer: Node = self.get(index)
        if pointer:
            pointer.value = value
            return True
        return False

    def insert(self, index: int, value):
        new_node: Node = Node(value)
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            previous_node: Node = self.get(index - 1)
            next_node: Node = previous_node.next
            previous_node.next = new_node
            new_node.next = next_node
            self.length += 1
            return True

    def remove(self, index: int) -> Node:
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == (self.length - 1):
            return self.pop()
        else:
            previous_node = self.get(index - 1)
            removed_node = previous_node.next
            previous_node.next = removed_node.next
            removed_node.next = None
            self.length -= 1
            return removed_node

    def reverse(self) -> None:
        pointer: Node = self.head
        self.head = self.tail
        self.tail = pointer

        previous_node: Node = None
        next_node: Node
        for _ in range(self.length):
            next_node = pointer.next
            pointer.next = previous_node
            previous_node = pointer
            pointer = next_node

    def print_linked_list(self) -> None:
        pointer: Node = self.head
        while pointer is not None:
            print(pointer.value)
            pointer = pointer.next

