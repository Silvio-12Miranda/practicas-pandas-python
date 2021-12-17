import pandas as pd

def run():
    x = pd.read_csv('dirtydata.csv')
    #x.dropna(inplace = True)
    #x.fillna(1, inplace = True)
    #x['Calories'].fillna('VALUE', inplace = True)
    x['Date'] = pd.to_datetime(x['Date'])
    x.dropna(subset = ['Date'], inplace = True)
    x.loc[7, 'Duration'] = 45

    for i in x.index:
        if x.loc[i, 'Duration'] > 120:
            x.loc[i, 'Duration'] = 120
    for i in x.index:
        if x.loc[i, 'Duration'] < 60:
            x.drop(i, inplace = True)

    #x = x.duplicated()
    x.drop_duplicates(inplace = True)

    print(x)

if __name__ == '__main__':
    run()
