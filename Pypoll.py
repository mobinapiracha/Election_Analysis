# Add our dependencies 
import csv 
import os 

# Assign a variable for a file to load and the path 
# Direct path file load 
# file_to_load = 'Resources/election_results.csv'
#Indirect path file load 
file_to_load = os.path.join("Resources","election_results.csv")
#Let's create a text file to analyze election data
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter 
total_votes = 0

# Candidate Options 
candidate_options = []

# Declare empty dictionaries 
candidate_votes = {}

# Open the election results and read the file 
#two methods 
#1st method 
# election_data = open(file_to_load, 'r')
with open(file_to_load) as election_data:
# To do: Read and Analyze the data here.
    file_reader = csv.reader(election_data)

# Read and print the header row 
    headers = next(file_reader)
    print(headers)


    #Print each row in the csv file 
    for row in file_reader:
        # Add to toal vote count
        total_votes += 1
        # Print the candidate name for each row
        candidate_name = row[2]

        # If candidate does not match any existing candidate
        if candidate_name not in candidate_options:
        # Add it to the list of candidates
            candidate_options.append(candidate_name)

        # 2. Begin tracking that candidate's vote count. 
            candidate_votes[candidate_name] = 0 
        # Add a vote to candidate's count
        candidate_votes[candidate_name] += 1


# Print the candidate list 
print(candidate_options)

# Print candidatte vote dictionary   
print(candidate_votes)

# Determine the percentage of votes for each candidate by looping through the counts 
# 1. Iterate through the candidate list 
for candidate_name in candidate_votes: 
    # 2. Retreive vote count of a candidate 
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage 
    vote_percentage = float(votes)/float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes. 
    print(f"{candidate_name}: received {vote_percentage:,.1f}% of the vote")

# Close the file 
election_data.close()

# Using the with statement open the file as a text file 
outfile = open(file_to_save, "w")
# Write some data 
outfile
outfile.write("Counties in the Election\n--------------------------\nArapahoe\nDenver\nJefferson")


# Close the file 
outfile.close()

