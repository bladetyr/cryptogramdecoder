#== GLOBAL VARIABLES ==
possibleWords = []
currentDict = {}
possibleMatches1 = []
possibleMatches2 =[]
possibleMatches3 = []
possibleMatches4 = []
possibleMatches5 = []

def main():
    workingDict = {}
    solutions = []
    en =  input("Enter your Cryptogram: ")
    #we need to check how many words are in input
    wordChecker = en.split()
    numWords = len(wordChecker)
    #let's now assume there are multiple words; check for a space
    for x in range(numWords):
        #set up possible matches using checkDictionary (which uses the global lists)
      checkDictionary(decrypt(wordChecker[x]),x)

    for word in possibleMatches1:
        #oneWord gets set to false if there is more than one word
        #this is because of how we put solutions in solutions[]
        #it's just easier this way, even if it's a bit ugly
        oneWord = True
        conflict = False
        solu = word
        #make dictionary
        count = 1
        resetDict(workingDict)
        for char in word:
            workingDict[char] = wordChecker[0][count-1:count]
            count = count + 1
        for word2 in possibleMatches2:
            #make temp dictionary for mapping checks
            conflict = False
            tempDict = workingDict.copy()
            oneWord = False
            #find solutions for word 2
            solu = word
            count2 = 1
            for char in word2:
                tempDict[char] = wordChecker[1][count2-1:count2]
                if(char in workingDict):    
                    if(str(wordChecker[1][count2-1:count2]) != str(workingDict[char])):
                        conflict = True
                else:
                    if wordChecker[1][count2-1:count2] in workingDict.values():
                        conflict = True
                count2 = count2+1
            #if no conflict in letter maps in the dictionary, add to solutions list
            if conflict == False:
                solu = solu + " " + word2
                tempSolu = solu
                if(len(wordChecker) == 2):
                    solutions.append(solu)
            #== WORD 3 ==
            #we should only continue if there is no conflict
            #having a conflict means there's an invalid solution
            if(conflict == False):
                #we need to reset solu up here or else we'll have answers strung together
                solu = tempSolu
                for word3 in possibleMatches3:
                    conflict = False
                    tempDict2 = tempDict.copy()
                    #make dictionary
                    count3 = 1
                    for char2 in word3:
                        tempDict2[char2] = wordChecker[2][count3-1:count3]
                        if(char2 in tempDict):    
                            if(str(wordChecker[2][count3-1:count3]) != str(tempDict[char2])):
                                conflict = True
                        else:
                            if wordChecker[2][count3-1:count3] in tempDict.values():
                                conflict = True
                        count3 = count3+1
                    #conflict checking again
                    if conflict == False:
                        #add word3 to solu, which could be added to solutions
                        solu = tempSolu + " " + word3
                        tempSolu2 = solu
                        if(len(wordChecker) == 3):
                            solutions.append(solu)
                    #we should only continue if there is no conflict
                    #having a conflict means there's an invalid solution
                    if (conflict == False):
                        #== WORD 4 ==
                        for word4 in possibleMatches4:
                            solu = tempSolu2
                            conflict = False
                            tempDict3 = tempDict2.copy()
                            #make dictionary
                            count4 = 1
                            for char3 in word4:
                                tempDict3[char3] = wordChecker[3][count4-1:count4]
                                if(char3 in tempDict2):    
                                    if(str(wordChecker[3][count4-1:count4]) != str(tempDict2[char3])):
                                        conflict = True
                                else:
                                    if wordChecker[3][count4-1:count4] in tempDict2.values():
                                        conflict = True
                                count4 = count4+1
                            if conflict == False:
                                solu = tempSolu2 + " " + word4
                                tempSolu3 = solu
                                if(len(wordChecker) == 4):
                                    solutions.append(solu)
                            #== WORD 5 ==
                            #we should only continue if there is no conflict
                            #having a conflict means there's an invalid solution
                            if (conflict == False):
                                for word5 in possibleMatches5:
                                    solu = tempSolu3
                                    conflict = False
                                    tempDict4 = tempDict3.copy()
                                    #make dictionary
                                    count5 = 1
                                    for char4 in word5:
                                        tempDict4[char4] = wordChecker[4][count5-1:count5]
                                        if(char4 in tempDict3):    
                                            if(str(wordChecker[4][count5-1:count5]) != str(tempDict3[char4])):
                                                conflict = True
                                        else:
                                            if wordChecker[4][count5-1:count5] in tempDict3.values():
                                                conflict = True
                                        count5 = count5+1
                                    if conflict == False:
                                        solu = tempSolu3 + " " + word5
                                        solutions.append(solu)
                        
    #printing the solution
    if(oneWord == True):
        #printing is a bit different if there's only one word; mentioned above
        solutions = possibleMatches1
    print("Given: " + en)
    print(len(solutions))
    for s in solutions:
        print(s)

def decrypt(s):
    global currentDict
    subst = {}
    #lcount is the ASCII value of a; we use this to set the
    #rhythym pattern of words
    #EX: decrypt("ditto")->"abccd"
    lcount = 97
    for char in s:
        if char in subst:
            pass
        else:
            subst[char] = lcount
            lcount = lcount + 1
    #count is to keep track of substring-ing
    count = 0
    s = list(s)
    for let in s:
        s[count] = chr(subst.get(let))
        count = count + 1
    currentDict = subst
    return s

def resetDict(dict):
    #easy reset for dictionary
    #didn't save any lines of code but made it easier for me to read
    dict.clear()

def checkDictionary(word, number):
    '''
    Takes in a word to check and a number. The number determines which list
    of possible matches that the matches go in. We have a separate list for each
    word (up to 5 can be decrypted at a time)
    '''
    #open dictionary.txt for reading purposes
    f = open('dictionary.txt','r')
    global possibleMatches1
    global possibleMatches2
    global possibleMatches3
    global possibleMatches4
    global possibleMatches5
    for line in f:
        line = line.strip('\n')
        if (len(word) == len(line)):
            if(decrypt(word) == decrypt(line)):
                if(number == 0):
                    possibleMatches1.append(line)
                elif(number == 1):
                    possibleMatches2.append(line)
                elif(number == 2):
                    possibleMatches3.append(line)
                elif(number == 3):
                    possibleMatches4.append(line)
                elif(number == 4):
                    possibleMatches5.append(line)
    #close dictionary.txt
    f.close()
  
#call main to start decyrpting
main()