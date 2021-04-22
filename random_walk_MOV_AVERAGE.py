import matplotlib.pyplot as plt
import random
import pandas as pd  
import time 
import os 
import numpy as np

def walk(n=1000):
  '''random walk in one dimension the direction is +1 or -1 and the step length change into [0, 2]'''
    y_= [0]
    passo =0
    while passo <n:
        y = y_[-1] + random.choice([-1,1]) * random.uniform(0,2)
        y_.append(y)
        passo+=1
    return y_

def file_(nome):
  '''create a file where to write the step'''
    f=open(nome,'w')
    f.close()

def scrittura(path, y):
  '''write the cordinates of the walk into the file'''
    f =open(path, 'a')
    f.write('y\n')
    for i in y:
        f.write(f'{str(i)}\n')
    f.close()    
    
def create_df(path):
  '''read the file and create a dataframe'''
    df = pd.read_csv(path, sep = '\t')
    return df

def media(lista, window_size):
  '''moving average for the random walk'''
    numbers_series = pd.Series(lista)
    windows = numbers_series.rolling(window_size)
    moving_averages = windows.mean()
    moving_averages_list = moving_averages.tolist()
    return moving_averages_list

def grafico(df):
  '''simple plot'''
    plt.figure(figsize=(8,4))
    plt.plot(df, marker='.', color='red')
    plt.show()

def main():
    local_path = ''
    window_size = 10
    l= walk(100)
    file_('fil')
    scrittura(local_path, l)
    dataframe = create_df(local_path)
    grafico(dataframe)
    lista = media(l,window_size)

    print('Sto plottando la media in funzione del numero di passi ')
    grafico(lista)
    plt.figure(figsize=(8,4))
    '''Here the overlap of the random walk and its moving average'''
    fig, ax = plt.subplots()
    ax.plot(dataframe, label='Random walk')
    ax.plot(lista, label='Moving average')
    ax.set_xlabel('number of steps')
    ax.set_ylabel('random walk ')
    plt.legend()
    plt.title('Grafici sovrapposti')
    plt.show()
main()
