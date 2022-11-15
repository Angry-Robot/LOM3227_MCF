import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt
import imageio
import os

# N: número de pontos na órbita
n = 1000000 # cuidado para não aumentar muito N! Pode consumir toda a memória

#t = [ a b e, c d f, 0 0 1 ]
#t = [ a  b  e ,
#      c  d  f ,
#      0  0  1 ]
a = np.array([[0.5, 0, 0], [0, 0.5, 0], [0, 0, 1]])         #Resize of 0.5 in both axis
b = np.array([[0.5, 0, 0.5], [0, 0.5, 0], [0, 0, 1]])       #Resize of 0.5 in both axis and translades by 0.5 in x
c = np.array([[0.5, 0, 0.25], [0, 0.5, 0.433], [0, 0, 1]])  #Resize of 0.5 in both axis and translades by 0.25 in x and 0.433 in y

def move(p0):
    r = rd.randint(3)  # gera aleatoriamente um dos inteiros 0, 1, 2
    if r == 0:  # escolho A
        p = a.dot(p0)
    elif r == 1:  # escolho B
        p = b.dot(p0)
    else:  # escolho C
        p = c.dot(p0)
    return p

# array que conterá a órbita
orbita = np.ones((n, 3))   #Creates an array of N by 3.
#1 1 1, i = 0
#1 1 1, i = 1
#1 1 1, i = 2
#1 1 1, i = 3
#1 1 1, i = 4
# ...
#1 1 1, i = N

# cálculo da órbita
for i in range(1, n):   #Just loops from 1 to N
    orbita[i] = move(orbita[i-1])   #i moves this bitch in lines, so three 1's by three 1's.

# for k in range(10,0,-1):
#     x=k/10
#     y=k/10
#     # gráfico
#     plt.figure()
#     ax = plt.axes()
#     ax.set_xlim(0,x)
#     ax.set_ylim(0,y)
#     ax.set_aspect(1)
#     ax.plot(orbita[:, 0], orbita[:, 1], ',')    #"," = "dot" = apenas um pixel
#     plt.show()

filenames = []
for k in range(40,20,-1):
    # plot the line chart
    x=k/50
    y=k/50
    # gráfico
    plt.figure()
    ax = plt.axes()
    ax.axes.xaxis.set_visible(False)
    ax.axes.yaxis.set_visible(False)   
    ax.set_xlim(0,x)
    ax.set_ylim(0,y)
    ax.set_aspect(1)
    ax.plot(orbita[:, 0], orbita[:, 1], ',')    #"," = "dot" = apenas um pixel
    # plt.show()
    
    # Create file name and append it to a list
    filename = f'{k}.png'
    filenames.append(filename)
    plt.savefig(filename)   # save frame
    plt.close()
# Append all images and assemble the gif
with imageio.get_writer('mygif.gif', mode='I') as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)
# Remove the temporary image files
for filename in set(filenames):
    os.remove(filename)