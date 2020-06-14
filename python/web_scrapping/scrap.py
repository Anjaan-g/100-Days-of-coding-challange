from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'

#open up the url and request the data in the site.
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
#finding the requested tag in the html file 
containers = page_soup.findAll("div", {"class":"item-container"})
for container in containers:
    brand = container.a.img["title"]
