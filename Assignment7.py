import random
def assignment7():
    WorldList = ['black','yellow','brown','red','pink']
     
    for i in range(len(WorldList)):
        word = WorldList[i]
        latterlist= random.sample(word,len(word))
        randomlword = "".join(latterlist)
        print("Color word anagram:"+randomlword)
        correctionword = randomlword
        while correctionword not in WorldList:
            correctionword = input("Guess the color word!")
        print("Correct!")
    


if __name__ == '__main__':
    assignment7()
      

