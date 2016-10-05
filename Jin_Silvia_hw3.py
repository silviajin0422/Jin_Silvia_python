# -*- coding: utf-8 -*-
"""
@author: Silvia

homework 03 Group D

09/29/2016
"""

import pandas as pd # import pandas
import matplotlib.pyplot as plot # for plot purpose later

### Problem 01 ###
'''
Search for the IRIS dataset on the internet.
You should quickly find the UCI machine learning repository.
Instead of downloading the files, figure out how to directly 
load the files from the internet into Python and add the column
names suing Python code instead of an editor.
'''

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', names = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class'])
# read the data from the internet, put the column names into the data frame


### Problem 02 ###
'''
Using Pandas, display the first ten and thelast ten rows of the data.
'''
df.head(n = 10) # display the first 10 rows 
df.tail(n = 10) # display the last 10 rows


### Problem 03 ###
'''
Using Pandas, print simple location statistics (Count, Mean, STD,
Min, 25%, 50%, 75%, MAX).
There is a single method call that will accomplish this.
'''

df.describe() #generate various summary statistics


### Problem 04 ###
'''
Write a function that accepts a list of numbers that represent numbers of 
bins and, using Pandas, plots a histogram for each of the numberic columns
at each bin size. For example, if I call your function with [10,50,100] as 
bin sizes, the function should plot 12 histograms (3 for each numeric variable).
Group the histograms by the column name.
'''

##Prof G - COuld you get these values from df?
columnname = ['sepal length', 'sepal width', 'petal length', 'petal width', 'class']
def plotHist(binSizes):
    '''
    This function takes in a list of bin sizes and plot the histgrams
    of the data for each bin size
    Input: a list of numbers, each number representing a bin size
    Ouput: 4n histograms, of each column in the data with corresponding bin size
    '''
    for col in columnname[0:4]: # forloop: look at each column
        for i in binSizes: # for each column: use each of the bin size
            df.hist(column = col, bins = i) # plot the histgram
            
# example
plotHist([10,50,100])

            
### Problem 05 ###
'''
Plot a box plot for each of the numeric column.
'''

plot.figure('sepal length box')#creat a new figure for sepal length
df['sepal length'].plot.box()#box plot in the figure created
plot.figure('sepal width box')#creat a new figure for sepal width
df['sepal width'].plot.box()#box plot in the figure created
plot.figure('petal length box')#creat a new figure for petal length
df['petal length'].plot.box()#box plot in the figure created
plot.figure('petal width box')#creat a new figure for petal width
df['petal width'].plot.box()#box plot in the figure created


### Problem 06 ###
'''
Plot a bar chart for the nominal column.
'''

df['class'].value_counts().plot.bar()
# first we count the frequency of each name in the 'class' column
# using the value_counts() function
# then we plot the bar chart for the frequency