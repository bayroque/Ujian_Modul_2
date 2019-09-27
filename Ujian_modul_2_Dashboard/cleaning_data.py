import pandas as pd
import numpy as np
# import seaborn as sns

def mpg():
    df = pd.read_csv('clean.csv')
    return df

def coba():
    df = pd.read_csv('clean.csv')
    cooba1 = df[df['origin'] == 'usa']['horsepower'].sort_values(ascending=False).head(3).index
    cooba2 = df[df['origin'] == 'japan']['horsepower'].sort_values(ascending=False).head(3).index
    cooba3 = df[df['origin'] == 'europe']['horsepower'].sort_values(ascending=False).head(3).index
    lixusa = []
    for item in cooba1:
        lixusa.append(df['name'][item])
    lixjap = []
    for item in cooba2:
        lixjap.append(df['name'][item])
    lixeu = []
    for item in cooba3:
        lixeu.append(df['name'][item])
    lirank = ['Rank 1', 'Rank 2','Rank 3']
    dictjj = {
        'Ranking' : lirank,
        'usa' : lixusa,
        'japan' : lixjap,
        'europe' : lixeu
        
    }
    finale = pd.DataFrame(dictjj)
    finale.set_index('Ranking')
    return finale

def coba2():
    df = pd.read_csv('clean.csv')
    cooba1 = df[df['origin'] == 'usa']['mpg'].sort_values(ascending=False).head(3).index
    cooba2 = df[df['origin'] == 'japan']['mpg'].sort_values(ascending=False).head(3).index
    cooba3 = df[df['origin'] == 'europe']['mpg'].sort_values(ascending=False).head(3).index
    lixusa = []
    for item in cooba1:
        lixusa.append(df['name'][item])
    lixjap = []
    for item in cooba2:
        lixjap.append(df['name'][item])
    lixeu = []
    for item in cooba3:
        lixeu.append(df['name'][item])
    lirank = ['Rank 1', 'Rank 2','Rank 3']
    dictjj = {
        'Ranking' : lirank,
        'usa' : lixusa,
        'japan' : lixjap,
        'europe' : lixeu
        
    }
    finale = pd.DataFrame(dictjj)
    finale.set_index('Ranking')
    return finale
