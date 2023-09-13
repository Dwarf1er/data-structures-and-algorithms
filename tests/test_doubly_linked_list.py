import unittest
from unittest.mock import patch
from data_structures.doubly_linked_list import Node, DoublyLinkedList


class TestDoublyLinkedList(unittest.TestCase):
    def test_constructor_empty_doubly_linked_list(self) -> None:
        doubly_linked_list: DoublyLinkedList = DoublyLinkedList()
        self.assertEqual(
            doubly_linked_list.length,
            0,
            "Expected an empty DoublyLinkedList to have length 0."
        )
        self.assertIsNone(
            doubly_linked_list.head,
            "Expected an empty DoublyLinkedList to have a None head."
        )
        self.assertIsNone(
            doubly_linked_list.tail,
            "Expected an empty DoublyLinkedList to have a None tail."
        )

    def test_constructor_with_initial_value(self) -> None:
        doubly_linked_list: DoublyLinkedList = DoublyLinkedList(1)
        self.assertEqual(
            doubly_linked_list.length,
            1,
            "Expected a DoublyLinkedList with initial value to have length 1."
        )
        self.assertEqual(
            doubly_linked_list.head.value,
            1,
            "Expected the head value to match the initial value."
        )
        self.assertEqual(
            doubly_linked_list.tail.value,
            1,
            "Expected the tail value to match the initial value."
        )

    def test_get_invalid_index_doubly_linked_list(self) -> None:
        doubly_linked_list: DoublyLinkedList = DoublyLinkedList(1)
        result: Node = doubly_linked_list.get(-1)
        self.assertEqual(
            result,
            None,
            "Getting a node at index < 0 should return None"
        )

        result = doubly_linked_list.get(2)
        self.assertEqual(
            result,
            None,
            "Getting a node at index >= length should return None"
        )

    def test_get_first_node_doubly_linked_list(self) -> None:
        doubly_linked_list: DoublyLinkedList = DoublyLinkedList(1)
        doubly_linked_list.append(2)

        result: Node = doubly_linked_list.get(0)
        self.assertEqual(
            result.value,
            1,
            "Getting node at index 0 should return 1"
        )

    def test_get_middle_node_doubly_linked_list(self) -> None:
        doubly_linked_list: DoublyLinkedList = DoublyLinkedList(1)
        doubly_linked_list.append(2)
        doubly_linked_list.append(3)

        result: Node = doubly_linked_list.get(1)
        self.assertEqual(
            result.value,
            2,
            "Getting node at middle index should return 2"
        )

    def test_get_last_node_doubly_linked_list(self) -> None:
        doubly_linked_list: DoublyLinkedList = DoublyLinkedList(1)
        doubly_linked_list.append(2)
        doubly_linked_list.append(3)

        result: Node = doubly_linked_list.get(2)
        self.assertEqual(
            result.value,
            3,
            "Getting node at last index should return 3"
        )

    def test_set_value_invalid_index(self) -> None:
        doubly_linked_list: DoublyLinkedList = DoublyLinkedList(1)
        doubly_linked_list.append(2)
        doubly_linked_list.append(3)
        invalid_indices: list[int] = [-1, 3]
        for index in invalid_indices:
            result: bool = doubly_linked_list.set_value(index, 99)
            self.assertFalse(
                result,
                f"Setting value at index {index} should return "
                "False for DoublyLinkedList with length 3."
            )

    def test_set_value_valid_index(self) -> None:
        doubly_linked_list: DoublyLinkedList = DoublyLinkedList(1)
        doubly_linked_list.append(2)
        doubly_linked_list.append(3)
        valid_indices: list[int] = [0, 1, 2]
        for index in valid_indices:
            result: bool = doubly_linked_list.set_value(index, 99)
            self.assertTrue(
                result,
                f"Setting value at index {index} should return "
                "True for DoublyLinkedList with length 3."
            )
            self.assertEqual(
                doubly_linked_list.get(index).value,
                99,
                f"Value at index {index} should be updated to 99."
            )

    def test_insert_invalid_index(self) -> None:
        doubly_linked_list: DoublyLinkedList = DoublyLinkedList(1)

        result = doubly_linked_list.insert(-1, 0)
        self.assertFalse(
            result,
            "Value should not be inserted out of bounds"
        )

        result = doubly_linked_list.insert(doubly_linked_list.length + 1, 0)
        self.assertFalse(
            result,
            "Value should not be inserted out of bounds"
        )

    def test_insert_first_node(self) -> None:
        doubly_linked_list: DoublyLinkedList = DoublyLinkedList(1)

        result = doubly_linked_list.insert(0, 0)
        self.assertTrue(
            result,
            "Value should be inserted at index 0"
        )
        self.assertEqual(
            doubly_linked_list.head.value,
            0,
            "Value at index 0 should be 0"
        )

    def test_insert(self) -> None:
        doubly_linked_list: DoublyLinkedList = DoublyLinkedList(1)
        doubly_linked_list.append(3)

        result = doubly_linked_list.insert(1, 2)
        self.assertTrue(
            result,
            "Value should be inserted at index 1"
        )
        self.assertEqual(
            doubly_linked_list.get(1).value,
            2,
            "Value at index 1 should be 2"
        )

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
