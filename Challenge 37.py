#Given numbers
countryPop = { "Japan":"127000000",
               "Germany":"81000000",
               "Iran":"77000000",
               "UK":"64000000",
               "Canada":"33000000",
               "Australia":"23000000",
               "USA":"317000000",
               "Bulgaria":"7000000",
               "Sweden":"10000000"}
#print the avaliable countrys
print("Avaliable countries:")
for country in countryPop:
    print("-", country)
#ask the user for 2 countrys, then add the population of both countries
country1 = input("Pick a first country? ")
country2 = input("Pick a second country? ")
if country1 in countryPop and country2 in countryPop:
    total_population = int(countryPop[country1]) + int(countryPop[country2])
    print(f"The total combined population of {country1} and {country2} is: {total_population}")
else:
    print("One or both of the countries you entered are not in the list, Try agian")
