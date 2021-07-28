#######################################################
## Find all anagrams in a string S with string P
#######################################################

def slidingWindow (s, p):

    solutionSet = []

    # Set up the pHash
    pHash = {}
    for character in p:
        pHash [character] = pHash [character] + 1 if character in pHash else 1

    # Set up our base case, which is the first "window"
    runningHash = {}
    for character in s[0:len(p)]:
        runningHash [character] = runningHash [character] + 1 if character in runningHash else 1
    if runningHash == pHash: # Note: == compares the value, vs 'is' which compares in memory
        solutionSet.append(0)
    
    # Run the general case
    for index, character in enumerate(s[len(p):], start=0):

        # Step 1: Add a new letter
        runningHash [character] = runningHash [character] + 1 if character in runningHash else 1

        # Step 2: Remove an old character
        runningHash [s[index]] -= 1
        if runningHash [s[index]] == 0:
            del runningHash [s[index]]
        
        # Step 3: Compare our runningHash with our pHash
        if runningHash == pHash:
            # We need index+1 because index is pointing towards a character to remove
            solutionSet.append(index+1)
    
    print (solutionSet)
            
slidingWindow ("banana banana many bananas do monkeys like to banana", "banana")