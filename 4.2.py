from WeightedMajorityAlgorithm.sleepingExperts import *


expertsValues = [[1,1,1,1,1,1,1],[-1,0,1,0,-1,1,0],[-1,1,0,1,0,1,1],[-1,1,1,-1,1,-1,0],[-1,1,-1,-1,0,-1,-1]]
realValues = [0,1,1,0,0,1,1]
learningRate = 0.25
sleepingExperts(expertsValues, realValues, learningRate)
