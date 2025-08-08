#{
#    key: [list] ,
#    key2: {Dict}
#}

#travel_log ={
#    "France" = "Paris" , "lille" , "Dijon"
# one key represent one values
# }

travel_log = {
    "France": {"citied_visited":["Paris" , "lille" , "Dijon"] , "total_vist":12}
}

 #Nested list inside dictionaries :
# [{
#{
#    key: [list] ,
#    key2: {Dict}

#}]

travel_log_list = [
    {
        "country": "France" ,
        "cities_visited": ["Paris" , "Lille" , "Dijon"],
        "total_vist": 12
    },
    {
        "country": "Germany" ,
        "cities_visited": ["Berlin" , "Hamburg" , "Stuttgart"],
        "total_vist": 13
    },
]
# Challenge
# Write a function to add the countries in list of nested dictionaries
def add_new_country(country_visited , cities_visited , total_vist):
    new_country = {}
    new_country["country"] = country_visited
    new_country["cities_visited"] = cities_visited
    new_country["total_vist"] = total_vist
    travel_log_list.append(new_country)
# print acc needs to travel_log_list
add_new_country("France", "Paris", "Hamburg")
print(travel_log_list)