import matplotlib.pyplot as plt
import csv
import numpy as np

def plotter(input):
    firedata = np.genfromtxt('data-fire-only.csv',delimiter=',')
    
    firedata = firedata[1:,:]
    time = (firedata[:,0] - 750002617) / 10000000

    # print(firedata[:,input])
    plt.plot(time, firedata[:,input])
    plt.show()


plotter(19)