
words = input('Enter the list: ').split()

are = ['a', 'r', 'e']
idxlst = []

# ******************************
# Make your Code
# ******************************

# print the words that has 'a', 'r', 'e' in sequence
for word in words:
    sequenceCounter = 0

    prevChar = ""
    for char in word:
        if char == are[0]:
            # indicates the start of a sequence or resets if encounter another "a"
            sequenceCounter = 1 
        
        # find other sequence if "a" has been found
        if sequenceCounter >= 1:
            if char == are[sequenceCounter] and char != prevChar:
                sequenceCounter += 1
        
        prevChar = are[sequenceCounter - 1] 
        
        if sequenceCounter == 3:
            idxlst.append(word)
            break

print(idxlst)
