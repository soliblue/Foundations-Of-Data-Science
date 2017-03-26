import numpy
import math
import random


def WMArandomizedA(lossMatrix,realValues,learningRate):
    numberOfExperts = len(lossMatrix)
    numberOfDays = len(realValues)
    weights = numpy.ones(numberOfExperts)
    sumOfWeights = sum(weights)
    probabilities = []

    for expertNumber in range(0, numberOfExperts):
        probability = weights[expertNumber] / float(sumOfWeights)
        probabilities.append(probability)

    print("Day:{}".format(0))
    print("Weights:{}".format(weights))
    print("Probabilities:{}".format(probabilities))

    for day in range(0,numberOfDays):

        probabilities = []
        for expertNumber in range(0,numberOfExperts):
            weights[expertNumber] *= math.pow((1-learningRate),lossMatrix[expertNumber][realValues[day] - 1])
        sumOfWeights = sum(weights)
        randomNumber = random.randint(0, 100)
        rangeStart = 0
        for expertNumber in range(0,numberOfExperts):
            probability = weights[expertNumber] / float(sumOfWeights)
            probabilities.append(probability)
            rangeEnd = rangeStart + 100 * probability
            if randomNumber >= rangeStart and randomNumber < rangeEnd:
                chosenExpertNumber = expertNumber
            rangeStart = rangeEnd
        print("-----------------------------------------------------------------")
        print("Day:{}".format(day + 1))
        print("Weights:{}".format(weights))
        print("Probabilities:{}".format(probabilities))

