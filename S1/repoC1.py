
# Count words
def countLetters(word):
    return len(word) - word.count(' ')

# Count words
def divisiblebythree(word):
    if (word % 3 == 0):
        #print ("The number is ok.")
        return True
    else: 
        #print ("Try another number. ")
        return False



