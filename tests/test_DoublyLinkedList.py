import unittest

from LinkedLists.DoublyLinkedList import DoublyLinkedList

def list_push_many(list, *args):
    for arg in args:
        list.push(arg)

def list_append_many(list, *args):
    for arg in args:
        list.append(arg)

class TestDoublyLinkedList(unittest.TestCase):
    def test_push(self):
        list = DoublyLinkedList()
        list_push_many(list, 5, 4, 3, 2, 1)
        self.assertEqual(str(list), '[1, 2, 3, 4, 5]')

    def test_append(self):
        list = DoublyLinkedList()
        list_append_many(list, 1, 2, 3, 4, 5)
        self.assertEqual(str(list), '[1, 2, 3, 4, 5]')

    def test_remove_by_index(self):
        list = DoublyLinkedList()
        list_append_many(list, 1, 1, 1, 2, 3, 3, 3, 4, 5, 5, 5)

        list.remove_by_value(1)
        self.assertEqual(str(list), '[1, 1, 2, 3, 3, 3, 4, 5, 5, 5]')

        list.remove_by_value(1, False)
        self.assertEqual(str(list), '[2, 3, 3, 3, 4, 5, 5, 5]')

        list.remove_by_value(5)
        self.assertEqual(str(list), '[2, 3, 3, 3, 4, 5, 5]')

        list.remove_by_value(5, False)
        self.assertEqual(str(list), '[2, 3, 3, 3, 4]')

        list.remove_by_value(3)
        self.assertEqual(str(list), '[2, 3, 3, 4]')

        list.remove_by_value(3, False)
        self.assertEqual(str(list), '[2, 4]')

    def test_remove_by_value(self):
        list = DoublyLinkedList()
        list_append_many(list, 1, 1, 1, 2, 3, 3, 3, 4, 5, 5, 5)

        list.remove_by_value(1)
        self.assertEqual(str(list), '[1, 1, 2, 3, 3, 3, 4, 5, 5, 5]')

        list.remove_by_value(1, False)
        self.assertEqual(str(list), '[2, 3, 3, 3, 4, 5, 5, 5]')

        list.remove_by_value(5)
        self.assertEqual(str(list), '[2, 3, 3, 3, 4, 5, 5]')

        list.remove_by_value(5, False)
        self.assertEqual(str(list), '[2, 3, 3, 3, 4]')

        list.remove_by_value(3)
        self.assertEqual(str(list), '[2, 3, 3, 4]')

        list.remove_by_value(3, False)
        self.assertEqual(str(list), '[2, 4]')

    def test_get_by_index(self):
        list = DoublyLinkedList()
        list_append_many(list, 11, 26, 30, 49, 59, 36, 31, 44, 57, 51, 55)

        self.assertEqual(list.get_by_index(0), 11)
        self.assertEqual(list.get_by_index(1), 26)
        self.assertEqual(list.get_by_index(10), 55)

        with self.assertRaises(IndexError):
            list.get_by_index(-1)

        with self.assertRaises(IndexError):
            list.get_by_index(11)

    def test_index_of(self):
        list = DoublyLinkedList()
        list_append_many(list, 11, 26, 30, 49, 59, 36, 31, 44, 57, 51, 55)

        self.assertEqual(list.index_of(11), 0)
        self.assertEqual(list.index_of(55), 10)
        self.assertEqual(list.index_of(26), 1)

    def test_update_by_index(self):
        list = DoublyLinkedList()
        list_append_many(list, 11, 26, 30, 49, 59, 36, 31, 44, 57, 51, 55)

        list.update_by_index(0, 2)
        self.assertEqual(str(list), '[2, 26, 30, 49, 59, 36, 31, 44, 57, 51, 55]')

        list.update_by_index(1, 29)
        self.assertEqual(str(list), '[2, 29, 30, 49, 59, 36, 31, 44, 57, 51, 55]')

        list.update_by_index(10, 11)
        self.assertEqual(str(list), '[2, 29, 30, 49, 59, 36, 31, 44, 57, 51, 11]')

        list.update_by_index(9, 100)
        self.assertEqual(str(list), '[2, 29, 30, 49, 59, 36, 31, 44, 57, 100, 11]')

    def test_len(self):
        list = DoublyLinkedList()
        list_append_many(list, 11, 26, 30, 49, 59, 36, 31, 44, 57, 51, 55)

        self.assertEqual(len(list), 11)

        list.remove_by_index(0)
        self.assertEqual(len(list), 10)

        list.remove_by_index(0)
        self.assertEqual(len(list), 9)

        list.push(111)
        self.assertEqual(len(list), 10)