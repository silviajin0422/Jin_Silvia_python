'''
@author: Silvia Jin

HW 02


'''

### Problem 01 ###
'''
Write a version of a palindrome recogniser that accepts a file name from the
user, reads each line, and prints the line to the screen if it is a palindrome.
'''

def is_palindrome(word):
    '''
    This function is a palindrome recogniser.
    Input: a string of a word.
    Output: True if the word is a palindrome;
            False if the word is not a palindrome.
    '''
    if word == '': #base case: if the word is empty
        return True
    elif len(word) == 1: #base case: if only one character
        return True
    else:
        if word[0]==word[-1]: #recursion step: look at the first and last character
            return is_palindrome(word[1:-1])
    return False

def palin_recogniser(filepath):
    '''
    This function is a palindrome recogniser that accepts a file name from
    the user, reads each line, and prints the line to the screen if it is
    a palindrome.
    Input: a string which is a filepath.
    '''
    file = open(filepath) #open the file
    for line in file.read().split('\n'): # read the content line by line
        if is_palindrome(line): # check if palindrome
            print(line)

# example
palin_recogniser('test01.txt')

### Problem 02 ###
'''
According to Wikipedia, a semordnilap is a word or phrase that spells a
different word or phrase backwards. ("Semordnilap" is itself "palindromes"
spelled backwards.) Write a semordnilap recogniser that accepts a file name
(pointing to a list of words) from the user and finds and prints all pairs
of words that are semordnilaps to the screen. For example, if "stressed"
and "desserts" is part of the word list, then the output should include the
pair "stressed desserts". Note, by the way, that each pair by itself forms
a palindrome!
'''

def semord_recogniser(filepath):
    '''
    This function is a semordnilap recogniser from a file
    Input: a string which is a filepath.
    The function read through the content in the file and print
    semordnilap to the screen.
    '''
    file=open(filepath) #open the file
    words = file.read().split() #read word by word, save to a list
    l=len(words) #get the number of words
    result = [] # create an empty list to save result
    for i in range(l-1): # for loop: look at each word
        for j in range(i+1,l): # for loop: for each word, compare it to the words after it
            if words[i] == words[j][::-1]: # if there is such semordnilap 
                result.append(words[i]) # save the first word to the result
                result.append(words[j]) # save the second word to the result
    print(result)


# example
semord_recogniser('test02.txt')

### Problem 03 ###
'''
Write a procedure char_freq_table() that, when run in a terminal, accepts
a file name from the user, builds a frequency listing of the characters
contained in the file, and prints a sorted and nicely formatted character
frequency table to the screen.
'''
import operator

def char_fraq_table():
    '''
    This is a function that when run in a terminal, accepts
    a file name from the user, builds a frequency listing of the characters
    contained in the file, and prints a sorted and nicely formatted character
    frequency table to the screen.
    '''
    filepath = input('Please type the file name:') # take the filepath from the user
    file = open(filepath) # open the file
    words = file.read().split() # read the file word by word
    chars = [] # create an empty list
    for word in words: # for loop: look at each word
        for i in range(len(word)): # put each character in a list
            chars.append(word[i])
    freqs = {key: 0 for key in chars} # create a dictionary with all the characters
    for char in chars: # for each character, count them and save as values in the dictionary
        freqs[char] += 1
    keys = sorted(freqs.keys()) # sort the dictionary by the characters
    for word in keys: # print the dictionary with the sorted characters
        print("%s: %s" % (word, freqs[word]))

# example
char_fraq_table()
# Please input file name: test03.txt

