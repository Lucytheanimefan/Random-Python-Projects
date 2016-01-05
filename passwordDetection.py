'''
Strong password detector 
Created on Jan 3, 2016
@author: lucy
'''
import re
from Tkinter import*

root=None
myText=None

def detectPass():
    global passwordBox
    global myText
    password=passwordBox.get()

    lowerRegex=re.compile(r'[a-z]') # check for lower case letter
    upperRegex=re.compile(r'[A-Z]') # check for upper case letter
    eightRegex=re.compile(r'(\S{8})+') # check for at least 8 characters
    digitRegex=re.compile(r'(\d)+') # check for at least 1 digit
    
    noLower=''
    noUpper=''
    noEight=''
    noDigit=''
    strong=''
    
    if lowerRegex.search(password)==None:
        noLower='Your password does not have a lower case letter.\n'
    if upperRegex.search(password)==None:
        noUpper='Your password does not have an upper case letter.\n'
    if eightRegex.search(password)==None:
        noEight='Your password needs at least 8 characters.\n'
    if digitRegex.search(password)==None:
        noDigit='Your digit needs at least 1 digit.\n'
    if noLower==noUpper and noEight==noDigit:
        strong='This is a strong password'
    
    myText.set(noLower+noUpper+noEight+noDigit+strong)

def createTextBox(parent):
    global passwordBox
    passwordBox=Entry(parent)
    passwordBox.insert(0,"Password")
    passwordBox.pack()

def addTextLabel(root):
    global myText
    myText=StringVar()
    myText.set("Password verification result")
    myLabel=Label(root, textvariable=myText)
    myLabel.pack()
    
def main():
    global root
    root=Tk()
    root.title("Password verification")
    myButton=Button(root, text="Verify", command=detectPass)
    createTextBox(root)
    myButton.pack()
    addTextLabel(root)
    root.mainloop()
    
main()
       
        