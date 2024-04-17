import pandas as pd

def sum_data(filename="contact_matrix.csv"):
        df = pd.read_csv(filename, index_col=0)
        return df.values.sum()
    
def min_data(filename="contact_matrix.csv"):
        df = pd.read_csv(filename, index_col=0)
        return df.values.min()

if __name__ == '__main__':
    unittest.main()