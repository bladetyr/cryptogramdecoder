f = open('dictionary.txt')

def main():

    en =  input("Enter your cryptogram : ")
    #words = en.split()
    new = en
    subst = {}
    lcount = 97
    decrypt(en)
    f.close()

def decrypt(s):
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




#brute force it 
#1. substitute a letter, check if it is possible, continue substituting each letter
#assuming there are still letters to substiture, check if possible every time
#TODO : Figure out how to substitute a letter, use ASCII to add and subtract from it
def checkDictionary(word):
    while True:
        line = f.readLine()
        if not line:
            return False
        if (str(word) == str(line)):
            return True
  
        

main()