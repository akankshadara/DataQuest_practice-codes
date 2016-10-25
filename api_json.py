import requests
# Make a get request to get the latest position of the international space station from the opennotify api.
response = requests.get("http://api.open-notify.org/iss-now.json")
print response.status_code

####
Make a list of fast food chains.
best_food_chains = ["Taco Bell", "Shake Shack", "Chipotle"]
print(type(best_food_chains))

# Import the json library
import json

# Use json.dumps to convert best_food_chains to a string.
best_food_chains_string = json.dumps(best_food_chains)
print(type(best_food_chains_string))
print best_food_chains
print best_food_chains_string

# Convert best_food_chains_string back into a list
print(type(json.loads(best_food_chains_string)))

# Make a dictionary
fast_food_franchise = {
    "Subway": 24722,
    "McDonalds": 14098,
    "Starbucks": 10821,
    "Pizza Hut": 7600
}

# # We can also dump a dictionary to a string and load it.
fast_food_franchise_string = json.dumps(fast_food_franchise)
print(type(fast_food_franchise_string))
fast_food_franchise_2 = json.loads(fast_food_franchise_string)


# Call the API here.
url = "http://api.open-notify.org/astros.json"
import json
import requests

r = requests.get(url)
print (r.status_code)
data = r.json()
# print data['number']
print data['number']



