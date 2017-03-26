import math;
import random;
import numpy;


def sgn(given):
    if given > 0:
        return 1;
    elif given < 0:
        return -1;
    else:
        return 0;


def multiplyVector(a, b):
    sum = 0;
    for (ai, bi) in zip(a, b):
        sum += ai * bi;
    return sum;


def euclideanNorm(A):
    sum = 0;
    for a in A:
        sum += math.pow(a, 2);
    return math.sqrt(sum);


def normalize(list):
    newList1 = [];
    newList2 = [];
    maximum = 0;
    for (a, b) in list:
        a = a + [(1)];
        newList1.append((a, b));
        current = euclideanNorm(a);
        if current > maximum:
            maximum = current;

    for (a, b) in newList1:
        a = [ai / maximum for ai in a];
        newList2.append((a, b));

    return newList2;


def perceptron(list):
    condition = True;
    epoch = 1;
    weight = numpy.zeros((len(list[0][0]),), dtype=numpy.int);
    updates = 0;
    while condition:
        condition = False;
        for element in list:
            if element[1] != sgn(multiplyVector(element[0], weight)):
                updates += 1;
                x = [element[1] * e for e in element[0]];
                weight = [a + b for (a, b) in zip(x, weight)];
                condition = True;
        print("epoch: {}".format(epoch))
        print("weight: {}".format(weight));
        print("updates: {}".format(updates));
        epoch += 1;
