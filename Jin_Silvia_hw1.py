# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 19:24:34 2016

@author: Silvia
"""
from functools import reduce

### Problem 1 ###
def translateWord(word):
    if word == "merry":
        return "god"
    elif word == "christmas":
        return "jul"
    elif word == "and":
        return "och"
    elif word == "happy":
        return "gott"
    elif word == "new":
        return "nytt"         
    elif word == "year":
        return "ar"
       
       
       
def translate(card):
    """
#Input: card: a list of strings
# Output: a list of translated strings from input
    """
    l = len(card)
    translatedCard = [None]*l
    for i in range(l):
        translatedCard[i] = translateWord(card[i])
        print(translatedCard)
    return translatedCard
    

### Problem 2 ###
    
def char_freq(text):
# Input: text: a string
# Output: a Python dictionary with each character and the frequncy
    freqDict = {}
    l = len(text)
    for i in range(l):
        if text[i] in freqDict:
            freqDict[text[i]] = freqDict[text[i]]+1
        else:
            freqDict[text[i]] = 1
    return freqDict
    
### Problem 3 ###
def rot13Char(char):
# Encode/decode a single character with ROT-13
# input: char: a character
# output: a character which is encoded/decoded using ROT-13
#         if the character is not a letter, return the same thing
    key = {'a':'n', 'b':'o',
'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v',
'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',
'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j',
'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q',
'E':'R', 'F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X',
'L':'Y', 'M':'Z', 'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E',
'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L',
'Z':'M'}
    if char in key:
        return key[char]
    else:
        return char
    
def rot13cipher(text):
# Encode/decode a string with ROT-13
# input: text: a string
# output: a string which is encoded/decoded using ROT-13
    codedText = ''
    l = len(text)
    for i in range(l):
        codedText=codedText + rot13Char(text[i])
    return codedText
    
### Problem 4 ###
def correct(text):
    correctedText = ''
    isSpace = False
    isDot = False
    i=0
    print('i',i)
    l = len(text)
    print('l',l)
    while True:
       if i >= l:
           break
       elif isSpace == True:
           if text[i] == ' ':
               i = i+1
               print('i',i)
           else:
               isSpace = False
               correctedText = correctedText+text[i]
               i = i+1
               print('i',i)
       elif isDot == True:
           if text[i] == ' ':
               correctedText = correctedText + ' '
               isSpace = True
               isDot = False
               i = i+1
               print('i',i)
           else:
               correctedText = correctedText+' '
               correctedText = correctedText + text[i]
               isSpace = True
               isDot = False
               i = i+1
               print('i',i)
       else:
           if text[i] == ' ':
               isSpace = True
           elif text[i] == '.':
               isDot = True
           correctedText = correctedText + text[i]
           i = i + 1
           print('i',i)
    return correctedText    
    
    
### Problem 5 ###
def make_3sg_form(word):
    newWord = ''
    if word.endswith('y'):
        newWord = word[:-1]+'ies'
    elif word.endswith('o'):
        newWord = word + 'es'
    elif word.endswith('ch'):
        newWord = word + 'es'
    elif word.endswith('s'):
        newWord = word + 'es'
    elif word.endswith('sh'):
        newWord = word + 'es'
    elif word.endswith('x'):
        newWord = word + 'es'
    elif word.endswith('z'):
        newWord = word + 'es'
    else:
        newWord = word + 's'
    return newWord
    
### Problem 6 ###
def isVowel(char):
    if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
        return True
    else:
        return False

def make_ing_form(word):
    newWord = ''
    if word.endswith('e'):
        if word=='be' or word=='see' or word=='flee' or word=='knee':
            newWord = word + 'ing'
        elif word.endswith('ie'):
            newWord = word[:-2] + 'ying'
        else:
           newWord = word[:-1] + 'ing' 
    elif len(word) >=3:
        if isVowel(word[-1])==False:
            if isVowel(word[-2]):
                if isVowel(word[-3])==False:
                    newWord = word+word[-1]+'ing'
                else:
                    newWord = word + 'ing'
            else:
                newWord = word + 'ing'
        else:
            newWord = word + 'ing'
    else:
        newWord = word + 'ing'
    return newWord
    
### Problem 7 ###
def max_in_list(alist):
    return reduce(max,alist)
    
### Problem 8 ###
def map1(listWords):
    l = len(listWords)
    listInts = [None]*l
    for i in range(l):
        listInts[i] = len(listWords[i])
    return listInts
    
def map2(listWords):
    return list(map(len,listWords))
    
def map3(listWords):
    l = len(listWords)
    listInts = [len(listWords[i]) for i in range(l)]
    return listInts
    
### Problem 9 ###
def find_longest_word(listWords):
    listInts = list(map(len,listWords))
    maxInt = reduce(max,listInts)
    return maxInt

### Problem 10 ###
def filter_long_words(listWords,n):
    return list(filter(lambda x:len(x)>n, listWords))

### Problem 11 ###
def translate(listWords):
    myDict = {"merry":"god","christmas":"jul","and":"och","happy":"gott","new":"nytt","year":"år"}
    return list(map(lambda x: myDict[x],listWords))

### Problem 12 ###
