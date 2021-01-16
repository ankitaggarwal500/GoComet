// To Create a Scraping/Crawling application that can crawl medium.com
import requests
from bs4 import BeautifulSoup
url="https://medium.com"
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')
print(soup.prettify)
#Get the title of html page
title=soup.title
#print(type(title.string))
#Get all paragraphs from page
paras=soup.find_all('p')
#print(paras)
#print(soup.find_all("p", class_="blog"))
anchors=soup.find_all('a')
#Get text from elements
print(soup.find('p').get_text())
print(soup.get_text())
anchors=soup.find_all('a')
all_links=set()
#For all links
for link in anchors:
  if(link.get('href')!='#'):
       linkText="https://medium.com" +link.get('href')
       all_links.add(link)
        #print(linkText)
root=soup.find(id='root')
for elem in root.contents:
    print(elem)








