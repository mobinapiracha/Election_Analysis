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
# Initialize a total vote counter 
total_votes = 0
# Candidate Options and Votes 
candidate_options = []
candidate_votes = {}
# Tracking Winning Candidate, Vote Count and Percentage 
winning_candidate = ""
winning_count = 0 
winning_percentage = 0 
# Open the election results and read the file 
#two methods 
#1st method 
# election_data = open(file_to_load, 'r')
with open(file_to_load) as election_data:
# To do: Read and Analyze the data here.
    file_reader = csv.reader(election_data)
# Read and print the header row 
    headers = next(file_reader)
    #Print each row in the csv file 
    for row in file_reader:
        # Add to total vote count
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

# Save the results to our text file 
with open(file_to_save, 'w') as txt_file:

# Print the final vote count to the terminal 
    election_results = ( 
        f"\nElection Results\n"
        f"------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"------------------------\n")
    print(election_results, end ="")
#Save the final vote count to the text file 
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through the counts 
    # 1. Iterate through the candidate list 
    for candidate_name in candidate_votes: 
        # 2. Retreive vote count of a candidate 
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage 
        vote_percentage = float(votes)/float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes. 
        candidate_results = (
            f"{candidate_name}: {vote_percentage: .1f}% ({votes:,})\n")

# Print out winning candidate, vote count and percentage to the terminal  
        print(candidate_results)

# Save the candidate results to our text file 
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # 1. Determine if votes are greater than winning count  
        if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. If true then set winning_count = votes and winning percent = vote percentage 
            winning_count = votes 
            winning_percentage = vote_percentage
            # 3. Set the winning candidate equal to the candidate's name 
            winning_candidate = candidate_name
# Print winning candidate's result to the terminal 
    winning_candidate_summary = (
    f"--------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count: ,}%\n"
    f"Winning Percentage: {winning_percentage: .1f}%\n"
    f"---------------------\n")
    print(winning_candidate_summary)

# Save the winning candidate name on text file 
    txt_file.write(winning_candidate_summary)



