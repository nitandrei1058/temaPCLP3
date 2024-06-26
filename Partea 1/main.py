import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
import seaborn as sns
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

def task6(data):
    bins = [0, 20, 40, 60, data['Age'].max()]
    labels = ['[0, 20]', '[21, 40]', '[41, 60]', '[61, max]']

    data['Ages'] = pd.cut(data['Age'], bins=bins, labels=labels)

    data = data[data['Sex'] == 'male']
    all_men = data['Ages'].value_counts().sort_index()

    data = data[data['Survived'] == 1]
    survived_men = data['Ages'].value_counts().sort_index()

    percent_men = survived_men / all_men
    percent_men = percent_men * 100
    percent_men.plot(kind='bar')
    plt.xticks(rotation=0)
    plt.show()

def task7(data):
    surv_c = data[data['Age'] < 18]['Survived'].mean() * 100
    surv_a = data[data['Age'] >= 18]['Survived'].mean() * 100
    print(f'How many children survived: {surv_c}%')
    print(f'How many adults survived: {surv_a}%')

    _, plot = plt.subplots()
    plot.bar(['Children', 'Adults'], [surv_c, surv_a])
    plt.show()

def task8(data):
    data['Age'] = data.groupby(['Pclass', 'Survived'])['Age'].transform(lambda x: x.fillna(x.mean()))

    for field in data.select_dtypes(include=['object']).columns:
        data[field] = data.groupby('Pclass')[field].transform(lambda x: x.fillna(x.mode()[0]))
    # decomenteaza pentru a salva datele
    # data.to_csv('DATE_TASK8.csv', index=False)

# pentru task 9
def check_title(person):
    if person['Name'] in ['Mr', 'Don', 'Sir', 'Rev', 'Dr', 'Col', 'Major', 'Capt', 'Jonkheer', 'Countess'] and person['Sex'] == 'female':
        return False
    elif person['Title'] in ['Mrs', 'Miss', 'Ms', 'Mlle', 'Lady', 'Mme'] and person['Sex'] == 'male':
        return False
    return True
    
def task9(data):
    data['Title'] = data['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
    data['Check_title'] = data.apply(check_title, axis=1)
    plt.figure(figsize=(20, 10))
    data['Title'].value_counts().plot(kind='bar')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

def task10(data):
    data['Alone'] = (data['Parch'] + data['SibSp'] == 0).astype(int)
    plt.hist([data[data['Survived'] == 1]['Alone'], data[data['Survived'] == 0]['Alone']], 
         bins=2, color=['purple', 'pink'], edgecolor='black')
    plt.legend(['Survived', 'Did not survive'])
    plt.xlabel('Stanga singur, Dreapta nu singur')
    plt.ylabel('Persoane')
    plt.xticks([0, 1])
    plt.show()

    data = data.head(100)
    sns.catplot(x='Pclass', y='Fare', hue='Survived', data=data, kind='swarm', height=8, aspect=2)
    plt.show()


def main():
    data = pd.read_csv(file)
    while True:
        print("Task:")
        input_task = input("1-10 ")
        switch = {
            '1': task1,
            '2': task2,
            '3': task3,
            '4': task4,
            '5': task5,
            '6': task6,
            '7': task7,
            '8': task8,
            '9': task9,
            '10': task10
        }
        func = switch.get(input_task)
        if func:
            func(data)
        else:
            break

if __name__ == '__main__':
    main()