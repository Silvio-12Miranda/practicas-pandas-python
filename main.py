import pandas as pd

def run():
    #pd.options.display.max_row = 1000
    x = pd.read_json('datajs.js')
    print(x)

if __name__ == '__main__':
    run()
