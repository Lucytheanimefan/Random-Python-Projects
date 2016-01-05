'''
Caesar Cipher
A user interface that encrypts and decrypts messages based on the Caesar Cipher. Require user input.
Based on caesarCipher.py by http://inventwithpython.com/hacking
Created on Jan 1, 2016
@author: lucy
'''


import PyperClip
from Tkinter import *

# Create user interface
root=None
entryBox=None
myText=None

def decipher():
    # message=string to be encrypted/decrypted
    #message='This is my secret message'

    # encryption/decryption key
    #key=13

    # tells program to encrypt or decrypt
    #mode='encrypt'   
    # every possible symbol that can be encrypted
    LETTERS='!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`a bcdefghijklmnopqrstuvwxyz{|}~'    
    global entryBoxMess
    global entryBoxKey
    global entryBoxMode
    global myText
    message=entryBoxMess.get()
    key=int(entryBoxKey.get()) 
    mode=entryBoxMode.get()   
    translated=''
    # capitalize string in message
    message=message.upper() 
    # run encryption/decryption code on each symbol in message String
    for symbol in message:
        if symbol in LETTERS:
            # get the encrypted (or decrypted) number for this symbol
            num=LETTERS.find(symbol) # get the number of the symbol
            if mode=='encrypt':
                num=num+key
            elif mode=='decrypt':
                num=num-key            
        # handle the wrap-around if num is larger than the length of
        # LETTERS or less than 0
            if num>=len(LETTERS):
                num=num-len(LETTERS)
            elif num<0:
                num=num+len(LETTERS)        
        # add encrypted/decrypted number's symbol at the end of translated
            translated=translated+LETTERS[num]
        else:
        # just add the symbol without encrypting/decrypting
            translated=translated+symbol
    # set label to translated message
    myText.set("Here is the encrypted message: \n"+translated+"\nThis text was copied to your clipboard.")
    # copy the encrypted/decrypted string to the clipboard
    PyperClip.copy(translated)

def createTextBox(parent):
    global entryBoxMess
    global entryBoxKey
    global entryBoxMode
    entryBoxMess=Entry(parent)
    entryBoxKey=Entry(parent)
    entryBoxMode=Entry(parent)
    entryBoxMess.insert(0,"Message/code")
    entryBoxKey.insert(0,"Key #")
    entryBoxMode.insert(0, "'encrypt' or 'decrypt?'")
    entryBoxMess.pack()
    entryBoxKey.pack()
    entryBoxMode.pack()

def addTextLabel(root):
    global myText
    myText=StringVar()
    myText.set("The Caesar Cipher encryption/decryption will appear here")
    myLabel=Label(root, textvariable=myText)
    myLabel.pack()
    
def main():
    global root
    root=Tk()
    root.title("Caesar Cipher")
    
    myButton=Button(root, text="Submit a message to encrypt", command=decipher)
    createTextBox(root)
    myButton.pack()
    addTextLabel(root)
    root.mainloop()
    
main()