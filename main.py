import pandas as pd
import matplotlib.pyplot as plt
def run():
    x = pd.read_csv('datacorrelacion.csv')
    x.plot(kind = 'scatter', y = 'Duration', x = 'Calories')
    plt.show()

if __name__ == '__main__':
    run()
