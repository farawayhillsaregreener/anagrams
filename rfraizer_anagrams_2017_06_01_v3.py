# -*- coding: utf-8 -*-
"""
Created on Tue May 30 13:31:51 2017

@author: Ryan J Frazier
contact: ryan.j.frazier@gmail.com

This script is written to find anagrams in words, from a known word list. 
For example, if the word post is submitted, then this script would return
opts, post, pots, spot, stop, and tops as anagrams. It will only return
anagrams in which there are at least 4 letters in the word and at least 
as many anagrams as there are letters. Anagrams will not repeat in the list.
Thus, the word post will show up as an anagram of opts, and not other places.

This script assumes you will have downloaded the words master file
available here: 
https://raw.githubusercontent.com/eneko/data-repository/master/data/words.txt

The string varaible named wrdsFile will be the location where the word list is
located.
Output will be written to where the wrdsFile is located and named anagrams.txt


"""


import os

   
######   INPUTS
wrdsFile=r"C:\courses\code_test\words_orig.txt"#words master file

#####  OUTPUTS
anagramFile=os.path.dirname(wrdsFile)+"\\anagrams.txt" #output anagram file




#test if anagram file already exists; if so, delete it, and create a new one
if os.path.exists(anagramFile):
    os.remove(anagramFile)
    a=open(anagramFile,'w+') 
else:
    a=open(anagramFile,'w+') 
 
#####  READ and CLEAN dictionary word file
#read in dictionary
wf=open(wrdsFile, 'r') #open the words file
wordList=wf.readlines()#read in all words as a list
wf.close()#close words file

#clean word list of carraige returns AND remove any words less than 3 letters
wordList=[wrd.rstrip('\n') for wrd in wordList if len(wrd.rstrip('\n')) >3]
wordList=[x.lower() for x in wordList]#lowercase the list
wordList=list(set(wordList))# retain unique words only
wordList.sort()#alphabetical sort the list  

sortedLetterList=[list(x) for x in wordList]#convert all words to lists 
sortedLetterList=[sorted(x) for x in sortedLetterList]#sort lists of letters
sortedLetterList=[''.join(x) for x in sortedLetterList]#convert them to words again


#####   FIND ANAGRAMS
combinedList=zip(sortedLetterList, wordList)#combine the wordlist and letter list
gramList=[]#start an empty list to store anagrams that meet all conditions  
                
for x in range(0,len(combinedList)):
    wrd=combinedList[x][0]#word to be looked for
    #reduce the list to words with the same first 4 chars and the same length
    reducedListOfWords=[y for y in combinedList if (len(y[0])==len(wrd)) and (y[0][0:4]==wrd[0:4])]
    #search the reduced combined list of words for strings that have the same letters
    matches=[y for y in reducedListOfWords if wrd == y[0]]#find anagrams
    #make sure there are at least as many anagrams as there are letters        
    if len(matches) >= len(wrd):
        gramList.append([x[1] for x in matches])#add ok matches to final list
        wrd=reducedListOfWords=matches=y=None
    else:
        wrd=reducedListOfWords=matches=y=None
    
   
#####    FORMAT  and  OUTPUT RESULTS

#unique List of anagrams
gramList=[list(x) for x in set(tuple(x) for x in gramList)]

#formatting, adding commas, and end of line returns          
for i in range(0,len(gramList)):
    dup=gramList[i][:]
    gramList[i]=[y+', ' for y in gramList[i][:-1]]
    gramList[i].append(dup[len(dup)-1]+'\n')
    gramList[i]=[''.join(gramList[i])]

#write out the reuslts out to the previously opened file
for lines in gramList:
    a.writelines(lines)

a.close()
