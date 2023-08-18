import unittest
from unittest.mock import patch
from data_structures.linked_list import Node, LinkedList

class TestLinkedList(unittest.TestCase):
    def test_prepend_empty_linked_list(self) -> None:
        linked_list: LinkedList = LinkedList()
        linked_list.prepend(1)

        self.assertEqual(linked_list.length, 1, "LinkedList length is not 1 after prepend operation on empty LinkedList.")

        values: list[int] = []
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

        values: list[int] = []
        pointer: Node = linked_list.head
        while pointer is not None:
            values.append(pointer.value)
            pointer = pointer.next
        self.assertEqual(values, [1,2,3], "LinkedList values don't match the expected values after prepend operation on LinkedList.")

    def test_append_empty_linked_list(self) -> None:
        linked_list: LinkedList = LinkedList()
        linked_list.append(1)

        self.assertEqual(linked_list.length, 1, "LinkedList length is not 1 after append operation on empty LinkedList.")

        values: list[int] = []
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

        values: list[int] = []
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

    def test_pop_first_empty_linked_list(self) -> None:
        linked_list: LinkedList = LinkedList()
        removed_node: Node = linked_list.pop_first()

        self.assertIsNone(removed_node, "Should return None when popping from an empty LinkedList.")
        self.assertEqual(linked_list.length, 0, "Length should be 0 after popping from an empty LinkedList.")
        self.assertIsNone(linked_list.head, "Head should be None after popping from an empty LinkedList.")
        self.assertIsNone(linked_list.tail, "Tail should be None after popping from an empty LinkedList.")

    def test_pop_first_linked_list(self) -> None:
        linked_list: LinkedList = LinkedList(1)
        linked_list.append(2)
        linked_list.append(3)
        removed_node: Node = linked_list.pop_first()

        self.assertEqual(removed_node.value, 1, "Value of the removed node should be 1.")
        self.assertEqual(linked_list.length, 2, "Length should be decremented after popping from a non-empty LinkedList.")
        self.assertEqual(linked_list.head.value, 2, "Head value should be updated after popping from a non-empty LinkedList.")
        self.assertEqual(linked_list.tail.value, 3, "Tail value should remain unchanged after popping from a non-empty LinkedList.")

    def test_get_invalid_index(self) -> None:
        linked_list: LinkedList = LinkedList(1)
        linked_list.append(2)
        linked_list.append(3)
        invalid_indices: list[int] = [-1, 3]
        for index in invalid_indices:
            result: Node = linked_list.get(index)
            self.assertIsNone(result, f"Index {index} should return None for LinkedList with length 3.")

    def test_get_valid_index(self) -> None:
        linked_list: LinkedList = LinkedList(1)
        linked_list.append(2)
        linked_list.append(3)
        index_value_map: dict[int, int] = {0: 1, 1: 2, 2: 3}
        for index, expected_value in index_value_map.items():
            result: Node = linked_list.get(index)
            self.assertIsNotNone(result, f"Index {index} should return a Node for LinkedList with length 3.")
            self.assertEqual(result.value, expected_value, f"Value at index {index} should be {expected_value}.")

    def test_set_invalid_index(self) -> None:
        linked_list: LinkedList = LinkedList(1)
        linked_list.append(2)
        linked_list.append(3)
        invalid_indices: list[int] = [-1, 3]
        for index in invalid_indices:
            result: bool = linked_list.set(index, 99)
            self.assertFalse(result, f"Setting value at index {index} should return False for LinkedList with length 3.")

    def test_set_valid_index(self) -> None:
        linked_list: LinkedList = LinkedList(1)
        linked_list.append(2)
        linked_list.append(3)
        valid_indices: list[int] = [0, 1, 2]
        for index in valid_indices:
            result: bool = linked_list.set(index, 99)
            self.assertTrue(result, f"Setting value at index {index} should return True for LinkedList with length 3.")
            self.assertEqual(linked_list.get(index).value, 99, f"Value at index {index} should be updated to 99.")

    def test_insert_invalid_index(self) -> None:
        linked_list: LinkedList = LinkedList(1)
        linked_list.append(2)
        linked_list.append(3)
        invalid_indices: list[int] = [-1, 4]
        for index in invalid_indices:
            result: bool = linked_list.insert(index, 99)
            self.assertFalse(result, f"Insert value at index {index} should return False for LinkedList with length 3.")

    def test_insert_at_first_node(self) -> None:
        linked_list: LinkedList = LinkedList(1)
        linked_list.append(2)
        result: bool = linked_list.insert(0, 99)
        self.assertTrue(result, "Inserting at the first node should return True.")
        self.assertEqual(linked_list.get(0).value, 99, "Value at the first node should be 99.")
        self.assertEqual(linked_list.get(1).value, 1, "Value at the second node should remain unchanged.")

    def test_insert_at_last_node(self) -> None:
        linked_list: LinkedList = LinkedList(1)
        linked_list.append(2)
        result: bool = linked_list.insert(2, 99)
        self.assertTrue(result, "Inserting at the last node should return True.")
        self.assertEqual(linked_list.get(1).value, 2, "Value at the second-to-last node should be 2.")
        self.assertEqual(linked_list.get(2).value, 99, "Value at the last node should be 99.")

    def test_insert_at_middle_node(self) -> None:
        linked_list: LinkedList = LinkedList(1)
        linked_list.append(2)
        linked_list.append(3)
        result: bool = linked_list.insert(1, 99)
        self.assertTrue(result, "Inserting at a middle node should return True.")
        self.assertEqual(linked_list.get(1).value, 99, "Value at second node should be 99.")
        self.assertEqual(linked_list.get(2).value, 2, "Value at third node should be 2.")

    def test_remove_invalid_index(self) -> None:
        linked_list: LinkedList = LinkedList(1)
        linked_list.append(2)
        linked_list.append(3)
        invalid_indices: list[int] = [-1, 4]
        for index in invalid_indices:
            result: Node = linked_list.remove(index)
            self.assertIsNone(result, f"Removing at index {index} should return None for LinkedList with length 3.")

    def test_remove_first_node(self) -> None:
        linked_list: LinkedList = LinkedList(1)
        linked_list.append(2)
        linked_list.append(3)
        result: Node = linked_list.remove(0)
        self.assertEqual(result.value, 1, "Removed value should be 1.")
        self.assertEqual(linked_list.length, 2, "Length should be decremented after removing the first node.")
        self.assertEqual(linked_list.get(0).value, 2, "Value at the first node should be updated.")

    def test_remove_last_node(self) -> None:
        linked_list: LinkedList = LinkedList(1)
        linked_list.append(2)
        linked_list.append(3)
        result: Node = linked_list.remove(2)
        self.assertEqual(result.value, 3, "Removed value should be 3.")
        self.assertEqual(linked_list.length, 2, "Length should be decremented after removing the last node.")
        self.assertEqual(linked_list.get(1).value, 2, "Value at the second-to-last node should remain the same.")

    def test_remove_middle_node(self) -> None:
        linked_list: LinkedList = LinkedList(1)
        linked_list.append(2)
        linked_list.append(3)
        result: Node = linked_list.remove(1)
        self.assertEqual(result.value, 2, "Removed value should be 2.")
        self.assertEqual(linked_list.length, 2, "Length should be decremented after removing a middle node.")
        self.assertEqual(linked_list.get(1).value, 3, "Value at the second node should be updated.") 

    def test_print_linked_list(self) -> None:
        linked_list: LinkedList = LinkedList(1)
        linked_list.append(2)
        linked_list.append(3)
        
        with patch("builtins.print") as mock_print:
            linked_list.print_linked_list()
            expected_calls = [unittest.mock.call(1), unittest.mock.call(2), unittest.mock.call(3)]
            assert mock_print.mock_calls == expected_calls, "Print calls don't match expected calls."

if __name__ == "__main__":
    unittest.main()