### Problem 04 ###
'''
The International Civil Aviation Organization (ICAO) alphabet assigns code words to the letters of the English alphabet
acrophonically (Alfa for A, Bravo for B, etc.) so that critical combinations of letters (and numbers) can be pronounced
and understood by those who transmit and receive voice messages by radio or telephone regardless of their native
language, especially when the safety of navigation or persons is essential. Here is a Python dictionary covering one
version of the ICAO alphabet:
d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 'f':'foxtrot',
     'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima',
     'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo',
     's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey',
     'x':'x-ray', 'y':'yankee', 'z':'zulu'}
     
Your task in this exercise is to write a procedure speak_ICAO() able to translate any text (i.e. any string) into spoken
ICAO words. You need to import at least two libraries: os and time. On a mac, you have access to the system TTS
(Text-To-Speech) as follows: os.system('say ' + msg), where msg is the string to be spoken.
(Under UNIX/Linux and Windows, something similar might exist.)

Apart from the text to be spoken, your procedure also needs to accept two additional parameters: a float indicating the
length of the pause between each spoken ICAO word, and a float indicating the length of the pause between each word
spoken.
'''
import os
import time

def speak_ICAO(msg,pauseTime):
    '''
    This functions takes in a message and prounance the message using ICAO.
    Input: msg: a string of words.
           pauseTime: a number which represent the pause time between words.
    When running the function in the terminal, we will hear the message pronounced.
    '''
    # create the ICAO dictionary
    d = {'a':'alfa', 'b':'bravo', 'c':'charlie',
         'd':'delta', 'e':'echo', 'f':'foxtrot', 'g':'golf', 'h':'hotel',
         'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima',
         'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa',
         'q':'quebec', 'r':'romeo', 's':'sierra', 't':'tango',
         'u':'uniform', 'v':'victor', 'w':'whiskey', 'x':'x-ray', 'y':'yankee', 'z':'zulu'}
    # store the length of the message
    l = len(msg)
    # change the characters in the message to lowercase, for prounanciation purpose
    msg=msg.lower()
    for i in range(l): # look at each character in the message
        if msg[i] == ' ': # pause between words
            time.sleep(pauseTime)
        elif msg[i] in d: # otherwise, prounance the ICAO for the message
            os.system('say' + d[msg[i]])

# example
speak_ICAO('Silvia',0.25)

### Problem 05 ###
'''
A hapax legomenon (often abbreviated to hapax) is a word which occurs only once in either the written record of a
language, the works of an author, or in a single text. Define a function that given the file name of a text will return
all its hapaxes. Make sure your program ignores capitalization.
'''

def hapaxFinder(filepath):
    '''
    This function finds the hapax legomenon in a file.
    Input: a string of a filepath.
    Output: a list of all the hapax legomenons in the file.
    '''
    file = open(filepath) # open the file
    chars=file.read().lower().split() # read the content word by word, lower case
    hapaxes=[] # create an empty list to same the hapaxes
    freqs={key:0 for key in chars} # save the words in a dictionary
    for char in chars: # save the number of the words in the dictionary as well
        freqs[char] += 1
    for word in freqs: # if a word only appear once, it is a hapax
        if freqs[word]==1:
            hapaxes.append(word)    
    return hapaxes

# example
hapaxFinder('test05.txt')

### Problem 06 ###
'''
Write a program that given a text file will create a new text file in which all the lines from the original file are
numbered from 1 to n (where n is the number of lines in the file).
'''
def numFile(filepath):
    '''
    This function takes in a text file and create a new text file in which all the lines from the original file
    are numbered from 1 to n (where n is the number of lines in the file).
    Input: a string of a filepath.
    '''
    file=open(filepath) # open the file
    lines = file.read().split('\n') # read the file line by line
    file.close() # close the file
    newFilepath = 'numbered'+filepath # create a name for the new file
    newFile = open(newFilepath,'w') # create the new file
    for i in range(len(lines)): # for each line in the original file
        newFile.write(str(i)+' '+lines[i]+'\n') # write the line number and the line content
    newFile.close() # close the written file
 
# example
numFile('test06.txt')

### Problem 07 ###
'''
Write a program that will calculate the average word length of a text stored in a file (i.e the sum of all the lengths
of the word tokens in the text, divided by the number of word tokens).
'''

