from bs4 import BeautifulSoup
import requests

url = "https://www.kjmotorsports.com/"

response = requests.get(url)
print(response.status_code)
print(response.content)

htmlcontent = response.content

soup = BeautifulSoup(htmlcontent,"html.parser")
print(soup.prettify())
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.p)
print(soup.a)
print(soup.find_all('a'))
print(soup.find(id =""))

for link in soup.find_all('a'):
    print(link.get('href'))

for image in soup.find_all('img'):
    print(image.get('src'))

product = soup.find_all('div',class_='level0 submenu')
print(product)

