# First Commit
# This is a tomorrowland websracper used to show the artists, stages and hosts
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.tomorrowland.com/en/festival/line-up/stages/friday-19-july-2019'

# opening connection, grabbing the page 
uClient = uReq(my_url)
page_html= uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class":"stage__content"})
eventdays = page_soup.findAll("div", {"class":"eventdays"})

###
# Stage Title
#containers[0].find("div","stage__title").h5.text

# Stage Location
#containers[0].find("div","stage__title").p.text

# Artists
#for artist in containers[0].findAll("li"):
#	print(artist.text)

#div_info = containers[0].find("div","item-info")

#filename = "products.csv"
#f = open(filename, "w")

#headers ="brand, product_name, shipping\n"

#f.write(headers)

i = 0
for container in containers:
    stage_title = containers[i].find("div","stage__title").h5.text
    print("Stage Title: "+ stage_title)

    stage_location = containers[i].find("div","stage__title").p.text
    print("Stage Location: "+ stage_location)

    for artist in containers[i].findAll("li"):
        print("Artist Number: %d " %i)
	


	#f.write(brand + "," + product_name.replace(",", "|") + "," + shipping + "\n")
    
    i += 1
	#brand = div_info.div.a.img["title"]
#f.close()

#for eventday in eventdays:
	#date = 