def aveLength(filepath):
    '''
    This function calculates the average word length of a text stored in a file.
    Input: a string of a filepath
    Output: a number, which is the average word length of the text stored in the file.
    '''
    file=open(filepath) # open the file
    words=file.read().split() # read the file word by word
    total = 0 # initialize the sum of the word length
    l = len(words) # number of words in the list
    for i in range(l): # look at each word
        total += len(words[i]) # add the length of each word to the total
    ave = total / l # calculate the average
    return ave

# example
aveLength('test07.txt')

### Problem 08 ###

'''
Write a program able to play the "Guess the number"-game, where the number to be guessed is randomly chosen between 1
and 20. (Source: http://inventwithpython.com)

This is how it should work when run in a terminal:

import guess_number
Hello! What is your name?
Torbjorn
Well, Torbjorn, I am thinking of a number between 1 and 20.
Take a guess.
10
Your guess is too low.
Take a guess.
15
Your guess is too low.
Take a guess.
18
Good job, Torbjorn! You guessed my number in 3 guesses!
'''

import random
def guess_number():
    '''
    This function lets the user play the guessnumber game in the terminal.
    '''
    # get user name
    name = input("Hello! What is your name?\n")
    # Prompt for the user to guess the number
    print("Well, %s, I am thinking of a number between 1 and 20." % name)
    # Generage the number randomly
    secret = random.randint(1, 20)
    # Take the guess from the user
    num = int(input("Take a guess.\n"))
    # count the guess number
    count = 1
    while num != secret:
        if num < secret: # if the guess is too low
            print("Your guess is too low.")
        elif num > secret: # if the guess is too high
            print("Your guess is too high.")
        num = int(input("Take a guess.\n"))
        count += 1 # store the number of guesses
    print("Good job, %s! You guessed my number in %d guesses!" % (name, count))

# example
guess_number()

### Problem 10 ###
'''
In a game of Lingo, there is a hidden word, five characters long.
The object of the game is to find this word by guessing, and in return receive two kinds of clues:
1) the characters that are fully correct, with respect to identity as well as to position, and
2) the characters that are indeed present in the word, but which are placed in the wrong position.
Write a program with which one can play Lingo. Use square brackets to mark characters correct in the sense of 1), and
ordinary parentheses to mark characters correct in the sense of 2). Assuming, for example, that the program conceals the
word "tiger", you should be able to interact with it in the following way:
import lingo
snake
Clue: snak(e)
fiest
Clue: f[i](e)s(t)
times
Clue: [t][i]m[e]s
tiger
Clue: [t][i][g][e][r]
'''

def lingo(word):
    '''
    This function lets the user play the lingo game in the terminal.
    Input: a string of word.
           In the function, we have the user to decide the word to be guessed.
    '''
    l=len(word) # store the length of the word
    while True:
        # take the guess from the user
        guess = input('Take a guess of a word with '+str(l)+ ' letters:')
        myOutput = '' # create an empty output
        if len(guess) == l: # the guess has to have the same length
            for i in range(len(word)): # look at each character
                if word.find(guess[i]) == i: # if both the character and the location is correct
                    myOutput = myOutput + '[' + guess[i]+']'
                elif guess[i] not in word: # if the guessed character is not currect
                    myOutput = myOutput + guess[i]
                else: # else: the character is currect, but the location is not correct
                    myOutput = myOutput +'(' + guess[i] + ')'
            print(myOutput) # give the hint
            if guess == word: # if the word is correct
                print('Congratulations! You got it!')
                break
        else: # if the guess does not have the same length
            print('The length is not current!')

# example
lingo('tiger')

