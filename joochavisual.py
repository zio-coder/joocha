import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.offsetbox import AnnotationBbox, AuxTransformBox
import serial
import time

board = serial.Serial('COM8', 115200)




parkinglot = [True, True, True, True, True, True]

# Here's my "image"
def emptytofill(x, y, num):
    rnew = Rectangle((x,y), 0.3, 0.3, fc='red', ec='black', lw=5)
    ax.add_artist(rnew)
    parkinglot[num-1] = False
    
def filltoempty(x, y, num):
    rnew = Rectangle((x,y), 0.3, 0.3, fc='limegreen', ec='black', lw=5)
    ax.add_artist(rnew)
    parkinglot[num-1] = True
    
def ifcarentered():
    pass
# Suppose I want to highlight some feature in the middle boxes.
fig = plt.figure()
ax = fig.add_subplot(111)

while True:
    be = Rectangle((0.4, 0.95), 0.3, 0.05, fc='cyan', ec='black', lw=5)
    enter = Rectangle((0.95, 0.4), 0.05, 0.1, fc='purple', ec='black', lw=5)
    r = [Rectangle((0.05, 0.05), 0.3, 0.3, fc='limegreen', ec='black', lw=5),
        Rectangle((0.05, 0.55), 0.3, 0.3, fc='limegreen', ec='black', lw=5),
        Rectangle((0.4, 0.55), 0.3, 0.3, fc='limegreen', ec='black', lw=5),
        Rectangle((0.4, 0.05), 0.3, 0.3, fc='limegreen', ec='black', lw=5),
        Rectangle((0.75, 0.55), 0.3, 0.3, fc='limegreen', ec='black', lw=5),
        Rectangle((0.75, 0.05), 0.3, 0.3, fc='limegreen', ec='black', lw=5)]
    ax.add_artist(r[0])
    ax.add_artist(r[1])
    ax.add_artist(r[2])
    ax.add_artist(r[3])
    ax.add_artist(r[4])
    ax.add_artist(r[5])
    ax.add_artist(be)
    ax.add_artist(enter)
    



        
        
    plt.show()

