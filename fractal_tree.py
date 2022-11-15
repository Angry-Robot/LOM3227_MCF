import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt

#N: número de pontos na órbita
n = 100000 # cuidado para não aumentar muito N! Pode consumir toda a memória

#t = [ a b e, c d f, 0 0 1 ]
#t = [ a  b  e ,
#      c  d  f ,
#      0  0  1 ]
a = np.array([[0.05, 0, 0], [0, 0.6, 0], [0, 0, 1]])                #Resize of 0.05 in x and 0.6 in y
b = np.array([[0.05, 0, 0], [0, -0.5, 1], [0, 0, 1]])               #Resize of 0.05 in x and -0.5 in y and translade y by 1
c = np.array([[0.46, -0.32, 0], [0.39, 0.38, 0.6], [0, 0, 1]])      #Resize of 0.46 in x and 0.38 in y, shear by -0.32 in x and 0.39 in y, and translade y by 0.6
d = np.array([[0.47, -0.154, 0], [0.171, 0.423, 1.1], [0, 0, 1]])   #Resize of 0.47 in x and 0.423 in y, shear by -0.154 in x and 0.171 in y, and translade y by 1.1
e = np.array([[0.433, 0.275, 0], [-0.25, 0.476, 1], [0, 0, 1]])     #Resize of 0.433 in x and 0.476 in y, shear by 0.275 in x and -0.25 in y, and translade y by 1
f = np.array([[0.421, 0.257, 0], [-0.353, 0.306, 0.7], [0, 0, 1]])  #Resize of 0.421 in x and 0.306 in y, shear by 0.257 in x and -0.353 in y, and translade y by 0.7

def move(p0):
    r = rd.randint(6)  #gera aleatoriamente um dos inteiros 0, 1, 2
    if r == 0:         #transforma a
        p = a.dot(p0)
    elif r == 1:       #transforma b
        p = b.dot(p0)
    elif r == 2:       #transforma c
        p = c.dot(p0)
    elif r == 3:       #transforma d
        p = d.dot(p0)
    elif r == 4:       #transforma e
        p = e.dot(p0)
    else:              #transforma f
        p = f.dot(p0)
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

#cálculo da órbita
for i in range(1, n):   #Just loops from 1 to N
    orbita[i] = move(orbita[i-1])   #i moves this bitch in lines, so three 1's by three 1's.

x=1
y=2
#gráfico
plt.figure()
ax = plt.axes()
ax.set_xlim(-x,x)
ax.set_ylim(0,y)
ax.set_aspect(1)
ax.plot(orbita[:, 0], orbita[:, 1], ',')    #"," = "dot" = apenas um pixel
plt.show()