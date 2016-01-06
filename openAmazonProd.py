'''
openAmazonProd.py
Opens all the product pages after searching a shopping site such as Amazon
Created on Jan 5, 2016

@author: lucy
'''
import requests, webbrowser, bs4, pyperclip

print('Searching...') # display text while downloading Amazon page
# copy desired search term to clipboard
res=requests.get('http://www.amazon.com/s?url=search-alias%3Daps&field-keywords='+pyperclip.paste().replace(' ','+')) 
res.raise_for_status

soup=bs4.BeautifulSoup(res.text,'html.parser')
links=soup.find_all('a',class_='a-link-normal a-text-normal')
maxNum=len(links)
amazon='amazon'
for i in range(min(20,maxNum)):
    if amazon in links[i].get('href') and links[i].get('href')!=links[i+1].get('href'):
        print links[i].get('href')
        webbrowser.open(links[i].get('href'))
    