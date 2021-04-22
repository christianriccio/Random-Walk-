import matplotlib.pyplot as plt
import random
import pandas as pd  
import numpy as np
import os 
import math

local_path = ''

def random_walk(n):
    x_=[0]
    y_= [0]
    step =0
    while step <n:        
        x = x_[-1] +random.uniform(0,2) #random.choice([-1,1])
        x_.append(x)
        y = y_[-1] + random.choice([-1,1]) #+random.uniform(0,2)/math.sqrt(2)
        y_.append(y)
        step+=1
    return x_, y_

def create_file(nome, p, coord):  
    path=os.path.join(p, nome)
    scrittura(path, coord)
    return path

def scrittura(path,coord):
    f =open(path, 'w')
    f.write('x\ty\n')
    for i, j in zip(coord[0],coord[1]):
        f.write(f'{str(i)}\t{str(j)}\n')
    f.close()
    
def create_df(path):
    df = pd.read_csv(path, sep = '\t')
    df = pd.DataFrame(df)
    return df

def two_dim(df):
    plt.figure()
    x,y = df['x'].values, df['y'].values
    plt.plot(x,y,marker='.',color="red")
    plt.title('Plot Bidimensionale')
    plt.xlabel('X-direction')
    plt.ylabel('Y-direction')
    plt.show()

def three_dim(df):
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    x,y,z = df['x'].values, df['y'].values, len(df)
    ax.plot3D(x,y,z,marker='.',color="red")
    plt.title('3-D Plot')
    ax.set_xlabel('X-direction')
    ax.set_ylabel('Y-direction')
    ax.set_zlabel('Number of steps')
    plt.show()      

def main():
    passi = int(input('Inserisci il numero di passi per il random walk: '))
    coordinates = random_walk(passi)
    path = create_file(input('insert file name: '), local_path, coordinates)
    dataframe = create_df(path)
    error = True
    while error:
        scelta = input('Vuoi visualizzare un grafico nello spazio o nel piano del random walk? ')
        if scelta == 'spazio' or scelta == 'Spazio':
            three_dim(dataframe)      
            error = False 
        elif scelta == 'piano' or scelta == 'Piano':
            two_dim(dataframe)  
            error = False     
        else:
            print('Scrivi meglio')

if __name__ == '__main__':
    main()
