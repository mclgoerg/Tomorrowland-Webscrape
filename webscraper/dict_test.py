### Standardized Dictionary for JSON Parsing
### Parameters:

### Structure for calling the method
metadata = {
    "Festivalname": "Tomorrowland",
    "Location": "Belgium, Boom",
    "Year": "2019"
}

weekends = ["Weekend 1", " Weekend 2"]
dict = {}


def create_dict(metadata, weekends):
    if(metadata.get("Festivalname") != None and
       metadata.get("Location") != None and
       metadata.get("Year") != None):

        dict["Festival"] = metadata.get("Festivalname")
        dict["Location"] = metadata.get("Location")
        dict["Year"] = metadata.get("Year")

    else:
        raise KeyError

    keys = weekends

    for key in keys:
        dict[key] = {}

    #dict[key] = {}
    #dict["Weekends"] = {}


create_dict(metadata, weekends)

print(dict)
