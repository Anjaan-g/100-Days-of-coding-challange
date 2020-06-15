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

filename = 'products.csv'
f = open(filename, 'w')

headers = "brand, product_name, shipping \n"

f.write(headers)



for container in containers:
    brand_container = container.find("div", {"class":"item-branding"})
    brand = brand_container.a.img["title"]
    
    title_container= container.find("a", {"class":"item-title"})
    product_name = title_container.text
    
    shipping_container = container.find("li", {"class":"price-ship"})
    product_shipping = shipping_container.text.strip()

    print("Brand: " + brand)
    print("Product Name: " + product_name)
    print("Shipping cost: " + product_shipping)

    f.write(brand + "," + product_name.replace(",","|") + "," + product_shipping + "\n")

f.close()