def fiveLetterWords():
    dictionary = open("english_dictionary.txt", "r")
    document = open("five.txt", "w")

    fiveLetterList=[]
    for line in dictionary:
        for word in line.split():
            if len(word) == 5:
                fiveLetterList.append(word)

    fiveLetterList2 = []
    
    for i in fiveLetterList:
        i = i.lower()
        if "-" in i or "'" in i:
            continue
        elif i not in fiveLetterList2:
            fiveLetterList2.append(i)
    for _ in fiveLetterList2:
        document.write(_)
        document.write("\n")
    document.close()
    dictionary.close()

#fiveLetterWords()

def listWords():
    document = open("five.txt", "r")
    lst = []
    for line in document:
        word = line[:5]
        lst.append(word)
    print(lst)

listWords()