import unittest
from unittest.mock import patch
from data_structures.linked_list import Node, LinkedList


class TestLinkedList(unittest.TestCase):
    def test_constructor_empty_linked_list(self) -> None:
        linked_list: LinkedList = LinkedList()
        self.assertEqual(
            linked_list.length,
            0,
            "Expected an empty LinkedList to have length 0."
        )
        self.assertIsNone(
            linked_list.head,
            "Expected an empty LinkedList to have a None head."
        )
        self.assertIsNone(
            linked_list.tail,
            "Expected an empty LinkedList to have a None tail."
        )

    def test_constructor_with_initial_value(self) -> None:
        linked_list: LinkedList = LinkedList(1)
        self.assertEqual(
            linked_list.length,
            1,
            "Expected a LinkedList with initial value to have length 1."
        )
        self.assertEqual(
            linked_list.head.value,
            1,
            "Expected the head value to match the initial value."
        )
        self.assertEqual(
            linked_list.tail.value,
            1,
            "Expected the tail value to match the initial value."
        )

    def test_prepend_empty_linked_list(self) -> None:
        linked_list: LinkedList = LinkedList()
        linked_list.prepend(1)

        self.assertEqual(
            linked_list.length,
            1,
            "Expected the length of the LinkedList to be 1 after prepend operation."
        )
        self.assertEqual(
            linked_list.head.value,
            1,
            "Expected the head value to match the value added with prepend."
        )
        self.assertEqual(
            linked_list.tail.value,
            1,
            "Expected the tail value to match the value added with prepend."
        )

    def test_prepend_linked_list(self) -> None:
        linked_list: LinkedList = LinkedList(2)
        linked_list.append(3)
        linked_list.prepend(1)

        self.assertEqual(
            linked_list.length,
            3,
            "Expected the length of the LinkedList to be 3 after prepend operation."
        )
        self.assertEqual(
            linked_list.head.value,
            1,
            "Expected the head value to match the value added with prepend."
        )
        self.assertEqual(
            linked_list.tail.value,
            3,
            "Expected the tail value to match the previous tail value."
        )

    def test_append_empty_linked_list(self) -> None:
        linked_list: LinkedList = LinkedList()
        linked_list.append(1)

        self.assertEqual(
            linked_list.length,
            1,
            "Expected the length of the LinkedList to be 1 after append operation."
        )
        self.assertEqual(
            linked_list.head.value,
            1,
            "Expected the head value to match the value added with append."
        )
        self.assertEqual(
            linked_list.tail.value,
            1,
            "Expected the tail value to match the value added with append."
        )

    def test_append_linked_list(self) -> None:
        linked_list: LinkedList = LinkedList(1)
        linked_list.append(2)
        linked_list.append(3)

        self.assertEqual(
            linked_list.length,
            3,
            "Expected the length of the LinkedList to be 3 after append operation."
        )
        self.assertEqual(
            linked_list.head.value,
            1,
            "Expected the head value to match the previous head value."
        )
        self.assertEqual(
            linked_list.tail.value,
            3,
            "Expected the tail value to match the value added with append."
        )

    def test_pop_empty_linked_list(self) -> None:
        linked_list: LinkedList = LinkedList()
        removed_node: Node = linked_list.pop()
        self.assertEqual(
            linked_list.length,
            0,
            "Expected the length to be 0 after pop operation on empty LinkedList."
        )
        self.assertIsNone(
            removed_node,
            "Expected removed node to be None after pop operation on empty LinkedList."
        )

    def test_pop_single_node_linked_list(self) -> None:
        linked_list: LinkedList = LinkedList(1)
        removed_node: Node = linked_list.pop()
        self.assertEqual(
            linked_list.length,
            0,
            "Expected the length to be 0 after pop operation on single node LinkedList."
        )
        self.assertIsNone(
            linked_list.head,
            "Expected head to be None after pop operation on single node LinkedList."
        )
        self.assertIsNone(
            linked_list.tail,
            "Expected tail to be None after pop operation on single node LinkedList."
        )
        self.assertIsNotNone(
            removed_node,
            "Expected removed node to have a value after pop operation on single node LinkedList."
        )

    def test_pop_linked_list(self) -> None:
        linked_list: LinkedList = LinkedList(1)
        linked_list.append(2)
        linked_list.append(3)
        removed_node: Node = linked_list.pop()
        self.assertEqual(
            linked_list.length,
            2,
            "Expected the length to be 2 after pop operation on LinkedList."
        )
        self.assertEqual(
            removed_node.value,
            3,
            "Expected removed node value to be 3 after pop operation on LinkedList."
        )

    def test_pop_first_empty_linked_list(self) -> None:
        linked_list: LinkedList = LinkedList()
        removed_node: Node = linked_list.pop_first()
        self.assertIsNone(
            removed_node,
            "Expected None when popping from an empty LinkedList."
        )
        self.assertEqual(
            linked_list.length,
            0,
            "Expected length to be 0 after popping from an empty LinkedList."
        )
        self.assertIsNone(
            linked_list.head,
            "Expected head to be None after popping from an empty LinkedList."
        )
        self.assertIsNone(
            linked_list.tail,
            "Expected tail to be None after popping from an empty LinkedList."
        )

    def test_pop_first_linked_list(self) -> None:
        linked_list: LinkedList = LinkedList(1)
        linked_list.append(2)
        linked_list.append(3)
        removed_node: Node = linked_list.pop_first()

        self.assertEqual(
            removed_node.value,
            1,
            "Expected value of the removed node to be 1."
        )
        self.assertEqual(
            linked_list.length,
            2,
            "Expected length to be decremented after popping from a non-empty LinkedList."
        )
        self.assertEqual(
            linked_list.head.value,
            2,
            "Expected head value to be updated after popping from a non-empty LinkedList."
        )
        self.assertEqual(
            linked_list.tail.value,
            3,
            "Expected tail value to remain unchanged after popping from a non-empty LinkedList."
        )

    def test_get_invalid_index(self) -> None:
        linked_list: LinkedList = LinkedList(1)
        linked_list.append(2)
        linked_list.append(3)
        invalid_indices: list[int] = [-1, 3]
        for index in invalid_indices:
            result: Node = linked_list.get(index)
            self.assertIsNone(
                result,
                f"Expected index {index} to return None for LinkedList with length 3."
            )

    def test_get_valid_index(self) -> None:
        linked_list: LinkedList = LinkedList(1)
        linked_list.append(2)
        linked_list.append(3)
        index_value_map: dict[int, int] = {0: 1, 1: 2, 2: 3}
        for index, expected_value in index_value_map.items():
            result: Node = linked_list.get(index)
            self.assertIsNotNone(
                result,
                f"Expected index {index} to return a Node for LinkedList with length 3."
            )
            self.assertEqual(
                result.value,
                expected_value,
                f"Expected value at index {index} to be {expected_value}."
            )

    def test_set_value_invalid_index(self) -> None:
        linked_list: LinkedList = LinkedList(1)
        linked_list.append(2)
        linked_list.append(3)
        invalid_indices: list[int] = [-1, 3]
        for index in invalid_indices:
            result: bool = linked_list.set_value(index, 99)
            self.assertFalse(
                result,
                f"Expected setting value at index {index} to return False for LinkedList with length 3."
            )

    def test_set_value_valid_index(self) -> None:
        linked_list: LinkedList = LinkedList(1)
        linked_list.append(2)
        linked_list.append(3)
        valid_indices: list[int] = [0, 1, 2]
        for index in valid_indices:
            result: bool = linked_list.set_value(index, 99)
            self.assertTrue(
                result,
                f"Expected setting value at index {index} to return True for LinkedList with length 3."
            )
            self.assertEqual(
                linked_list.get(index).value,
                99,
                f"Expected value at index {index} to be updated to 99."
            )

    def test_insert_invalid_index(self) -> None:
        linked_list: LinkedList = LinkedList(1)
        linked_list.append(2)
        linked_list.append(3)
        invalid_indices: list[int] = [-1, 4]
        for index in invalid_indices:
            result: bool = linked_list.insert(index, 99)
            self.assertFalse(
                result,
                f"Expected inserting value at index {index} to return False for LinkedList with length 3."
            )

    def test_insert_at_first_node(self) -> None:
        linked_list: LinkedList = LinkedList(1)
        linked_list.append(2)
        result: bool = linked_list.insert(0, 99)
        self.assertTrue(
            result,
            "Expected inserting at the first node to return True."
        )
        self.assertEqual(
            linked_list.get(0).value,
            99,
            "Expected value at the first node to be 99."
        )
        self.assertEqual(
            linked_list.get(1).value,
            1,
            "Expected value at the second node to remain unchanged."
        )

    def test_insert_at_last_node(self) -> None:
        linked_list: LinkedList = LinkedList(1)
        linked_list.append(2)
        result: bool = linked_list.insert(2, 99)
        self.assertTrue(
            result,
            "Expected inserting at the last node to return True."
        )
        self.assertEqual(
            linked_list.get(1).value,
            2,
            "Expected value at the second-to-last node to be 2."
        )
        self.assertEqual(
            linked_list.get(2).value,
            99,
            "Expected value at the last node to be 99."
        )

    def test_insert_at_middle_node(self) -> None:
        linked_list: LinkedList = LinkedList(1)
        linked_list.append(2)
        linked_list.append(3)
        result: bool = linked_list.insert(1, 99)
        self.assertTrue(
            result,
            "Expected inserting at a middle node to return True."
        )
        self.assertEqual(
            linked_list.get(1).value,
            99,
            "Expected value at second node to be 99."
        )
        self.assertEqual(
            linked_list.get(2).value,
            2,
            "Expected value at third node to be 2."
        )

    def test_remove_invalid_index(self) -> None:
        linked_list: LinkedList = LinkedList(1)
        linked_list.append(2)
        linked_list.append(3)
        invalid_indices: list[int] = [-1, 4]
        for index in invalid_indices:
            result: Node = linked_list.remove(index)
            self.assertIsNone(
                result,
                f"Expected removing at index {index} to return None for LinkedList with length 3."
            )

    def test_remove_first_node(self) -> None:
        linked_list: LinkedList = LinkedList(1)
        linked_list.append(2)
        linked_list.append(3)
        result: Node = linked_list.remove(0)
        self.assertEqual(
            result.value,
            1,
            "Expected removed value to be 1."
        )
        self.assertEqual(
            linked_list.length,
            2,
            "Expected length to be decremented after removing the first node."
        )
        self.assertEqual(
            linked_list.get(0).value,
            2,
            "Expected value at the first node to be updated."
        )

    def test_remove_last_node(self) -> None:
        linked_list: LinkedList = LinkedList(1)
        linked_list.append(2)
        linked_list.append(3)
        result: Node = linked_list.remove(2)
        self.assertEqual(
            result.value,
            3,
            "Expected removed value to be 3."
        )
        self.assertEqual(
            linked_list.length,
            2,
            "Expected length to be decremented after removing the last node."
        )
        self.assertEqual(
            linked_list.get(1).value,
            2,
            "Expected value at the second-to-last node to remain the same."
        )

    def test_remove_middle_node(self) -> None:
        linked_list: LinkedList = LinkedList(1)
        linked_list.append(2)
        linked_list.append(3)
        result: Node = linked_list.remove(1)
        self.assertEqual(
            result.value,
            2,
            "Expected removed value to be 2."
        )
        self.assertEqual(
            linked_list.length,
            2,
            "Expected length to be decremented after removing a middle node."
        )
        self.assertEqual(
            linked_list.get(1).value,
            3,
            "Expected value at the second node to be updated."
        )

    def test_reverse_empty_linked_list(self):
        linked_list: LinkedList = LinkedList()
        linked_list.reverse()
        self.assertIsNone(
            linked_list.head,
            "Expected reversing an empty LinkedList to result in a None head."
        )
        self.assertIsNone(
            linked_list.tail,
            "Expected reversing an empty LinkedList to result in a None tail."
        )
        self.assertEqual(
            linked_list.length,
            0,
            "Expected length of an empty LinkedList to remain 0 after reversing."
        )

    def test_reverse_one_node_linked_list(self):
        linked_list: LinkedList = LinkedList(1)
        linked_list.reverse()
        self.assertEqual(
            linked_list.head.value,
            1,
            "Expected head value of a LinkedList with one node to remain unchanged."
        )
        self.assertEqual(
            linked_list.tail.value,
            1,
            "Expected tail value of a LinkedList with one node to remain unchanged."
        )
        self.assertEqual(
            linked_list.length,
            1,
            "Expected length of a LinkedList with one node to remain 1 after reversing."
        )

    def test_reverse_linked_list(self):
        linked_list: LinkedList = LinkedList()
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.reverse()
        self.assertEqual(
            linked_list.head.value,
            3,
            "Expected head value to be updated to the last node's value after reversing."
        )
        self.assertEqual(
            linked_list.tail.value,
            1,
            "Expected tail value to be updated to the first node's value after reversing."
        )
        self.assertEqual(
            linked_list.length,
            3,
            "Expected length of a LinkedList with multiple nodes to remain unchanged after reversing."
        )

    def test_print_linked_list(self) -> None:
        linked_list: LinkedList = LinkedList(1)
        linked_list.append(2)
        linked_list.append(3)

        with patch("builtins.print") as mock_print:
            linked_list.print()
            expected_calls: list[unittest.mock.Call] = [
                unittest.mock.call(1),
                unittest.mock.call(2),
                unittest.mock.call(3)
            ]
            self.assertEqual(
                mock_print.mock_calls,
                expected_calls,
                "Print calls don't match expected calls."
            )


if __name__ == "__main__":
    unittest.main()
