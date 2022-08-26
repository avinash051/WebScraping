"""
Here we use to scrap the website
 1. using the API
 2. Html web scraping using tool like bs4

 For achieving these kind of scraping we need to install -
 1. pip install requests
 2. pip install bs4
 3. pip install html5lib

  """

import requests
from bs4 import BeautifulSoup
url = "https://www.zerodha.com/"

# Step1 - Get the HTML
r = requests.get(url)
htmlContent = r.content
print(htmlContent)

# step2 - Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
#print(soup.prettify())

# step3 - HTML traversal

title = soup.title
print(title)
#find all anchor tags

anchor = soup.find_all('a')
for i in anchor:
    print(i)

#find all paragraph

para = soup.find_all('p')
for j in para:
    print(j)

print(soup.find_all('p', class_ = 'lead'))

navbarSupportedContent = soup.find('navbarSupportedContent')

for items in navbarSupportedContent.stripped_strings:
    print(items)