from Perceptron.perceptron import *;

def maj(list):
    sum = 0;
    for l in list:
        sum += l;
    if sum >= 0:
        return 1;
    else:
        return -1;

TrainingSet1 = [];

for i in range(1,20):
    x = [];
    for j in range(1,10):
        x.append(random.choice([-1,1]));
    TrainingSet1.append((x,maj(x)));

TrainingSet2 = [];
TrainingSet2 = list(TrainingSet1);
TrainingSet3 = list(TrainingSet1);
TrainingSet4 = list(TrainingSet1);


random.shuffle(TrainingSet1);
random.shuffle(TrainingSet2);
random.shuffle(TrainingSet3);

print(perceptron(normalize(TrainingSet1)));
print(perceptron(normalize(TrainingSet2)));
print(perceptron(normalize(TrainingSet3)));
print(perceptron(normalize(TrainingSet4)));

