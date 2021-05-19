'''
Identifiers:
\d any number
\D anything but a number
\s space
\S anything but  space
\w any character
\W anything but a character
.  any character except a newline
\. a period
\b whitespace around words


Modifiers:
{1,3} we're expecting 1-3
+ Match 1 or more
? Match 0 or 1
* Match 0 or more
$ match the end of a string
^ matching the beginning of a string
| either or 
[] range or "Variance" [A-Z]
{X} expecting x amount


White space characters:
\n new line 
\s space 
\t tab
\e escape
\f form feed 
\r return

DONT'T FORGET:
. + * ? [ ] $ ^ ( ) | \ 

'''
import urllib.request
import urllib.parse
import re
"""
exampleString = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97, and his grandfather, Oscar, is 102 
'''

ages = re.findall(r'\d{1,3}', exampleString)
names = re.findall(r'[A-Z][a-z]*',exampleString)

print(ages)
print(names)

ageDict = {}
x=0
for eachname in names:
    ageDict[eachname]= ages[x]
    x+=1

print(ageDict)
"""
url = 'https://pythonprogramming.net'
values = {
    's':'basics',
    'submit':'search'
}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

paragraphs = re.findall(r'<p>(.*?)</p>', str(respData))

saveFile = open('regex_re_tut.txt','a+')
for eachP in paragraphs:
    saveFile.write(eachP+"\n")

saveFile.close()

