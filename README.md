# Election_Analysis

## Project Overview 
In this analysis we will be doing an election audit of results for a US congressional precinct in Colorado. We will help tabulate the results of this election. 

Requirements: 

* Calculate total number of votes cast. 
* Get a complete list of candidates who received votes.
* Calculate the total number of votes each candidate received 
* Calculate the percentage of votes each candidate won. 
* Determine the winner of the election based on popular vote. 

## Resources 
- Data Sources: election_results.csv 
- Software: Python 3.9.1, Visual Studio Code 1.52.1

## Summary 
The analysis of the election shows us that:

* There were a total of 369,711 votes cast in this election
* The candidates contesting this election were:

i.  Charles Casper Stockham 

ii.  Diane DeGette 

iii. Raymon Anthony Doane 

* The candidate results were:

i. Charles Casper received 85,213 number of votes 

ii. Diana DeGette received 272,892 number of votes 

iii. Raymon Anthony Doane received 11,606 number of votes

* The winner of the election was: 

 Diana DeGette who received 73.8% of vthe votes and 272,892 number of votes 

## Challenge Overview 

In this challenge, the election commission has requested some additional data to complete the audit: 

* The voter turnout for each county 
* The percentage of votes from each county of the total count
* The county with the highest voter turnout 

### Overview of Election Audit 
The purpose of this audit is to gather additional data regarding the election outcome to ensure greater transparency in the election. Therefore, the election commission has requested voter turnout for each county, percentage of votes from each county as a percentage of total count and the county with the highest voter turnout. This information allows us to understand this election in greater detail, looking at what county carries the most weight in the election and how results in each county affects the outcome of the election. Therefore, conducting a more detailed analysis of the election outcome can help us understand who won the election, why they won it and which county was the most important county in determining the election. 

### Election-Audit Results 
Let's address a number of important questions in this audit: 

 How many votes were cast in this congressional election?

* The total number of votes cast in this election are 369,711. 

* Provide a breakdown of the no. of votes and % of total votes for each county in the precint. 

The total number of votes and percentage of total vote by county: 

i. Jefferson County received 38,855 votes, which accounts for 10.5% of the total vote 

ii. Denver County received 306,055 votes, which accounts for 82.8% of the total vote

iii. Arapahoe County received 24,801 votes, which accounts for 6.7% of the total vote 

* Which county had the largest number of votes? 

Denver county had the largest number of votes with 305,055 of the total 369,11 votes being cast in this county 

* Provide a breakdown of the no. of vote and % of total votes each candidate received

i. Charles Casper Stockham received a total of 85,213 votes which accounts for 23.0% of the total vote

ii. Diana DeGette received a total of 272,892 votes which accounts for 73.8% of the total vote.

iii. Raymon Anthony Doane received a total of 11,606 votes which accounts for 3.1% of the total vote. 

* Which candidate won the election, what was their vote count and their percentage of the total votes?

Diana DeGette overwhelmingly won this election receiving 272,892 out of the 369,711 votes, which accounts for 73.8% of the total vote, a landslide victory. 

# Election-Audit Summary

In this election, we've seen the power of programming, using programming languages like python to analyze election data, help tabulate election results and find all sorts of different election statistics such as voter turnout and county turnout. I believe that python scripts should definitely be used more frequently in calculating election results. In fact, by simply making a few modifications to this script we can create a sort of a template and tabualate results for every election. One modification we could make is simply to change the file paths on the script to the relevant file paths when conducting analysis. Another modification is to during loops, in our analysis we use indexing to extract candidate and county name for each row but when analyzing other election files the index number depends on the where the candidate names and county names are positioned in the dataset, if candidate name is on the 4th column then we have to index on the 3rd row. Therefore, by making a few modifications we can create a template script in which we can analyze any election result. 
