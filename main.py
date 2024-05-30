import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
matplotlib.use('TkAgg')
file = 'train.csv'

def task1(data):
    n = len(data.columns)
    m = len(data)
    types = data.dtypes
    miss = data.isnull().sum()
    dup = data.duplicated().sum()
    print(f'Number of columns: {n}\n')
    print(f'Data types:\n')
    print(f'{types}\n')
    print(f'Missing values:')
    print(f'{miss}\n')
    print(f'Number of rows: {m}\n')
    print(f'Duplicates: {dup}')









def main():
    data = pd.read_csv(file)


if __name__ == '__main__':
    main()