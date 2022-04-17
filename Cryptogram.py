f = open('dictionary.txt','r')
#==GLOBAL VARIABLES==
possibleWords = []
currentDict = {}

def main():

    en =  input("Enter your cryptogram : ")
    #words = en.split()
    new = en
    subst = {}
    lcount = 97
    #if there is only one word, then this is all we have to do
    checkDictionary(decrypt(en))
    #let's now assume there are multiple words; check for a space
    #if(' ' in en):
        #for
    print("Given: " + en)
    print("Possible Matches: ")
    print(possibleWords)
    f.close()

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
        print(let)
        print(s)
        count = count + 1
    print(s)
    print(subst)
    currentDict = subst
    return s

def testPossibleWords():
    #a
    return False

#brute force it 
#1. substitute a letter, check if it is possible, continue substituting each letter
#assuming there are still letters to substiture, check if possible every time
#TODO: Figure out how to substitute a letter, use ASCII to add and subtract from it
def checkDictionary(word):
    for line in f:
        #line = f.readLine()
        line = line.strip('\n')
        #print("===")
        #print(line)
        if not line:
            return False
        if (len(word) == len(line)):
            if(decrypt(word)==decrypt(line)):
                possibleWords.append(line)
  
        

main()