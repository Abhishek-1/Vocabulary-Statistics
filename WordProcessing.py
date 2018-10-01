import glob
import os
import operator
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

##  Name - Abhishek Ranjan
##  UIN - 657657618
##  NetId - aranja8

path = 'citeseer/citeseer/*'

files = glob.glob(path)

vocabList = {}
vocabListNew = {}
wordslist = []
totalwords = []
totalwordsNew = []
totalwordsTemp = []
stops = []
#print(stopwords.words('english'))
#stops = set(stopwords.words('english'))


##########Tokenizing Function ###################
def wordtokenize(wordslist):
    for item in wordslist:
        for word in item:
            ## Call to punctuation removal ##
            word = punctuation_remove(word)
            if word != '':
                totalwords.append(word)
                if word in vocabList:
                    vocabList[word] += 1
                else:
                    vocabList[word] = 1
                if word.lower() not in stops:
                    wordNew  = word_stemming(word)
                    totalwordsNew.append(wordNew)                    
                    if wordNew in vocabListNew:
                        vocabListNew[wordNew] += 1
                    else:
                        vocabListNew[wordNew] = 1

#########Punctuation Removal #####################
def punctuation_remove(word):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    # remove punctuation from the string
    no_punct = ""
    for char in word:
        if char not in punctuations:
            no_punct = no_punct + char
    return no_punct


#########Porter Stemmer #####################
def word_stemming(word):
     return ps.stem(word)
 



######### Word Facts - Question 2a - 2e Function ###################

def wordFact(vocabListItems, totalwordsItems):
    totalNum = len(totalwordsItems)
    stopList = []
    count = 0
    print("Total Number of Words in Collection --> ",totalNum)
    uniqueNum = len(vocabListItems)
    print("Total Number of Unique Words in Collection --> ",uniqueNum)
    sorted_vocab = sorted(vocabListItems.items(), key=operator.itemgetter(1), reverse=True)
    top20 = sorted_vocab[:20]
    print(" \nTop 20 Words in this List are", top20)
    for word in top20:
        if word[0].lower() in stops:
            stopList.append(word)
    print(" \nStopWords present in top 20 Words --> ", stopList)
    
    minnumLimit = totalNum*0.15
    for word in sorted_vocab:
        if word[1] > minnumLimit:
            count += 1
    print(" \n Minimum number of unique words accounting for 15% of the total number of words --> ", count)
    print("\n\n")       
    
for paths in files:
    with open(os.path.join(os.path.dirname(__file__), paths)) as file:
        #print(file.read())
        whiteSpaceRegex = "\\s";
        wordslist.append(file.read().split());

########### Reading StopWords ###################################################

with open('stopwords.txt', 'r') as stopFile:
    stops = stopFile.read().split('\n')

        

ps = PorterStemmer() 
wordtokenize(wordslist)

####### Checking question 2a - 2e before porter stemmer and stopWord Elimination
print("\n############### Before Porter Stemmer and StopWord Elimination ##################\n")
wordFact(vocabList, totalwords)


####### Checking question 3a - 3e before porter stemmer and stopWord Elimination
print("\n############### After Porter Stemmer and StopWord Elimination ##################\n")
wordFact(vocabListNew, totalwordsNew)

      




 
                

            
        
        
        
    