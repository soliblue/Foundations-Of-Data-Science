from Perceptron.perceptron import *

def maj(list):
    sum = 0
    for l in list:
        sum += l
    if sum >= 0:
        return 1
    else:
        return -1


TrainingSet = []
oddNumber = 5
print(oddNumber)
k = math.pow(2, oddNumber)
print(k)
for i in range(0, int(k)):
    x = []
    for j in range(0, oddNumber):
        randomNumber = random.choice([1, -1])
        x.append(randomNumber)
    TrainingSet.append((x, maj(x)))
print(TrainingSet)

TrainingSet = normalize(TrainingSet)

print(TrainingSet)

perceptron(TrainingSet)
