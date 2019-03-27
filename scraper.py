from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

### Line-Up URL
my_url = 'https://www.tomorrowland.com/en/festival/line-up/'

### Opening connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

### Parse HTML
page_soup = soup(page_html, "html.parser")

### Find all div tags with the class "eventday"
eventdays = page_soup.findAll("div", {"class": "eventday"})

### Init artist counter
artist_count = 0
### Init day counter
day_number = 0
### Init weekend counter
weekend_number = 0

### For each eventday in all eventdays
for eventday in eventdays:
    day_number += 1

    ### Get Weekend 
    ### Short version of: foreach eventday count up and return total number of days
    if(day_number <= int(len(page_soup.findAll("div", {"class": "eventday"}))/2)):
        weekend_number = 1
    else:
        weekend_number = 2
    
    ### For each stage in the current eventday
    for stage in eventday.findAll("div","stage__content"):
        ### Output stage host
        print("Stage Host: " + stage.h5.text)  

        ### Output stage location
        print("Stage Location: " + stage.p.text)

        ### For each artist in the current stage
        for artist in stage.findAll("li"):
            ### Output weekend number
            print("Weekend: ", weekend_number)

            ### Output artist name
            print(artist.text.strip())

            ### Increase artist counter
            artist_count += 1

### Output artist counter
print("Artist count: ", artist_count)
