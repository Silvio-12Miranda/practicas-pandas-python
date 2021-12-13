import pandas as pd

def run():
    dataset = {
            'cars' : ['bmw', 'volvo', 'ford'],
            'passing' : [3, 7, 2]
            }    
    x = pd.DataFrame(dataset)
    print(x)
    print(f'la version de pandas es: {pd.__version__}')

if __name__ == '__main__':
    run()
