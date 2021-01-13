counties = ["Arapahoe","Denver","Jefferson"]

if counties[1] == "Denver": 
    print(counties[1])

if "El Paso" in counties:
    print("El Paso is in the list of counties")
else:
    print("El Paso is not in the county list")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso are in the list of counties")
else:
    print("Arapahoe and El Paso is not in the list of counties")

# Iterating through lists and tuples 

for county in counties:
    print(county)

for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# Get Keys in a dictionary 

for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)


# Get the values in the dictionary 

for county in counties_dict.values():
    print(county)

for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))

# Get Key Value pairs of a Dictionary 

for key, value in counties_dict.items(): 
    print(key, value)

for county, voters in counties_dict.items():
    print(county, voters)

# Both methods work similarly except in one we are referencing

#Get each dictionary in the list of dictionaries 

voting_data = [{"county": "Arapahoe", "registered_voters": 422829},
                {"county": "Denver", "registered_voters": 463353},
                {"county": "Jefferson", "registered_voters": 432438}
]

for county_dict in voting_data: 
    print(county_dict)

for i in range(len(voting_data)):
    print(voting_data[i])

# Using nested for loops to get the values from the list of dictionaries 

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

# Number of registered voters in each dictionary 

for county_dict in voting_data:
    print(county_dict['registered_voters'])


# Only print county name for each dictionary 
for county_dict in voting_data: 
    print(county_dict['county'])

# Printing Formats 

# Votes original code 
# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# percentage_votes = (my_votes/total_votes) * 100 
# print("I received " + str(percentage_votes)+ "% of votes")

# Votes f string edited
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100} % of the total votes. ")

# Using F-String with Dictionaries
print(counties_dict)
for county, voters in county_dict.items():
    print(f"{county} county has {voters} registered voters")

#Multiline F strings 
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100: .2f}% of the total votes. ")

print(message_to_candidate)

# Skill Drill 

for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters")
