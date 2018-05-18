import random;


def simpleSample(stream):
    for currentPosition in range(0, len(stream)):
        currentPosition += 1;
        if random.randint(1, currentPosition) == currentPosition:
            sample = stream[currentPosition]
    return sample;
