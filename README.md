# anagrams
Coding Skills test

@author: Ryan J Frazier
contact: ryan.j.frazier@gmail.com

This script is written to find anagrams in words, from a known word list. 
For example, if the word post is in the dictionary word file, then this 
script would return opts, post, pots, spot, stop, and tops as anagrams. 
It will only return anagrams in which there are at least 4 letters in the 
word and at least as many anagrams as there are letters. Anagrams will not 
repeat in the list. Thus, the word post will show up as an anagram of opts, 
and not other places.

This script assumes you will have downloaded the words master file
available here: 
https://raw.githubusercontent.com/eneko/data-repository/master/data/words.txt

The string varaible named wrdsFile will be the location where the word list is
located.
Output will be written to where the wrdsFile is located and named anagrams.txt
