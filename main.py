import pandas as pd

def run():
    x = pd.read_csv('datacorrelacion.csv')
    x = x.corr() 

    print(x)

if __name__ == '__main__':
    run()
