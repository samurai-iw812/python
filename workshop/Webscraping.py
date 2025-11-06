import requests
from bs4 import BeautifulSoup #to parse the HTML content

response=requests.get("https://www.google.com")
print(response)

content=response.text #get the text content of the response
print (content)

soup=BeautifulSoup(content,'html.praser')
for link in soup.find_all('a'): #find all the links in the HTML content
    print(link.get('href'))
