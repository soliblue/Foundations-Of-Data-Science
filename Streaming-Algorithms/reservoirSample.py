import random;


def simpleSample(stream, samplesSize):
    samples = [samplesSize]
    for sampleNumber in range(0, samplesSize):
        samples[sampleNumber] = stream[sampleNumber];
    for currentPosition in range(0, len(stream)):
        currentPosition += 1;
        probability = samplesSize / float(currentPosition)
        if random.randint(1, 100) <= probability * 100:
            sampleNumber = random.randint(0, samplesSize - 1)
            samples[sampleNumber] = stream[currentPosition];
    return samples;
