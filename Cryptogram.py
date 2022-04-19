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
        #global conflict
        conflict = False
        solu = word
        #make dictionary
        count = 1
        resetDict(workingDict)
        for char in word:
            workingDict[char] = wordChecker[0][count-1:count]
            count = count + 1
        for word2 in possibleMatches2:
            #find solutions for word 2
            solu = word
            count2 = 1
            for char in word2:
                if(char in workingDict):                        
                    if(wordChecker[1][count2-1:count2] != workingDict[char]):
                        #conflict = True
                        a = 1
                count2 = count2+1
            #FIXME: conflict is the problem; it's not getting inside this if statement
            #so solutions never appends and solu has only one word
            if conflict == False:
                solu = solu + " " + word2
                print("UR MOM: " + solu)
                solutions.append(solu)


        #     for word3 in possibleMatches3:
        #         for word4 in possibleMatches4:
        #             for word5 in possibleMatches5:
                        
    #if there is only one word, then this is all we have to do
    #checkDictionary(decrypt(en))
    print("Given: " + en)
    print("Solu: " + solu)
    print(solutions)
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