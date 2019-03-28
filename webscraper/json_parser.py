### Output.json contains a "demo"

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import json
import re

### Line-Up URL
my_url = 'https://www.tomorrowland.com/en/festival/line-up/'

### Opening connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

### Parse HTML
page_soup = soup(page_html, "html.parser")

### Find all div tags with the class "eventday"
days = page_soup.findAll("div", {"class": "eventday"})
#eekends = page_soup.findAll("div", {"class": "weekend-switch"})
weekends = page_soup.findAll("div", class_=re.compile('weekend-switch__button'))
days = page_soup.findAll("div", class_=re.compile('eventday-switch__button'))
### Init artist counter
artist_count = 0
### Init day counter
day_number = 0
### Init weekend counter
weekend_number = 0

dict_weekends = []
dictionary = {}

# for eventday in eventdays:
#     day_number += 1

#     ### Get Weekend
#     ### Short version of: foreach eventday count up and return total number of days
#     if(day_number <= int(len(page_soup.findAll("div", {"class": "eventday"}))/2)):
#         weekend_number = 1
#     else:
#         weekend_number = 2
#     if weekend_number not in weekends:
#         weekends.append(weekend_number)

#     for weekend in weekends:
#         dictionary[weekend] = {}
#         for eventday in eventdays:
#             dictionary[weekend][eventday] = {}
#             for stage in eventday.findAll("div","stage__content"):
#                 ### Output stage host
#                 #item[stage.]
#                 print("Stage Host: " + stage.h5.text)
#                 dictionary[weekend][eventday][stage] = {}

total_day_number = 0
for day in days:
    total_day_number += 1
    if(total_day_number <= int(len(page_soup.findAll("div", {"class": "eventday"}))/2)):
        weekend_number = 1
    else:
        weekend_number = 2
    if weekend_number not in dict_weekends:
        dict_weekends.append(weekend_number)



for weekend in weekends:
        #print(weekend.span.text)
        #print(weekend)
    dictionary[weekend.span.text] = {}
    # day_number = 0
    #for day in days:
    #     string = "Day "
    #     day_number += 1
    #     string += str(day_number)
    #     #print(stage.h5.text)
    #     print(day_number)
    #     if(day_number <= total_day_number/2 ):
    #         dictionary[weekend][string] = {}
    #     else:
    #         dictionary[weekend][string] = {}
    #     # for stage in day.findAll("div","stage__content"):
        #     dictionary[weekend][day][stage] = {}
        #     for artist in artists:
        #         dictionary[weekend][day][stage] = artist



print(dictionary)