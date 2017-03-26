import numpy;


def WMAdetermistic(expertsValues, realValues,learningRate):

    weights = numpy.ones(len(realValues));
    decisions = [];

    for day in range(0,len(realValues)):
        do = 0;
        dont = 0;

        for expertNumber in range(0,len(expertsValues)):
            if expertsValues[expertNumber][day] == 1:
                do += weights[expertNumber];
            else:
                dont += weights[expertNumber];

        if do >= dont:
            decision = 1;
        else:
            decision = 0;
        decisions.append(decision);

        for expertNumber in range(0,len(expertsValues)):
            if expertsValues[expertNumber][day] != realValues[day]:
                weights[expertNumber] *= (1 - learningRate);


