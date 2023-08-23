travel_log = [
    {
        "country" : "A",
        "visits"  : 12,
        "cities"  : ["a", "b", "c"]
    }, 
    {
        "country" : "B",
        "visits"  : 5,
        "cities"  : ["d", "e", "f"]
    }
]


def add_new_country(country, visits, cities):
    country_dict = {}
    country_dict["country"] = country
    country_dict["visits"] = visits
    country_dict["cities"] = cities
    
    travel_log.append(country_dict)
    
    print(f"You have visited {country} {visits} times")
    print(f"You have been to {cities}")
    
add_new_country("Russia", 2, ["g", "h", "i"])
print(travel_log)

