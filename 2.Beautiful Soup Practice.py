import requests
from bs4 import BeautifulSoup
'''
##Example 1

result=requests.get('https://google.com')

print(result.status_code)
print(result.headers)

src=result.content

soup=BeautifulSoup(src,'lxml')
links=soup.find_all('a')

for link in links:
    if 'About' in link.text:
        print(link)
        print(link.attrs['href'])

##Output

200
{'Date': 'Mon, 04 May 2020 16:09:27 GMT', 'Expires': '-1', 'Cache-Control': 'private, max-age=0', 'Content-Type': 'text/html; charset=ISO-8859-1', 'P3P': 'CP="This is not a P3P policy! See g.co/p3phelp for more info."', 'Content-Encoding': 'gzip', 'Server': 'gws', 'X-XSS-Protection': '0', 'X-Frame-Options': 'SAMEORIGIN', 'Set-Cookie': '1P_JAR=2020-05-04-16; expires=Wed, 03-Jun-2020 16:09:27 GMT; path=/; domain=.google.com; Secure, NID=203=Rk6X_BW0wvj8ZqVHTBqJpLTYqeM8Fzs8iFNmlbWZgI27sfEH8IYU0pduyqxEUVDPKEdrtiNUSaHEzCR5_jLhCB1f0sndsTTIZCCTuD3m6ap3tob0vOrdV40agwaff4CwUeIwRsBaM70y3xAiP-j-NjDSvXrVEvUp50Tb48p1cyU; expires=Tue, 03-Nov-2020 16:09:27 GMT; path=/; domain=.google.com; HttpOnly', 'Alt-Svc': 'h3-Q050=":443"; ma=2592000,h3-Q049=":443"; ma=2592000,h3-Q048=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"', 'Transfer-Encoding': 'chunked'}
<a href="/intl/en/about.html">About Google</a>
/intl/en/about.html

'''

##Example 2
'''
result=requests.get('https://www.whitehouse.gov/briefings-statements/')
src=result.content
soup=BeautifulSoup(src,'lxml')
line1=soup.find_all('h2')
urls=[]

for h2_tag in line1:
    a_tag = h2_tag.find('a')
    urls.append(a_tag.attrs['href'])
    for link in a_tag:
        print(link.string)
print(urls)
'''


'''
##Example 3

from bs4 import BeautifulSoup
# To keep things simple and also reproducible, consider the following HTML code
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; their names:
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
<b class="boldest">Extremely bold</b>
<blockquote class="boldest">Extremely bold</blockquote>
<b id="1">Test 1</b>
<b another-attribute="1" id="verybold">Test 2</b>
"""
##with open('index.html', 'w') as f:
    ##f.write(html_doc)
##soup = BeautifulSoup(html_doc, "lxml")
##print(soup.prettify())
# Tag:
# Finds the first occurrence of usage for a "b"
# bold tag.
##print(soup.b)

# The "find" function also does the same, where it
# only finds the first occurrence in the HTML doc
# of a tag with "b".
##print(soup.find('b'))

# If we want to find all of the elements on the page
# with the "b" tag, we can use the "find_all" function.
##print(soup.find_all('b'))

# Name:

# This gives the name of the tag. In this case, the
# tag name is "b".
##print(soup.b.name)

# We can alter the name and have that reflected in the
# source. For instance:
##tag = soup.b
##print(tag)
##tag.name = "blockquote"
##print(tag)
##tag=soup.find_all('p')
##print(tag)

# Attributes:

##tag = soup.find_all('b')[2]
##print(tag)

# This specific tag has the attribute "id", which
# can be accessed like so:
#print(tag['id'])

#tag = soup.find_all('b')[3]
#print(tag)

# We can even access multiple attributes that are
# non-standard HTML attributes:
##print(tag['id'])
##print(tag['another-attribute'])

# If we want to see all attributes, we can access them
# as a dictionary object:
#tag = soup.find_all('b')[3]
#print(tag)

#print(tag.attrs)

# These properties are mutable, and we can alter them
# in the following manner.
#print(tag)
#tag['another-attribute'] = 2
#print(tag)

# We can also use Python's del command for lists to
# remove attributes:
#del tag['id']
#del tag['another-attribute']
#print(tag)

# Multi-valued Attributes
##tag = soup.find_all('b')[3]
##print(tag)
#print(tag.string)

# We can use the "replace_with" function to replace
# the content of the string with something different:
##tag.string.replace_with("This is another string")
##print(tag)
'''
