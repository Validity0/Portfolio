def binarySearch(sequence, item):
    beginIndex = 0
    endIndex = len(sequence) - 1

    while beginIndex <= endIndex:
        midpoint = beginIndex + (endIndex - beginIndex) // 2
        midpointVal = sequence[midpoint]
        if midpointVal == item:
            return midpoint

        elif item < midpointVal:
            endIndex = midpoint - 1

        else:
            beginIndex = midpoint + 1
    return None

sequenceA = [2,4,6,8,10,12,14,16,18,20]
itemA = 12


print(binarySearch(sequenceA, itemA))