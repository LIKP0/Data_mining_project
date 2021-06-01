import pandas as pd
import random

if __name__ == "__main__":
    js = pd.read_json('busRoutines.json')
    print(len(js['coords']))
