# stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]



# # #1. Add "Edinburgh Waverley" to the end of the list
# stops.append("Edinburgh Waverley")
# # #2. Add "Glasgow Queen St" to the start of the list
# stops.insert(0, "Glasgow Queen St")
# #3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
# stops.insert(4, "polmont")
# # #4. Print out the index position of "Linlithgow"
# print(stops[5])
# # #5. Remove "Livingston" from the list using its name
# stops.remove("Livingston")
# # #6. Delete "Cumbernauld" from the list by index
# stops.pop(2)
# # #7. Print the number of stops there are in the list
# print(len(stops))
# # #8. Sort the list alphabetically
# stops.sort()
# # #9. Reverse the positions of the stops in the list
# stops.reverse()
# # #10 Print out all the stops using a for loop
# for stop in stops:
#        print(stop)



# users = {
#   "Jonathan": {
#     "twitter": "jonnyt",
#     "lottery_numbers": [6, 12, 49, 33, 45, 20],
#     "home_town": "Stirling",
#     "pets": [
#     {
#       "name": "fluffy",
#       "species": "cat"
#     },
#     {
#       "name": "fido",
#       "species": "dog"
#     },
#     {
#       "name": "spike",
#       "species": "dog"
#     }
#   ]
#   },
#   "Erik": {
#     "twitter": "eriksf",
#     "lottery_numbers": [18, 34, 8, 11, 24],
#     "home_town": "Linlithgow",
#     "pets": [
#     {
#       "name": "nemo",
#       "species": "fish"
#     },
#     {
#       "name": "kevin",
#       "species": "fish"
#     },
#     {
#       "name": "spike",
#       "species": "dog"
#     },
#     {
#       "name": "rupert",
#       "species": "parrot"
#     }
#   ]
#   },
#   "Avril": {
#     "twitter": "bridgpally",
#     "lottery_numbers": [12, 14, 33, 38, 9, 25],
#     "home_town": "Dunbar",
#     "pets": [
#       {
#         "name": "monty",
#         "species": "snake"
#       }
#     ]
#   }
# }

# # 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
# users["Jonathan"]["twitter"]
# # 2. Get Erik's hometown
# users["Erik"]["home_town"]
# # 3. Get the list of Erik's lottery numbers
# users["Erik"]["lottery_numbers"]
# # 4. Get the species of Avril's pet Monty
# users["Avril"]["pets"][0]["species"]
# # 5. Get the smallest of Erik's lottery numbers
# min(users["Erik"]["lottery_numbers"])
# # 6. Return an list of Avril's lottery numbers that are even
# evenNumbers = []
# for num in users["Avril"]["lottery_numbers"]:
#    if num % 2 == 0:
#        evenNumbers.append(num)
# # 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
# users["Erik"]["lottery_numbers"].append(7)
# # 8. Change Erik's hometown to Edinburgh
# users["Erik"]["hometown"] = "Edinburgh"
# # 9. Add a pet dog to Erik called "fluffy"
# users["Erik"]["pets"].append({"name": "fluffy", "species": "dog"})
# # 10. Add another person to the users dictionary
# users["Bob"] = {
#     "twitter": "bobby",
#     "lottery_numbers": [10, 54, 21, 14, 44], 
#     "home_town": "Hollywood", 
#     "pets": [
#         {
#          "name": "Itchy",
#          "species": "cat"
#          }
#      ]
#     }



united_kingdom = [
  {
    "name": "Scotland",
    "population": 5295000,
    "capital": "Edinburgh"
  },
  {
    "name": "Wales",
    "population": 3063000,
    "capital": "Swansea"
  },
  {
    "name": "England",
    "population": 53010000,
    "capital": "London"
  }
]

#1. Change the capital of Wales from `"Swansea"` to `"Cardiff"`.
united_kingdom[1]["captial"] = "Cardiff"
#2. Create a dictionary for Northern Ireland and add it to the `united_kingdom` list (The capital is Belfast, and the population is 1,811,000).
northern_ireland =  {
    "name": "Northern Ireland",
    "population": 1811000,
    "capital": "Belfast"
  }
united_kingdom.append(northern_ireland)

#3. Use a loop to print the names of all the countries in the UK.
for country in united_kingdom:
    print(country["name"])

#4. Use a loop to find the total population of the UK.
total = 0
for country in united_kingdom:
    total = total + country["population"]


