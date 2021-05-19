import bs4 as bs
import urllib.request
import pandas as pd

 
##sauce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
##soup = bs.BeautifulSoup(sauce,'lxml')

#nav = soup.nav

##for url in nav.find_all('a'):
##   print(url.get('href'))

##for paragraph in soup.find_all('p'):
##    print(paragraph.text)

##print(soup.get_text)

##body = soup.body
##for paragraph in body.find_all('p'):
##    print(paragraph.text) 

##for div in soup.find_all('div', class_='body'):
##    print(div.text)

'''
table = soup.table
# or
table = soup.find('table')

table_rows = table.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row)

dfs = pd.read_html('https://pythonprogramming.net/parsememcparseface/', header = 0)

for df in dfs:
    print(df)
'''

sauce = urllib.request.urlopen('https://pythonprogramming.net/sitemap.xml').read()
soup = bs.BeautifulSoup(sauce,'xml')

print(soup)

for url in soup.find_all('loc'):
    # this is wrong ----print(url.get('href'))
    print(url.text)
