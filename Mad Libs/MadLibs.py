'''
MadLibs.py
A program that reads in text files and lets the user add their own text 
anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file
Created on Jan 4, 2016

@author: lucy
'''

adj=list()
n=list()
adv=list()
vb=list()
myFile=open('madlibs.txt') # read a text file
myWords=myFile.read() # original string
words=myWords.replace('.',' ') # replace periods with white space
print words.split()
for word in words.split():
    if word=='ADJECTIVE':
        adjective=raw_input('Enter an adjective: \n')
        adj.append(adjective)
    elif word=='NOUN':
        noun=raw_input('Enter a noun: \n')
        n.append(noun)
    elif word=='VERB':
        verb=raw_input('Enter a verb: \n')
        vb.append(verb)   
    elif word=='ADVERB':
        adverb=raw_input('Enter an adverb: \n')
        adv.append(adverb)
for myWord in adj:
    print myWord
    maxNum=adj.index(myWord)+1
    myWords=myWords.replace('ADJECTIVE',myWord,maxNum)
for myWord in n:
    maxNum=n.index(myWord)+1
    myWords=myWords.replace('NOUN',myWord,maxNum)  
for myWord in vb:
    maxNum=vb.index(myWord)+1
    myWords=myWords.replace('VERB',myWord,maxNum)
for myWord in adv:
    maxNum=adv.index(myWord)+1
    myWords=myWords.replace('ADVERB',myWord,maxNum)

print 'Your story:\n'+ myWords  
    