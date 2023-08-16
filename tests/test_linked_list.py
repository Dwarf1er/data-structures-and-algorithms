import unittest
from unittest.mock import patch
from data_structures.linked_list import Node, LinkedList

class TestLinkedList(unittest.TestCase):
    def test_prepend_empty_linked_list(self) -> None:
        linked_list: LinkedList = LinkedList()
        linked_list.prepend(1)

        self.assertEqual(linked_list.length, 1, "LinkedList length is not 1 after prepend operation on empty LinkedList.")

        values = []
        pointer: Node = linked_list.head
        while pointer is not None:
            values.append(pointer.value)
            pointer = pointer.next
        self.assertEqual(values, [1], "LinkedList values don't match the expected values after prepend operation on empty LinkedList.")

    def test_prepend_linked_list(self) -> None:
        linked_list: LinkedList = LinkedList(2)
        linked_list.append(3)
        linked_list.prepend(1)

        self.assertEqual(linked_list.length, 3, "LinkedList length doesn't match expected value after prepend operation on LinkedList.")

        values = []
        pointer: Node = linked_list.head
        while pointer is not None:
            values.append(pointer.value)
            pointer = pointer.next
        self.assertEqual(values, [1,2,3], "LinkedList values don't match the expected values after prepend operation on LinkedList.")

    def test_append_empty_linked_list(self) -> None:
        linked_list: LinkedList = LinkedList()
        linked_list.append(1)

        self.assertEqual(linked_list.length, 1, "LinkedList length is not 1 after append operation on empty LinkedList.")

        values = []
        pointer: Node = linked_list.head
        while pointer is not None:
            values.append(pointer.value)
            pointer = pointer.next
        self.assertEqual(values, [1], "LinkedList values don't match the expected values after append operation on empty LinkedList.")

    def test_append_linked_list(self) -> None:
        linked_list: LinkedList = LinkedList(1)
        linked_list.append(2)
        linked_list.append(3)

        self.assertEqual(linked_list.length, 3, "LinkedList length doesn't match expected value after append operation on LinkedList.")

        values = []
        pointer: Node = linked_list.head
        while pointer is not None:
            values.append(pointer.value)
            pointer = pointer.next
        self.assertEqual(values, [1,2,3], "LinkedList values don't match the expected values after append operation on LinkedList.")

    def test_pop_empty_linked_list(self) -> None:
        linked_list: LinkedList = LinkedList()
        removed_node: Node = linked_list.pop()
        self.assertEqual(linked_list.length, 0, "LinkedList length is not 0 after pop operation on empty LinkedList.")
        self.assertIsNone(removed_node, "Removed node value is not None after pop operation on empty LinkedList.")
    
    def test_pop_single_node_linked_list(self) -> None:
        linked_list: LinkedList = LinkedList(1)
        removed_node: Node = linked_list.pop()
        self.assertEqual(linked_list.length, 0, "LinkedList length is not 0 after pop operation on single node LinkedList.")
        self.assertIsNone(linked_list.head, "LinkedList head is not None after pop operation on single node LinkedList.")
        self.assertIsNone(linked_list.tail, "LinkedList tail is not None after pop operation on single node LinkedList.")
        self.assertIsNotNone(removed_node, "Removed node value doesn't match the expected value after pop operation on single node LinkedList.")

    def test_pop_linked_list(self) -> None:
        linked_list: LinkedList = LinkedList(1)
        linked_list.append(2)
        linked_list.append(3)
        removed_node: Node = linked_list.pop()
        self.assertEqual(linked_list.length, 2, "LinkedList length doesn't match the expected value after pop operation on LinkedList.")
        self.assertEqual(removed_node.value, 3, "Removed node value doesn't match the expected value after pop operation on LinkedList.")

    def test_print_linked_list(self) -> None:
        linked_list: LinkedList = LinkedList(1)
        linked_list.head.next = Node(2)
        linked_list.head.next.next = Node(3)
        
        with patch("builtins.print") as mock_print:
            linked_list.print_linked_list()
            expected_calls = [unittest.mock.call(1), unittest.mock.call(2), unittest.mock.call(3)]
            assert mock_print.mock_calls == expected_calls, "Print calls don't match expected calls."

if __name__ == "__main__":
    unittest.main()