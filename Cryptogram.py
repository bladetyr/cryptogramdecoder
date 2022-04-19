#==GLOBAL VARIABLES==
possibleWords = []
currentDict = {}
#conflict = False
possibleMatches1 = []
possibleMatches2 =[]
possibleMatches3 = []
possibleMatches4 = []
possibleMatches5 = []

def main():
    workingDict = {}
    solutions = []
    #global conflict
    en =  input("Enter your cryptogram : ")
    #words = en.split()
    #new = en
    #needed for decrypt; is ASCII value of A
    #check how many words are in input
    wordChecker = en.split()
    numWords = len(wordChecker)
    #print(numWords)
    #let's now assume there are multiple words; check for a space
    for x in range(numWords):
        #set up possible matches
      checkDictionary(decrypt(wordChecker[x]),x)

    for word in possibleMatches1:
        oneWord = True
        #global conflict
        #FIXME: need to add possibleMatches1 to solutions if only one word
        conflict = False
        solu = word
        #make dictionary
        count = 1
        resetDict(workingDict)
        for char in word:
            workingDict[char] = wordChecker[0][count-1:count]
            count = count + 1
        for word2 in possibleMatches2:
            #make temporrary dictionary for mapping checks
            conflict = False #REMOVE THIS IF THIS DOESNT WORK
            tempDict = workingDict.copy()
            oneWord = False
            #find solutions for word 2
            solu = word
            count2 = 1
            for char in word2:
                tempDict[char] = wordChecker[1][count2-1:count2]
                if(char in workingDict):   
                    print("===")
                    print(workingDict[char])
                    print("===b")                
                    print(char)
                    print("===c")  
                    if(str(wordChecker[1][count2-1:count2]) != str(workingDict[char])):
                        conflict = True
                        print("Conflict is True")
                        print("Conflict: " + wordChecker[1][count2-1:count2] + " vs " + workingDict[char])
                        #break
                else:
                    if wordChecker[1][count2-1:count2] in workingDict.values():
                        conflict = True
                count2 = count2+1
            #if no conflict, add to solutions list
            if conflict == False:
                print("Word added!")
                print("Conflict is False")
                solu = solu + " " + word2
                tempSolu = solu
                print("UR MOM: " + solu)
                print(tempDict)
                if(len(wordChecker) == 2):
                    solutions.append(solu)
            #conflict = False
            #== WORD 3 ==
            if(conflict == False):
                solu = tempSolu
                for word3 in possibleMatches3:
                    conflict = False
                    threeWords = True
                    tempDict2 = tempDict.copy()
                    #make dictionary
                    count3 = 1
                    for char2 in word3:
                        tempDict2[char2] = wordChecker[2][count3-1:count3]
                        if(char2 in tempDict):    
                            if(str(wordChecker[2][count3-1:count3]) != str(tempDict[char2])):
                                conflict = True
                                #print("Conflict is True")
                                #print("Conflict: " + wordChecker[2][count3-1:count3] + " vs " + tempDict[char])
                                #break
                        else:
                            if wordChecker[2][count3-1:count3] in tempDict.values():
                                conflict = True
                        count3 = count3+1
                    if conflict == False:
                        print("Word added! 3 Time")
                        print("Conflict is False")
                        solu = tempSolu + " " + word3
                        tempSolu2 = solu
                        print("UR MOM: " + solu)
                        if(len(wordChecker) == 3):
                            solutions.append(solu)
                    if (conflict == False):
                        for word4 in possibleMatches4:
                            #== WORD 4==
                            solu = tempSolu2
                            conflict = False
                            fourWords = True
                            tempDict3 = tempDict2.copy()
                            #make dictionary
                            count4 = 1
                            for char3 in word4:
                                tempDict3[char3] = wordChecker[3][count3-1:count3]
                                if(char3 in tempDict2):    
                                    if(str(wordChecker[3][count4-1:count4]) != str(tempDict2[char3])):
                                        conflict = True
                                else:
                                    if wordChecker[3][count4-1:count4] in tempDict2.values():
                                        conflict = True
                                count4 = count4+1
                            if conflict == False:
                                print("Word added! 4 Time")
                                print("Conflict is False")
                                solu = tempSolu2 + " " + word4
                                print("UR MOM: " + solu)
                                solutions.append(solu)
        #             for word5 in possibleMatches5:
                        
    #if there is only one word, then this is all we have to do
    #checkDictionary(decrypt(en))
    if(oneWord == True):
        solutions = possibleMatches1
    print("Given: " + en)
    print("Solu: " + solu)
    print(len(solutions))
    for s in solutions:
        print(s)
    #print("Possible Matches: ")
    #print(possibleWords)

def decrypt(s):
    global currentDict
    subst = {}
    lcount = 97
    for char in s:
        if char in subst:
            pass
        else:
            subst[char] = lcount
            lcount = lcount + 1
    count = 0
    s = list(s)
    for let in s:
        s[count] = chr(subst.get(let))
        #print(let)
        #print(s)
        count = count + 1
    #print(s)
    #print(subst)
    currentDict = subst
    return s

def resetDict(dict):
    dict.clear()

#brute force it 
#1. substitute a letter, check if it is possible, continue substituting each letter
#assuming there are still letters to substiture, check if possible every time
#TODO: Figure out how to substitute a letter, use ASCII to add and subtract from it
def checkDictionary(word, number):
    f = open('dictionary.txt','r')
    global possibleMatches1
    global possibleMatches2
    global possibleMatches3
    global possibleMatches4
    global possibleMatches5
    for line in f:
        #line = f.readLine()
        line = line.strip('\n')
        #print("===")
        #print(line)
        #if not line:
            #return False
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
    f.close()
  
main()