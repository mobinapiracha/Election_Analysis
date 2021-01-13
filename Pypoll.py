import csv 
import os 

# Assign a variable for a file to load and the path 
# Direct path file load 
# file_to_load = 'Resources/election_results.csv'
#Indirect path file load 
file_to_load = os.path.join("Resources","election_results.csv")
#Let's create a text file to analyze election data
file_to_save = os.path.join("analysis", "election_analysis.txt")

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

#print each row in the csv file 
    for row in file_reader:
        print(row[0])

# To do: perform analysis. 
    print(election_data)

# Close the file 
election_data.close()

# Using the with statement open the file as a text file 
outfile = open(file_to_save, "w")
# Write some data 
outfile
outfile.write("Counties in the Election\n--------------------------\nArapahoe\nDenver\nJefferson")


# Close the file 
outfile.close()
