import unittest

class TestPandasReading(unittest.TestCase):

    def test_numeric(self):
        import pandas as pd
        import numpy as np
        df = pd.read_csv("contact_matrix.csv", index_col=0)
        pd.to_numeric(df.values.ravel())
        self.assertTrue(all(df >= 0))
    
    def test_mean(self):
        import pandas as pd
        import numpy as np
        df = pd.read_csv("contact_matrix.csv", index_col=0)
        self.assertEqual(round(df.mean().mean(), 15), round(df.values.mean(), 15))

#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())

#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)

if __name__ == '__main__':
    unittest.main()