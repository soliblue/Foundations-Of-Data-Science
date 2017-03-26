def spraseMatrixMaltiplication(values, colIndexes, rowPtr, vectorValues):
    answers = []
    rows = len(rowPtr)
    for row in range(1,rows):
        numberOfValues = rowPtr[row] - rowPtr[row-1]
        valuesToMultiply = values[rowPtr[row-1]:rowPtr[row-1]+numberOfValues]
        answer = 0
        for vectorValueIndex in range(0,len(vectorValues)):
            if vectorValues[vectorValueIndex] != 0:
                answer += vectorValues[vectorValueIndex] * colIndexes[vectorValueIndex]
        answers.append(answer)
    return answers

values = [10,12,11,13,16,11,13]
colInd = [0,3,2,4,1,2,4]
rowPtr = [0,2,4,5,7]

vector = [0,0,0,0,0]
vector2 = [1,1,1,1,1]
vector3 = [1,-1,1,-1,1]

print(spraseMatrixMaltiplication(values,colInd,rowPtr,vector))
print(spraseMatrixMaltiplication(values,colInd,rowPtr,vector2))
print(spraseMatrixMaltiplication(values,colInd,rowPtr,vector3))
