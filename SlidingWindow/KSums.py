import math
import random

def slidingWindow (list, windowSize):
    # Set up the first window
    maxSum = sum(list[0:windowSize])
    maxIndex = 0
    slidingSum = maxSum

    # Enumerate starting from the second window
    # with a counter starting from the first index of the first window
    for index, item in enumerate(list[windowSize:], start=0):
        slidingSum += item
        slidingSum -= list [index]
        if slidingSum > maxSum:
            maxSum = slidingSum
            maxIndex = index
    
    print ("Result: list["+str(maxIndex)+"] = " + str(maxSum))

list = [random.randint(1, 20) for x in range(100000)]
slidingWindow(list, 50)