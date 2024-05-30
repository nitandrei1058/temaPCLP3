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

def task2(data):
    surv = data['Survived'].value_counts(normalize=True) * 100
    pcls = data['Pclass'].value_counts(normalize=True) * 100
    sex = data['Sex'].value_counts(normalize=True) * 100
    print(f'How many survived: {surv[1]}%')
    print(f'How many did not survive: {surv[0]}%\n')
    print(f'Passengers Class:')
    for key, value in pcls.items():
        print(f'{key}: {value}%')
    print(f"\nSex:")
    for key, value in sex.items():
        print(f'{key}: {value}%')
    
    _, plot = plt.subplots(3, 1)
    plot[0].set_title('Survival rate')
    plot[1].set_title('Passenger Class')
    plot[2].set_title('Sex')

    plot[0].bar(['Did not survive', 'Survived'], surv)
    plot[1].set_xticks(pcls.index)
    plot[1].bar(pcls.index, pcls)
    plot[2].bar(sex.index, sex)

    plt.tight_layout()
    plt.show()

def task3(data):
    num = data.select_dtypes(include=[int, float]).columns
    n = len(num)

    _, plot = plt.subplots(n, 1, figsize=(10, n * 2))
    for i, field in enumerate(num):
        plot[i].hist(data[field], bins=30, edgecolor='darkblue')
        plot[i].set_title(f'{field}')

    plt.tight_layout()
    plt.show()

def task4(data):
    for field in data.columns[data.isnull().any()].tolist():
       miss = data[field].isnull().sum()
       print(f'Column: {field}')
       print(f'Missing Values: {miss}, %: {miss / len(data) * 100}%\n')

    data_s = data[data['Survived'] == 1]
    print(f'Survived:')
    for field in data.columns[data.isnull().any()].tolist():
        miss = data_s[field].isnull().sum()
        print(f'Column: {field}')
        print(f'Missing Values: {miss}, %: {miss / len(data_s) * 100}%')
    print('\n')

    data_s = data[data['Survived'] == 0]
    print(f'Did not survive:')
    for field in data.columns[data.isnull().any()].tolist():
        miss = data_s[field].isnull().sum()
        print(f'Column: {field}')
        print(f'Missing Values: {miss}, %: {miss / len(data_s) * 100}%')
    print('\n')

def task5(data):
    bins = [0, 20, 40, 60, data['Age'].max()]
    labels = ['[0, 20]', '[21, 40]', '[41, 60]', '[61, max]']
    offset = 10
    ticks = [0 + offset, 20 + offset, 40 + offset, 60 + offset]
    data['Ages'] = pd.cut(data['Age'], bins=bins, labels=labels)

    plt.hist(data['Age'], bins=bins, edgecolor='darkblue')
    plt.xticks(ticks, labels)
    plt.show()





def main():
    data = pd.read_csv(file)


if __name__ == '__main__':
    main()