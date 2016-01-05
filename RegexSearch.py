'''
RegexSearch.py
Opens all .txt files in a folder and searches for 
any line that matches a user-supplied regular expression
Created on Jan 5, 2016
@author: lucy
'''
import re,os

userRegex=raw_input('Supply a Regex to look for in the folder: \n')
# Regex test case: \d{3}-\d{3}-\d{4}
userRegex=re.compile(userRegex)
userFolder=raw_input('Supply a folder path: \n') # folder path goes here
# Folder test case: 'C:\\RegexSearchSample' 

# iterate through each txt file in the folder
for file in os.listdir(userFolder):
    myFile=os.path.join(userFolder,file)
    File=open(myFile)
    myText=File.read()
    found=userRegex.findall(myText)
    print found
    