import random
import numpy
import math
from Perceptron.perceptron import *

def maj(list):
    sum = 0
    for l in list:
        sum += l
    if sum >= 0:
        return 1
    else:
        return -1



oddDimension = random.randint(0,20)
if oddDimension % 2 == 0:
    oddDimension += 1
weight = numpy.ones(oddDimension)
k = math.pow(2, oddDimension)
TrainingSet = []
for i in range(0, int(k)):
    x = []
    for j in range(0, oddDimension):
        randomNumber = random.choice([1, -1])
        x.append(randomNumber)
    TrainingSet.append((x, maj(x)))

for ts in TrainingSet:
    if ts[1] != sgn(multiplyVector(weight,x)):
        print("FAAAAAAAAAIL")
