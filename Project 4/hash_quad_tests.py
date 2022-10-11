import unittest
from hash_quad import *


class TestList(unittest.TestCase):
    """the following 8 tests were given initially to make sure each function works at a basic level"""

    def test_01a(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_table_size(), 7)

    def test_01b(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_num_items(), 1)

    def test_01c(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertAlmostEqual(ht.get_load_factor(), 1 / 7)

    def test_01d(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_all_keys(), ["cat"])

    def test_01e(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.in_table("cat"), True)

    def test_01f(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_value("cat"), 5)

    def test_01g(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_index("cat"), 3)

    def test_02(self):
        ht = HashTable(5)
        ht.insert("a", 0)
        self.assertEqual(ht.get_index("a"), 2)
        ht.insert("f", 0)
        self.assertEqual(ht.get_index("f"), 3)
        ht.insert("k", 0)  # causes rehash
        self.assertEqual(ht.get_index("a"), 9)
        self.assertEqual(ht.get_index("f"), 3)
        self.assertEqual(ht.get_index("k"), 8)

    def test_insert(self):
        """fully tests the insert function"""
        ht = HashTable(5)
        ht.insert("a", 6)
        ht.insert("b", 4)
        ht.insert("c", 6)
        ht.insert("d", 3)
        ht.insert("a", 3)
        ht.insert("a", 3)
        ht.insert("a", 7)
        ht.insert("a", 1)
        self.assertEqual(ht.table_size, 11)
        self.assertEqual(ht.get_index('a'), 9)
        self.assertEqual(ht.get_index('b'), 10)
        self.assertEqual(ht.get_index('c'), 0)
        self.assertEqual(ht.get_index('d'), 1)
        self.assertEqual(ht.get_value('a'), 1)
        self.assertEqual(ht.get_value('d'), 3)

    def test_horner_hash(self):
        """tests the horner hash function which computes the hash value of the key"""
        ht = HashTable(100)
        self.assertEqual(ht.horner_hash("cat"), 62)
        self.assertEqual(ht.horner_hash('a'), 97)

    def test_in_table(self):
        """tests the in_table function"""
        ht = HashTable(100)
        ht.insert('abga')
        ht.insert('asddfg')
        self.assertTrue(ht.in_table('abga'))
        self.assertTrue(ht.in_table("asddfg"))
        self.assertFalse(ht.in_table('abssdga'))

    def test_get_index(self):
        """tests that the get_index function works fully"""
        ht = HashTable(7)
        self.assertEqual(ht.get_index('as'), None)

    def test_get_all_keys(self):
        '''tests the get all keys function for the hash table'''
        ht = HashTable(115)
        ht.insert('a')
        ht.insert('a')
        ht.insert('b')
        ht.insert('c')
        ht.insert('d')
        ht.insert('e')
        ht.insert('f')
        ht.insert('h')
        self.assertEqual(ht.get_all_keys(), ['a', 'b', 'c', 'd', 'e', 'f', 'h'])

    def test_get_value(self):
        '''tests the get_value function'''
        ht = HashTable(115)
        ht.insert('a')
        ht.insert('b', 'banana')
        ht.insert('c')
        ht.insert('c', ['cat'])
        ht.insert('d', 5)
        ht.insert('d')
        ht.insert('h')
        self.assertEqual(ht.get_value('a'), None)
        self.assertEqual(ht.get_value('b'), 'banana')
        self.assertEqual(ht.get_value('c'), ['cat'])
        self.assertEqual(ht.get_value('d'), None)

    def test_num_items_table_size_lf(self):
        """tests num_items, table_size, and load_factor functions"""
        ht = HashTable(3)
        self.assertEqual(ht.get_table_size(), 3)
        ht.insert('a')
        self.assertEqual(ht.get_load_factor(), 1 / 3)
        ht.insert('b')
        ht.insert('a')
        ht.insert('a')
        self.assertEqual(ht.get_num_items(), 2)
        self.assertEqual(ht.get_table_size(), 7)
        self.assertEqual(ht.get_load_factor(), 2 / 7)
        ht.insert('aa')
        ht.insert('ad')
        self.assertEqual(ht.get_num_items(), 4)
        self.assertEqual(ht.get_table_size(), 15)
        self.assertEqual(ht.get_load_factor(), 4 / 15)
        ht.insert('ag')
        ht.insert('a')
        ht.insert('ca')
        ht.insert('bha')
        # rehashed
        ht.insert('fa')
        ht.insert('cfa')
        ht.insert('dfha')
        ht.insert('at')
        ht.insert('a')
        self.assertEqual(ht.get_num_items(), 11)
        self.assertEqual(ht.get_table_size(), 31)
        self.assertEqual(ht.get_load_factor(), 11 / 31)

    def test_07_big_oh(self):
        table = HashTable(100001)
        file = open('dictionary_a-c.txt', 'r')
        n = 0
        for line in file:
            word = line.strip()
            n += 1
            table.insert(word, word)
            self.assertTrue(table.in_table(word))
            table.get_index(word)
            self.assertEqual(table.get_value(word), word)
        file.close()


if __name__ == '__main__':
    unittest.main()
