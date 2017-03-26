from WeightedMajorityAlgorithm.randomized import *;

lossMatrix = [[1,1,0,0],[0,1,1,1],[1,0,1,0.5]];
realValues = [1,2,1,2,3,4];
learningRate = 0.5;

WMArandomizedA(lossMatrix,realValues,learningRate);
