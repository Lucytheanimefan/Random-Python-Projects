'''
MyLinkOpener.py
Opens all important links (to me) in txt files in separate browser tabs...because you never know when your browser
will suddenly exit on you while you have hundreds of tabs open
Created on Jan 5, 2016

@author: lucy
'''

import webbrowser, os

userFolder='C:\\Users\\lucy\\workspace\\AutomatePrac\\Link files\\'

# The following commented out code that make the text files with all the links have already been run
# and the files already exist in the folder

# social media links
# socialMedia=open(userFolder+'socialMedia.txt','w')
# socialMedia.write('https://www.facebook.com/\nhttps://www.twitter.com/')

# email links
# mail=open(userFolder+'mail.txt','w')
# mail.write('http://gmail.com/\nhttps://outlook.office.com/owa/#path=/mail')

# anime links
# anime=open(userFolder+'anime.txt','w')
# anime.write('http://www.crunchyroll.com/\nhttp://www.animemaru.com/wp-admin/edit.php\nhttp://kissanime.com/')

# iterate through all files in folder
for myfile in os.listdir(userFolder):
    myFile=os.path.join(userFolder,myfile)
    File=open(myFile)
    print File
    links=File.read()
    print links
    # iterate through all links in each file
    for link in links.split('\n'):
        print link 
        # open links in browser
        webbrowser.open(link)