### Problem 11 ###
'''
A sentence splitter is a program capable of splitting a text into sentences. The standard set of heuristics for sentence
splitting includes (but isn't limited to) the following rules:

Sentence boundaries occur at one of "."(periods), "?" or "!", except that

a. Periods followed by whitespace followed by a lower case letter are not sentence boundaries.

b. Periods followed by a digit with no intervening whitespace are not sentence boundaries.

c. Periods followed by whitespace and then an upper case letter, but preceded by any of a short list of titles are
   not sentence boundaries. Sample titles include Mr., Mrs., Dr., and so on.

d. Periods internal to a sequence of letters with no adjacent whitespace are not sentence boundaries (for example,
   www.aptex.com, or e.g).

e. Periods followed by certain kinds of punctuation (notably comma and more periods) are probably not sentence boundaries.

Your task here is to write a program that given the name of a text file is able to write its content with each sentence
on a separate line. Test your program with the following short text: Mr. Smith bought cheapsite.com for 1.5 million dollars,
i.e. he paid a lot for it. Did he mind? Adam Jones Jr. thinks he didn't. In any case, this isn't true... Well, with a
probability of .9 it isn't. The result should be:

Mr. Smith bought cheapsite.com for 1.5 million dollars, i.e. he paid a lot for it. \n
Did he mind? \n
Adam Jones Jr. thinks he didnt. \n
In any case, this isn't true... \n
Well, with a probability of .9 it isn't.
'''
def senSplitter(text):
    '''
    This function takes in a string of text and split the text by sentence into a list, in which each object is a sentence.
    Input: text (a string)
    Output: a list of strings, in which each string is a sentence.
    '''
    text = text.replace('\n',' ') # in case the text has several lines, we put them together
    newText=[] # create an empty new text
    isDot = False # initialize a boolean for later use
    currentSen = ''# create an empty string store the current sentence
    l = len(text) # get the length of the text
    i=0 # initialze a counter, i is the location in the text
    while True: # while loop
        # if i is out of the range of text (or the text is empty)
        if i == l:
            return newText # this is the base or final case, return the output
        # if i indicated the last character in text
        elif i == l-1:
            currentSen = currentSen + text[i] # add the current character to the current sentence
            newText.append(currentSen) # since it is the last loction, it must be a sentence, so add the sentence to the list
            currentSen = ''
        # otherwise, i indicates location before the last in text
        else:
            currentSen=currentSen + text[i] # add the current character to the current sentence
            if text[i]=='?': # if '?', must be the end of a sentence
                newText.append(currentSen)
                currentSen = ''
                isDot = False
            elif text[i]=='!': # if '!', must be the end of a sentence
                newText.append(currentSen)
                currentSen = ''
                isDot = False
            elif text[i] == '.': # if '.', store in the boolean
                isDot = True
            elif text[i] == ' ':
                # if period followed by space
                if isDot == True:
                    # case a: not a boundary
                    if text[i+1].islower():
                        isDot = False
                    # case c: not a boundary
                    elif text.find('Mr.',i-3) == i-3:
                        isDot = False
                    elif text.find('Ms.',i-3) == i-3:
                        isDot = False                        
                    elif text.find('Dr.',i-3) == i-3:
                        isDot = False
                    elif text.find('Mrs.',i-4) == i-4:
                        isDot = False
                    elif text.find('Miss.',i-5) == i-5:
                        isDot = False
                    elif text.find('Prof.',i-5) == i-5:
                        isDot = False
                    # otherwise: is a boundary
                    else:
                        newText.append(currentSen)
                        currentSen = ''
        i=i+1


def writeSenSplit(filepath):
    '''
    This function takes in a filepath and break the sentences in the file, and write each
    sentence in a line into a new file.
    '''
    file=open(filepath) # open the file
    text = file.read() # read the file, put the content into a string
    file.close() # close the file
    splittedText= senSplitter(text) # split the content, save it into a list
    newFilepath = 'splitted' + filepath # create a name for the new file
    newFile = open(newFilepath, 'w') # open the new file
    for i in range(len(splittedText)): # for each string in the list
        newFile.write(splittedText[i]+'\n') # write a sentence in a line into the new file
    newFile.close() # close the new file

# example
writeSenSplit('test11.txt')
