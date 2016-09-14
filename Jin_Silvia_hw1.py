# -*- coding: utf-8 -*-
"""

@author: Silvia Jin

Homework 1 Group D
"""

### Problem 1 ###

def translateWord(char):
    '''
    This is a helper function for the function translate, which only translate one
    word in English into Swedish.
    '''
    key = {'merry':'god','christmas':'jul','and':'och','happy':'gott','new':'nytt','year':'år'}
    if char in key:
        return key[char]
    else:
        return char
       
       
       
def translate(card):
    """
    This is a function that takes a list of English words and returns a list of
    Swedish words.
    We use the helper function translateWrod(char) to translate each word in the list
    Input: card: a list of strings.
    Output: a list of translated strings from input.
    """
    l = len(card) #store the length of the list
    translatedCard = [None]*l #name an empty list
    for i in range(l):
        translatedCard[i] = translateWord(card[i])
    return translatedCard

# example
print(translate(['merry','christmas','and','happy','new','year']))


### Problem 2 ###
    
def char_freq(text):
    '''
    This funcion takes a string and builds a frequency listing of the characters
    contained in it represented by a Python dictionary.
    Input: text: a string.
    Output: a Python dictionary with each character and the frequncy.
    '''
    freqDict = {} # create a null dictionary
    l = len(text) # store the length of the text
    for i in range(l):
        if text[i] in freqDict: # if the letter is already in the dict
            freqDict[text[i]] = freqDict[text[i]]+1 # add the count by 1
        else: # if the letter is not in the dict
            freqDict[text[i]] = 1 # we create a new item
    return freqDict

# example
print(char_freq("abbabcbdbabdbdbabababcbcbab"))

### Problem 3 ###

def rot13Char(char):
    '''
    This is a helper function for the function rot13cipher.
    The function encodes/decodes a single character with ROT-13.
    Input: char: a character.
    Output: a character which is encoded/decoded using ROT-13
            if the character is not a letter, return the same thing.
    '''
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
    else: # when the character is not a letter, we output the same input
        return char
    
def rot13cipher(text):
    '''
    This function encodes/decodes a string with ROT-13.
    The function uses the helper function rot13Char(char).
    Input: text: a string.
    Output: a string which is encoded/decoded using ROT-13.
    '''
    codedText = '' # create an empty string
    l = len(text) # store the length of the text
    for i in range(l): # for each character in the text
        codedText=codedText + rot13Char(text[i]) # encode/decode the letter
    return codedText

# example
print(rot13cipher('Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!'))

### Problem 4 ###

def correct(text):
    '''
    This is a simple "spelling correction" function that takes a string and sees to
    it that 1) two or more occurrences of the space character is compressed into one,
    and 2) inserts an extra spce after a period if the period is directly followed by
    a letter.
    '''
    correctedText = '' # create an empty string for the corrected text
    isSpace = False # initialize a boolean for space
    isDot = False # initialize a boolean for period
    i=0 # initialize the position where we are checking the string
    l = len(text)
    while True:
       if i >= l: # if we reach the end of the string, stop
           break
       elif isSpace == True: # if the current location is a space
           if text[i] == ' ': # if the next location is still a space, we jump
               i = i+1
           else:
               isSpace = False # if the next location is not a space, we copy
               correctedText = correctedText+text[i]
               i = i+1
       elif isDot == True: # if the current location is a period
           if text[i] == ' ': # if there is a space behind it, we copy
               correctedText = correctedText + ' '
               isSpace = True
               isDot = False
               i = i+1
           else: # if there is no space behind it, we add a space
               correctedText = correctedText+' '
               correctedText = correctedText + text[i]
               isSpace = True
               isDot = False
               i = i+1
       else: # otherwise we just copy the text, and change the boolean values accordingly
           if text[i] == ' ':
               isSpace = True
           elif text[i] == '.':
               isDot = True
           correctedText = correctedText + text[i]
           i = i + 1
    return correctedText    

# example
print(correct("This  is very funny    and cool.Indeed!"))
    
### Problem 5 ###

def make_3sg_form(word):
    '''
    The function changes a verb to its third person singular verb form.
    However, the rules are heuristic and do not work for all cases.
    The rules:
    a. If a verb ends in y, remove it and add ies;
    b. If the verb ends in o, ch, s, sh, x or z, add es;
    c. By default just add s.
    Input: a string.
    Output: a string, which changes the input into its third person singular form.
    '''
    newWord = '' # create an empty string to hold the new word
    if word.endswith('y'): # if the verb ends in y
        newWord = word[:-1]+'ies' # remove it and add ies
    elif word.endswith('o'): # if the verb ends in o
        newWord = word + 'es' # add es
    elif word.endswith('ch'): # if the verb ends in ch
        newWord = word + 'es' # add es
    elif word.endswith('s'): # if the verb ends in s
        newWord = word + 'es' # add es
    elif word.endswith('sh'): # if the verb ends in sh
        newWord = word + 'es' # add es
    elif word.endswith('x'): # if the verb ends in x
        newWord = word + 'es' # add es
    elif word.endswith('z'): # if the verb ends in z
        newWord = word + 'es' # add es
    else: # all other cases
        newWord = word + 's' # add s
    return newWord

# example
print(make_3sg_form('satisfy'))
print(make_3sg_form('catch'))
print(make_3sg_form('love'))

### Problem 6 ###

def isVowel(char):
    '''
    This is a helper function for make_ing_form(word).
    Input: a character.
    Output: a boolean:
            True if the input is a vowel;
            False otherwise.
    '''
    if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
        return True
    else:
        return False

