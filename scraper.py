from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.tomorrowland.com/en/festival/line-up/'

# opening connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")


eventdays = page_soup.findAll("div", {"class": "eventday"})
#containers = eventdays[0].findAll("div", {"class": "stage__content"})
#stages = page_soup.findAll("div", {"class": "stage__content"})

###
# Stage Title
#containers[0].find("div","stage__title").h5.text

# Stage Location
#containers[0].find("div","stage__title").p.text

# Artists
#for artist in containers[0].findAll("li"):
#	print(artist.text)


#filename = "products.csv"
#f = open(filename, "w")

#headers ="brand, product_name, shipping\n"

#f.write(headers)
artist_count = 0
i = 0
day_number = 0
weekend_number = 0


for eventday in eventdays:
    # Get Weekend
    day_number += 1
    if(day_number <= int(len(page_soup.findAll("div", {"class": "eventday"}))/2)):
        print(int(len(page_soup.findAll("div", {"class": "eventday"}))/2))
        weekend_number = 1
    else:
        print(int(len(page_soup.findAll("div", {"class": "eventday"}))/2))
        weekend_number = 2

    for stage in eventday.findAll("div","stage__content"):
        n = 0
        #stage_title = stages[i].find("div", "stage__title").h5.text
        #print("Stage Title 2 : " + stage_title)
        print("Stage Title: " + stage.h5.text)        

        #stage_location = stages[i].find("div", "stage__title").p.text
        #print("Stage Location: " + stage_location)
        print("Stage Location: " + stage.p.text)
        print("i ist: ", i)

        
        for artist in stage.findAll("li"):
            print("Weekend: ", weekend_number)
            print(artist.text.strip())

            #print(containers[i].findAll("li")[n].text.strip())
            n += 1
            artist_count += 1

        i += 1

#f.close()

print("Artist count: ", artist_count)
