from bs4 import BeautifulSoup
import requests

url = "https://getpython.wordpress.com/"
source = requests.get(url)
soup = BeautifulSoup(source.text, 'html.parser')

title = soup.find('title')
print("This is with html tags :", title)
print("This is without html tags :", title.string)

qwery = soup.find('h1')
print("This is without html tags:", qwery.text)

links = soup.find('a')  # i extracted link using "a" tag
print('Links :',links)

print('href :',links['href'])
print('class :',links['class'])

many_link = soup.find_all('a')
total_links = len(many_link)
print("total links in my website :", total_links)
print()
print('--------')
for i in many_link[:6]:
    print(i)
print('--------')

second_link = many_link[1]
print(second_link)
print()
print("href is :", second_link['href'])

nested_div = second_link.find('div')
print('Nested Div :',nested_div)
print()
z = (nested_div['class'])
print('Class of nested_div :',z)
print('Type of nested_div :',type(z))
print()
#  " " .join () method use to convert list type  into string type
print("class name of div is :", " ".join(nested_div['class']))
print('--------')

##scrap data from wikipedia

wiki = requests.get("https://en.wikipedia.org/wiki/World_War_II")
soup = BeautifulSoup(wiki.text, 'html.parser')
print(soup.find('title'))

##find html tags with classes

ww2_contents = soup.find_all("div", class_='toc')
for i in ww2_contents:
    print(i.text)

overview = soup.find_all('table', class_='infobox vevent')
for z in overview:
    print(z.text)
