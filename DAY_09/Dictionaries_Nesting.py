# Syntax
#dictionaries = {
#    key: value
#}

programming_dictionaries = {
    "Bug": "The values where expected output not comes" ,
    "Function": "Which can be called again and again"
}

# Retriving the data items from dictionaries
print(programming_dictionaries.get("Bug"))
print(programming_dictionaries["Function"])

# Adding in the dictionaries
programming_dictionaries["Loop"] = "The action done again and again"
print(programming_dictionaries["Loop"])

# Empty dictionary
empty_dictionary = {}

# Edit the dictionary
programming_dictionaries["Bug"] = "Error"
print(programming_dictionaries["Bug"])

# Loop through dictionary
for key in programming_dictionaries:
    print(key)
    print(programming_dictionaries[key])
