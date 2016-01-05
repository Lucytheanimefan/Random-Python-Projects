'''
Phone Number Finder 
Finds phone numbers from text
Created on Jan 2, 2016
@author: lucy

'''
import re
from Tkinter import*


root=None
entryBox=None
myText=None

def findPhoneNum():
    global entryBoxMess
    global myText
    message=entryBoxMess.get()
    phoneRegex=re.compile(r'\(\d{3}\)\s\d{3}-\d{4} | \d{3}-\d{3}-\d{4}')
    mo=phoneRegex.findall(message) #mo is an array
    string=''
    for number in mo:
        string=string+number+'\n'
    myText.set(string) 
    print string

def createTextBox(parent):
    global entryBoxMess
    entryBoxMess=Entry(parent)
    entryBoxMess.insert(0,"Text")
    entryBoxMess.pack()

def addTextLabel(root):
    global myText
    myText=StringVar()
    myText.set("Phone Numbers")
    myLabel=Label(root, textvariable=myText)
    myLabel.pack()
    
def main():
    global root
    root=Tk()
    root.title("Phone Number Finder")
    myButton=Button(root, text="Find", command=findPhoneNum)
    createTextBox(root)
    myButton.pack()
    addTextLabel(root)
    root.mainloop()
    
main()