import math
import random


def sleepingExperts(expertsValues, realValues, learningRate):
    numberOfExperts = len(expertsValues)
    numberOfDays = len(realValues)
    weights = [1 for i in range(0,numberOfExperts)]

    print("Weights:{}".format(weights))
    print("-------------------------------------------")


    for day in range(0, numberOfDays):
        # create an array of the active experts
        activeExperts = []
        for expertNumber in range(0, numberOfExperts):
            if expertsValues[expertNumber][day] != -1:
                activeExperts.append(expertNumber)
        # create an array with the results of experts (1 for right)
        # and calculate sumOfWeights of active experts
        m = []
        sumOfWeights = 0
        for expertNumber in activeExperts:
            if expertsValues[expertNumber][day] != realValues[day]:
                mvalue = float(1)
                m.append(mvalue)
            else:
                mvalue = float(0)
                m.append(mvalue)
            sumOfWeights += weights[expertNumber]
        # choose which advice to follow
        #   generate a random number
        randomNumber = random.randint(0, 99)
        rangeStart = 0
        #   choose the expert based on random number
        probabilities = []
        for expertNumber in activeExperts:
            probability = weights[expertNumber] / float(sumOfWeights)
            probabilities.append(probability)
            rangeEnd = rangeStart + 100 * probability
            if randomNumber >= rangeStart & randomNumber < rangeEnd:
                chosenExpertNumber = expertNumber
        for number in range(0,len(activeExperts)):
            array = [p * mvalue for (p,mvalue) in zip(probabilities,m)]
            r = (sum(array) / float(1+learningRate)) - m[number]
            weights[activeExperts[number]] *= math.pow(1+learningRate,r)

        print("Day:{}".format(day))
        print("Weights:{}".format(weights))
        print("Probabilities:{}".format(probabilities))
        print("-------------------------------------------")
