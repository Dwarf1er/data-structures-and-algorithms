import unittest
from unittest.mock import patch
from data_structures.doubly_linked_list import Node, DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):
    def test_pop_first_empty_doubly_linked_list(self) -> None:
        doubly_linked_list: DoublyLinkedList = DoublyLinkedList()

        removed_node: Node = doubly_linked_list.pop_first()
        self.assertEqual(
            removed_node,
            None,
            "Removed node should be None for an empty DoublyLinkedList"
        )
        self.assertEqual(
            doubly_linked_list.length,
            0,
            "Length of empty DoublyLinkedList should be 0"
        )
        self.assertEqual(
            doubly_linked_list.head,
            None,
            "Head of empty should be None for an empty DoublyLinkedList"
        )
        self.assertEqual(
            doubly_linked_list.tail,
            None,
            "Tail of empty should be None for an empty DoublyLinkedList"
        )

    def test_pop_first_single_node_doubly_linked_list(self) -> None:
        doubly_linked_list: DoublyLinkedList = DoublyLinkedList(1)

        removed_node: Node = doubly_linked_list.pop_first()
        self.assertEqual(
            removed_node.value,
            1,
            "Removed node value should be 1"
        )
        self.assertEqual(
            doubly_linked_list.length,
            0,
            "Length of single node DoublyLinkedList should be 0"
        )
        self.assertEqual(
            doubly_linked_list.head,
            None,
            "Head of empty should be None for a single node DoublyLinkedList"
        )
        self.assertEqual(
            doubly_linked_list.tail,
            None,
            "Tail of empty should be None for a single node DoublyLinkedList"
        )

    def test_pop_first_doubly_linked_list(self) -> None:
        doubly_linked_list: DoublyLinkedList = DoublyLinkedList(1)
        doubly_linked_list.append(2)

        removed_node: Node = doubly_linked_list.pop_first()
        self.assertEqual(
            removed_node.value,
            1,
            "Removed node value should be 1"
        )
        self.assertEqual(
            doubly_linked_list.length,
            1,
            "Length of DoublyLinkedList should be 1"
        )
        self.assertEqual(
            doubly_linked_list.head.value,
            2,
            "Head value of DoublyLinkedList should be 2"
        )
        self.assertEqual(
            doubly_linked_list.tail.value,
            2,
            "Tail value of DoublyLinkedList should be 2"
        )

    def test_prepend_empty_doubly_linked_list(self) -> None:
        doubly_linked_list: DoublyLinkedList = DoublyLinkedList()
        doubly_linked_list.prepend(1)
        self.assertEqual(
            doubly_linked_list.length,
            1,
            "DoublyLinkedList length didn't increase"
        )
        self.assertEqual(
            doubly_linked_list.head.value,
            1,
            "DoublyLinkedList head value is not the value of the new node"
        )
        self.assertEqual(
            doubly_linked_list.tail.value,
            1,
            "DoublyLinkedList tail value is not the value of the new node"
        )

    def test_prepend_doubly_linked_list(self) -> None:
        doubly_linked_list: DoublyLinkedList = DoublyLinkedList(2)
        doubly_linked_list.prepend(1)
        self.assertEqual(
            doubly_linked_list.length,
            2,
            "DoublyLinkedList length didn't increase"
        )
        self.assertEqual(
            doubly_linked_list.head.value,
            1,
            "DoublyLinkedList head value is not the value of the new node"
        )
        self.assertEqual(
            doubly_linked_list.tail.value,
            2,
            "DoublyLinkedList tail value is not the value of the last node"
        )

    def test_pop_empty_doubly_linked_list(self) -> None:
        doubly_linked_list: DoublyLinkedList = DoublyLinkedList()
        removed_node: Node = doubly_linked_list.pop()
        self.assertEqual(
            doubly_linked_list.length,
            0,
            "DoublyLinkedList length is not 0 "
            "after pop operation on empty DoublyLinkedList."
        )
        self.assertIsNone(
            removed_node,
            "Removed node value is not None "
            "after pop operation on empty DoublyLinkedList."
        )

    def test_pop_single_node_doubly_linked_list(self) -> None:
        doubly_linked_list: DoublyLinkedList = DoublyLinkedList(1)
        removed_node: Node = doubly_linked_list.pop()
        self.assertEqual(
            doubly_linked_list.length,
            0,
            "DoublyLinkedList length is not 0 after "
            "pop operation on single node DoublyLinkedList."
        )
        self.assertIsNone(
            doubly_linked_list.head,
            "DoublyLinkedList head is not None after "
            "pop operation on single node DoublyLinkedList."
        )
        self.assertIsNone(
            doubly_linked_list.tail,
            "DoublyLinkedList tail is not None after "
            "pop operation on single node DoublyLinkedList."
        )
        self.assertIsNotNone(
            removed_node,
            "Removed node value doesn't match the "
            "expected value after pop operation on "
            "single node DoublyLinkedList."
        )

    def test_pop_doubly_linked_list(self) -> None:
        doubly_linked_list: DoublyLinkedList = DoublyLinkedList(1)
        doubly_linked_list.append(2)
        doubly_linked_list.append(3)
        removed_node: Node = doubly_linked_list.pop()
        self.assertEqual(
            doubly_linked_list.length,
            2,
            "DoublyLinkedList length doesn't match the "
            "expected value after pop operation on DoublyLinkedList."
        )
        self.assertEqual(
            removed_node.value,
            3,
            "Removed node value doesn't match the "
            "expected value after pop operation on DoublyLinkedList."
        )

    def test_append_empty_doubly_linked_list(self) -> None:
        doubly_linked_list: DoublyLinkedList = DoublyLinkedList()
        doubly_linked_list.append(1)

        self.assertEqual(
            doubly_linked_list.length,
            1,
            "DoublyLinkedList length is not 1 after append "
            "operation on empty LinkedList."
        )

        values: list[int] = []
        pointer: Node = doubly_linked_list.head
        while pointer is not None:
            values.append(pointer.value)
            pointer = pointer.next
        self.assertEqual(
            values,
            [1],
            "DoublyLinkedList values don't match "
            "the expected values after append "
            "operation on empty DoublyLinkedList."
        )

    def test_append_doubly_linked_list(self) -> None:
        doubly_linked_list: DoublyLinkedList = DoublyLinkedList(1)
        doubly_linked_list.append(2)
        doubly_linked_list.append(3)

        self.assertEqual(
            doubly_linked_list.length,
            3,
            "DoublyLinkedList length doesn't match "
            "expected value after append "
            "operation on DoublyLinkedList."
        )

        values: list[int] = []
        pointer: Node = doubly_linked_list.head
        while pointer is not None:
            values.append(pointer.value)
            pointer = pointer.next
        self.assertEqual(
            values,
            [1, 2, 3],
            "DoublyLinkedList values don't match "
            "the expected values after append "
            "operation on DoublyLinkedList."
        )

    def test_print_doubly_linked_list(self) -> None:
        doubly_linked_list: DoublyLinkedList = DoublyLinkedList(1)
        doubly_linked_list.append(2)
        doubly_linked_list.append(3)

        with patch("builtins.print") as mock_print:
            doubly_linked_list.print()
            expected_calls: list[unittest.mock.Call] = [
                unittest.mock.call(1),
                unittest.mock.call(2),
                unittest.mock.call(3)
            ]
            expected_message: str = "Print calls don't match expected calls."
            assert mock_print.mock_calls == expected_calls, expected_message


if __name__ == "__main__":
    unittest.main()
