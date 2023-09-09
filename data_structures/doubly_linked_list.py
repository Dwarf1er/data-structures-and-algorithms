class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.previous = None


class DoublyLinkedList:
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

    def pop_first(self) -> Node:
        if self.length == 0:
            return None
        removed_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = removed_node.next
            self.head.previous = None
            removed_node.next = None
        self.length -= 1
        return removed_node

    def prepend(self, value) -> bool:
        new_node: Node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop(self) -> Node:
        if self.length == 0:
            return None
        else:
            removed_node: Node = self.tail
            self.tail = self.tail.previous
            if self.tail is not None:
                self.tail.next = None
            else:
                self.head = None
            removed_node.previous = None
            self.length -= 1
            return removed_node

    def append(self, value) -> bool:
        new_node: Node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def print(self) -> None:
        pointer: Node = self.head
        while pointer is not None:
            print(pointer.value)
            pointer = pointer.next
