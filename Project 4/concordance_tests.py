import unittest
import subprocess
from concordance import *
import hash_quad

class TestList(unittest.TestCase):


    def test_01(self):
        """tests the concordance function on file1.txt"""
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("file1.txt")
        conc.write_concordance("file1_con.txt")
        err = subprocess.call("FC file1_con.txt file1_sol.txt", shell = True)
        self.assertEqual(err, 0)

        
    def test_02(self):
        """tests the concordance function on file1.txt"""
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("file2.txt")
        conc.write_concordance("file2_con.txt")
        err = subprocess.call("FC file2_con.txt file2_sol.txt", shell = True)
        self.assertEqual(err, 0)

        
    def test_03(self):
        """tests the concordance function on declaration.txt"""
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("declaration.txt")
        conc.write_concordance("declaration_con.txt")
        err = subprocess.call("FC declaration_con.txt declaration_sol.txt", shell = True)
        self.assertEqual(err, 0)

    def test_sample(self):
        """test the concordance function on sample.txt"""
        conc = Concordance()
        conc.load_stop_table("sample_stop_words.txt")
        conc.load_concordance_table("sample.txt")
        conc.write_concordance("sample_con.txt")
        err = subprocess.call("FC sample_con.txt sample_sol.txt", shell = True)
        self.assertEqual(err, 0)

    def test_07(self):
        conc = Concordance()
        conc.load_stop_table("stop_words.txt")
        conc.load_concordance_table("War_And_Peace.txt")
        conc.write_concordance('War_And_Peace_con.txt')
        err = subprocess.call("FC War_And_Peace_con.txt War_And_Peace_sol.txt", shell = True)
        self.assertEqual(err, 0)


if __name__ == '__main__':
    unittest.main()
