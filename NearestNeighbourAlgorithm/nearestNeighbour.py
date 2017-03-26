import math

def euclidean(vectorA,vectorB):
    sum = 0
    for (a,b) in zip(vectorA,vectorB):
        sum += math.pow(a - b,2)
    return math.sqrt(sum)

def manhatten(vectorA,vectorB):
    sum = 0
    for (a,b) in zip(vectorA, vectorB):
        sum += math.fabs(a-b)
    return sum


def nearest_neighbour_manhattan(k,oldDataPoints,newDataPoints):
    answers = []
    for newDataPoint in newDataPoints:
        distances = []
        for oldDataPoint in oldDataPoints:
            distances.append((oldDataPoint[1], manhatten(oldDataPoint[0],newDataPoint)))
        distances = sorted(distances, key=lambda distance: distance[1])
        distances = distances[0:k]
        for distance in distances:
            sum =+ distance[0]
        if sum >= 0:
            answer = (newDataPoint,1)
        else:
            answer = (newDataPoint,-1)
        answers.append(answer)
    return answers

def nearest_neighbour_euclidean(k,oldDataPoints,newDataPoints):
    answers = []
    for newDataPoint in newDataPoints:
        distances = []
        for oldDataPoint in oldDataPoints:
            distances.append((oldDataPoint[1], euclidean(oldDataPoint[0],newDataPoint)))
        distances = sorted(distances, key=lambda distance: distance[1])
        distances = distances[0:k]
        for distance in distances:
            sum =+ distance[0]
        if sum >= 0:
            answer = (newDataPoint,1)
        else:
            answer = (newDataPoint,-1)
        answers.append(answer)
    return answers
