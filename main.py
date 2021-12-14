import pandas as pd

def run():
    data = {
            'nombres' : ['Silvio', 'Joserra', 'Miguel'],
            'edades' : [26, 26, 29],
            'altura' : [1.75, 1.75, 1.70],
            'peso' : [85, 110, 100]
            }
    x = pd.DataFrame(data)
    print(x)

if __name__ == '__main__':
    run()
