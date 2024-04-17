import unittest

import pandas_script

class TestScript(unittest.TestCase):

    def test_open(self):
        n = pandas_script.sum_data()
        self.assertTrue(n >= 0)
    
    def test_sum(self):
        n = pandas_script.sum_data()
        # We know this should be above 400
        self.assertTrue(n >= 400)
        
    def test_min(self):
        n = pandas_script.min_data()
        # should be less than 0.05 
        self.assertTrue(n < 0.05)

if __name__ == '__main__':
    unittest.main()