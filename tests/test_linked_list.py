import unittest
from unittest.mock import patch
from data_structures.linked_list import Node, LinkedList

class TestLinkedList(unittest.TestCase):
    def test_print_linked_list(self):
        linked_list: LinkedList = LinkedList(1)
        linked_list.head.next = Node(2)
        linked_list.head.next.next = Node(3)
        
        with patch("builtins.print") as mock_print:
            linked_list.print_linked_list()
            expected_calls = [unittest.mock.call(1), unittest.mock.call(2), unittest.mock.call(3)]
            assert mock_print.mock_calls == expected_calls, "Print calls don't match expected calls."

if __name__ == "__main__":
    unittest.main()