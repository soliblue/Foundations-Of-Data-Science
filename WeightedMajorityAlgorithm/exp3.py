import numpy;
import math;
import random;


def WMArandomizedexp3(actions, payoff, tradeoff):
    numberOfExperts = len(actions);
    numberOfDays = len(payoff[0]);
    weights = numpy.ones(numberOfExperts);
    for day in range(0, numberOfDays):
        probabilities = [];
        sumOfWeights = sum(weights);
        randomNumber = random.randint(1, 100);
        rangeStart = 1;
        for expertNumber in range(0, numberOfExperts):
            probability = (1 - tradeoff) * (weights[expertNumber] / float(sumOfWeights)) + (
                tradeoff / float(numberOfExperts));
            probabilities.append(probability);
            rangeEnd = rangeStart + 100 * probability;
            if randomNumber >= rangeStart & randomNumber <= rangeEnd:
                chosenExpertNumber = expertNumber;
                reward = payoff[chosenExpertNumber][day];
                weights[chosenExpertNumber] *= math.exp(
                    (tradeoff * reward) / (numberOfExperts * probabilities[chosenExpertNumber]));
            rangeStart = rangeEnd + 1;
        print("Weights:")
        print(weights);
        print(probabilities);
