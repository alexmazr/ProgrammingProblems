import random

#######################################################
## Find a subset of a list, of size k, with a max sum
#######################################################

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
            # We need plus one because index is flagging an item for removal
            maxIndex = index+1
    
    print ("Result: list["+str(maxIndex)+"] = " + str(maxSum))

list = [random.randint(1, 20) for x in range(100000)]
slidingWindow(list, 4)