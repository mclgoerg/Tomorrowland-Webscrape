### Standardized dictionaryionary for JSON Parsing
### Parameters:
import json # das ist json
### Structure for calling the method
metadata = {
    "Festivalname": "Tomorrowland",
    "Location": "Belgium, Boom",
    "Year": "2019"
}

weekends = ["Weekend 1", " Weekend 2"]
days = ["Day 1", "Day 2", "Day 3"]
artists = ["Dr. Peackock", "Sefa", "Headhunterz"]
stages = ["Mainstage", "Atmosphere"]
dictionary = {}


def create_dictionary():
    if(metadata.get("Festivalname") != None and
       metadata.get("Location") != None and
       metadata.get("Year") != None):

        dictionary["Festival"] = metadata.get("Festivalname")
        dictionary["Location"] = metadata.get("Location")
        dictionary["Year"] = metadata.get("Year")

    else:
        raise KeyError
        

    for weekend in weekends:
        dictionary[weekend] = {}
        for day in days:
            dictionary[weekend][day] = {}
            for stage in stages:
                dictionary[weekend][day][stage] = {}
                for artist in artists:
                    dictionary[weekend][day][stage] = artist

    #dictionary[key] = {}
    #dictionary["Weekends"] = {}

#json = json.dumps(dictionary)
# 
create_dictionary()

#print(dictionary)
#print(json)

print(json.dumps(dictionary))
