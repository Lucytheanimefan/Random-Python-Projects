'''
Caesar Cipher Hacker
A user interface that encrypts and decrypts messages based on the Caesar Cipher. Require user input.
Based on caesarCipher.py by http://inventwithpython.com/hacking
Created on Jan 1, 2016
@author: lucy
'''

from Tkinter import *

# Create user interface
root=None
entryBox=None
myText=None

def decipher():
    LETTERS='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    global entryBoxMess
    global myText
    message=entryBoxMess.get()
    i=0  
    string=[]
   
    for key in range(len(LETTERS)):      
        translated=''
        for symbol in message:
            if symbol in LETTERS:
                num=LETTERS.find(symbol) # get the number of the symbol
                num=num-key            

                if num<0:
                    num=num+len(LETTERS)        

                translated=translated+LETTERS[num]
            else:
                translated=translated+symbol
        string.append('Key #%s: %s' % (key, translated))
    # print results in Tkinter window
    Arraydata=""
    for i in string:
        Arraydata=Arraydata+i+'\n' # WHAT'S WRONG?
    myText.set(Arraydata)

def createTextBox(parent):
    global entryBoxMess
    entryBoxMess=Entry(parent)
    entryBoxMess.insert(0,"Code to decipher")
    entryBoxMess.pack()

def addTextLabel(root):
    global myText
    myText=StringVar()
    myText.set("Decryptions will appear here")
    myLabel=Label(root, textvariable=myText)
    myLabel.pack()
    
def main():
    global root
    root=Tk()
    root.title("Caesar Cipher Hacker")
    
    myButton=Button(root, text="Decrypt", command=decipher)
    createTextBox(root)
    myButton.pack()
    addTextLabel(root)
    root.mainloop()
    
main()