def make_ing_form(word):
    '''
    This function changes a word into its present participle.
    However, the rules are heuristic and do not work for all cases.
    The rules:
    a. If the verb ends in e, drop the e and add ing;
       Exceptions: be, see, flee, knee;
    b. If the verb ends in ie, change ie to y and add ing;
    c. For words consisting of consonant-vowel-consonant,
       double the final letter before adding ing;
    d. By default just add ing.
    Input: a string.
    Output: a string of the input changed into present participle.
    '''
    newWord = '' # create an empty string for the output
    if word.endswith('e'): # if the verb ends in e
        if word=='be' or word=='see' or word=='flee' or word=='knee': # exceptions
            newWord = word + 'ing' # add ing
        elif word.endswith('ie'): # if the verb actually ends in ie
            newWord = word[:-2] + 'ying' # change ie to y and add ing
        else: # if not exeption, and just ends in e
           newWord = word[:-1] + 'ing' # drop the e and add ing
    # for words consisting of consonant-vowel-consonant,
    # the length has to be gigger than three
    elif len(word) >=3: 
        if isVowel(word[-1])==False: # if the last character is consonant
            if isVowel(word[-2]): # if the second last character is vowel
                if isVowel(word[-3])==False: # if the thrid last character is consonant
                    newWord = word+word[-1]+'ing' # double the final letter and add ing
                else:
                    newWord = word + 'ing'
            else:
                newWord = word + 'ing'
        else:
            newWord = word + 'ing'
    else: # by default, add ing
        newWord = word + 'ing'
    return newWord

# example
print(make_ing_form('love'))
print(make_ing_form('be'))
print(make_ing_form('die'))
print(make_ing_form('bug'))
print(make_ing_form('drink'))

### Problem 7 ###

from functools import reduce # import reduce module

def max_in_list(alist):
    '''
    This function takes a list of numbers and returns the largest one,
    using the higher order function reduce().
    Input: a list ot numbers.
    Output: a number, which is the largest one in the list.
    '''
    return reduce(max,alist)

# example
print(max_in_list([1,2,3,42]))
    
### Problem 8 ###

def map1(listWords):
    '''
    This function maps a list of words into a list of integers
    representing the lengths of the corresponding words.
    This function uses a for-loop.
    Input: a list of strings.
    Output: a list of integers.
    '''
    l = len(listWords)
    listInts = [None]*l
    for i in range(l):
        listInts[i] = len(listWords[i])
    return listInts

# example
print(map1(['a','be','can','doll']))

def map2(listWords):
    '''
    This function maps a list of words into a list of integers
    representing the lengths of the corresponding words.
    This function uses the higher order function map().
    Input: a list of strings.
    Output: a list of integers.
    '''
    return list(map(len,listWords))

# example
print(map2(['a','be','can','doll']))
    
def map3(listWords):
    '''
    This function maps a list of words into a list of integers
    representing the lengths of the corresponding words.
    This function uses list comprehensions.
    Input: a list of strings.
    Output: a list of integers.
    '''    
    l = len(listWords)
    listInts = [len(listWords[i]) for i in range(l)]
    return listInts

# example
print(map3(['a','be','can','doll']))

### Problem 9 ###

from functools import reduce # import reduce module

def find_longest_word(listWords):
    '''
    This function takes a list of words and returns the length of the longest one.
    Input: a list of wtrings.
    Ouput: an integer, representing the length of the longest string.
    '''
    listInts = list(map(len,listWords)) # create a list of the length
    maxInt = reduce(max,listInts) # find the largest number in the list of length
    return maxInt

# example
print(find_longest_word(['a','be','can','doll']))

### Problem 10 ###

def filter_long_words(listWords,n):
    '''
    This function takes a list of words and an integer n and
    returns the list of words that are longer than n.
    Input: listWords: a list of strings;
           n: an integer.
    Output: a list of strings.
    '''
    return list(filter(lambda x:len(x)>n, listWords))

# example
print(filter_long_words(['This','is','Silvia'],4))

### Problem 11 ###

def translate(listWords):
    '''
    This is a function that takes a list of English words and returns a list of
    Swedish words.
    This function uses the higher order function map().
    Input: a list of strings.
    Output: a list of strings.
    '''
    myDict = {"merry":"god",
"christmas":"jul","and":"och","happy":"gott","new":"nytt","year":"år"}
    return list(map(lambda x: myDict[x],listWords))

# example
print(translate(['merry','christmas','and','happy','new','year']))

### Problem 12 ###
def myMap(function,myList):
    '''
    Implement the higher order function map().
    '''
    newlist=[] # create an empty new list
    for i in myList:
        newlist.append(function(i)) # add function(i) to the new list
    return newlist
    
print(myMap(lambda x: x+1,[1,2,3,4,5,42]))
    
def myFilter(function,myList):
    '''
    Implement the higher order functions filter().
    '''
    newlist=[] #create an empty new list
    for i in myList:
        if function(i)==True:
            newlist.append(i) #if Ture, add to newlist
    return newlist
    
print(myFilter(lambda x:x>4,[1,2,3,4,5,42]))
    
def myReduce(function,myList):
    '''
    Implement the higher order function reduce(). 
    '''
    accum=myList[0] # let accum be the first iterator in myList
    for i in myList[1:]: # for every i starting from the second place in myList
       accum=function(accum,i) # funciton accum and i
    return accum

print(myReduce(max,[1,2,3,4,5,42]))
