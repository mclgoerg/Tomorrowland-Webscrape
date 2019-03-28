### Standardized Dictionary for JSON Parsing
### Parameters:

festivalname = "Tomorrowland"
location = "Belgium"
year = 2019
weekends = ["Weekend 1", " Weekend 2"]
dict = {}

def create_dict(name, location, year, weekends):
    
    dict["Festival"] = name
    dict["Location"] = location
    dict["Year"] = year
    keys = weekends
    print(keys)


    for key in keys:
        dict[key] = {}

    #dict[key] = {}
    #dict["Weekends"] = {}

    
    

create_dict(festivalname, location, year, weekends)

print(dict)