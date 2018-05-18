import math

def zeros(given):
    log2 = math.log(given,2)
    if log2 % 2 == 0:
        return int(log2)
    else:
        for i in range(int(math.floor(log2)),-1,-1):
            if given % math.pow(2,i) == 0:
                return i


def hashOne(input,outputSize):
    primeNumber = long(15485863)
    firstNaturalNumber = primeNumber / 4
    secondNaturalNumber = primeNumber / 2
    return ((firstNaturalNumber * input + secondNaturalNumber) % primeNumber) % outputSize


def hashTwo(input,outputSize):
    primeNumber = long(2372701867)
    firstNaturalNumber = primeNumber / 4
    secondNaturalNumber = primeNumber / 2
    return ((firstNaturalNumber * input + secondNaturalNumber) % primeNumber) % outputSize

