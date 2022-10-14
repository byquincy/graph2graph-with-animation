import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import random
import time

speedGraph=[0, 0, 0.1, 0.2, 0.4, 0.6, 0.9, 1.3, 1.7, 2.3, 2.9, 3.7, 4.6, 5.7, 6.9, 8.4, 10.1, 12.1, 14.5, 17.2, 20.4, 24.0, 28.0, 32.3, 36.6, 40.7, 44.7, 48.3, 51.6, 54.7, 57.5, 60.0, 62.4, 64.6, 66.6, 68.4, 70.2, 71.8, 73.3, 74.8, 76.1, 77.4, 78.6, 79.7, 80.8, 81.8, 82.7, 83.7, 84.5, 85.4, 86.2, 86.9, 87.6, 88.3, 89.0, 89.6, 90.2, 90.7, 91.3, 91.8, 92.3, 92.8, 93.2, 93.6, 94.0, 94.4, 94.8, 95.2, 95.5, 95.8, 96.1, 96.4, 96.7, 97.0, 97.2, 97.4, 97.7, 97.9, 98.1, 98.3, 98.4, 98.6, 98.8, 98.9, 99.0, 99.2, 99.3, 99.4, 99.5, 99.6, 99.6, 99.7, 99.8, 99.8, 99.9, 99.9, 99.9, 100, 100, 100]

class userAddedFunction():
    def __init__(self, range: tuple, coefficient: dict, goalCoefficient: dict):
        # range: (start, stop, step)
        # coefficient {(exponentiation): (coefficient)}
        self.coefficient = coefficient
        self.goalCoefficient = goalCoefficient

        for i in self.coefficient:
            if not (i in self.goalCoefficient):
                self.goalCoefficient[i] = 0
        for i in self.goalCoefficient:
            if not (i in self.coefficient):
                self.coefficient[i] = 0
        
        print(self.coefficient)
        print(self.goalCoefficient)

        self.difference = {}
        for i in self.goalCoefficient:
            self.difference[i] = float(self.goalCoefficient[i] - self.coefficient[i])
        
        print(self.difference)

        self.range = range
    
    def draw(self, plot, coefficient=None):
        if coefficient==None:
            coefficient = self.coefficient

        x=np.arange(self.range[0], self.range[1], self.range[2])
        y=np.array([float(0) for i in range(len(x))])
        for i in range(len(x)):
            for expoentiation in coefficient.keys():
                calcTemp = coefficient[expoentiation]*x[i]**expoentiation
                if calcTemp != np.inf:
                    y[i] += calcTemp
        plot(x, y)
    
    def draw_animation(self, plot, progress):
        adjustmentCoefficient = {}
        for i in self.coefficient:
            adjustmentCoefficient[i] = self.coefficient[i] + (progress*self.difference[i])
        
        print(adjustmentCoefficient)
        self.draw(plot, adjustmentCoefficient)

class RTplot():
    def __init__(self):
        self.X = []
        self.Y = []
        self.C = []
        self.upCount = 0
        self.fig = plt.figure()
        self.ax = plt.subplot()

        self.progress = 0
        plt.autoscale(enable=True)


    def aniFunc(self, i):
        # self.addPoint([random.randrange(1,100),random.randrange(1,100)])
        self.ax.cla()
        self.ax.scatter(self.X, self.Y, c=self.C)
        x = np.array(range(-10,11))
        myFunc.draw_animation(plt.plot, speedGraph[self.progress]/100)
        self.progress+=1
        print(self.progress)

        plt.savefig(str(i)+".png", dpi=300)
        if self.progress==100:
            exit()
            self.progress = 0

    def addPoint(self, list):
        if self.upCount > 100:
            self.clearPoint()
            self.upCount = 0
        self.X.append(list[0])
        self.Y.append(list[1])
        self.C.append("#%06x" % random.randint(0, 0xFFFFFF))
        self.upCount += 1

    def clearPoint(self):
        self.X.clear()
        self.Y.clear()
        self.C.clear()
    
    def start(self):
        self.ani = FuncAnimation(self.fig, self.aniFunc, interval=10)
        plt.show()

myFunc = userAddedFunction(
    range=(-20, 10, 0.1), 
    coefficient={2: 1, }, 
    goalCoefficient={4: 1, 3:20, 0: 20000}
)

if __name__ == "__main__":
    plot = RTplot()
    plot.start()