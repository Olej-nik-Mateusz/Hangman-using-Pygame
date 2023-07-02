import random
import os

# open food.txt file. Create list with words to choose as guessingWord
def getList():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    fh = open("food.txt", "r", encoding="utf-8")
    text = fh.read().split("\n")

    foodList=set([word for word in text])
    guessingList = []
    
    for word in foodList:
            
            if ' ' in word:
                continue
            
            elif '-' in word:
                continue
            
            else:
            
                if len(guessingList) == 0:
                    guessingList = [word]
            
                else:
                    guessingList.append(word)
                    
    return guessingList

# guessWord generator
def rndGuessWord(guessingList):
     guessWord = random.choice(guessingList).upper()
     return guessWord


if __name__ == "__main__":
     print(rndGuessWord(getList()))
     