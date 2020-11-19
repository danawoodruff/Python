#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.
#As an example, your analysis should look similar to the one below:

#Election Results
#-------------------------
#Total Votes: 3521001
#-------------------------
#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
#O'Tooley: 3.000% (105630)
#-------------------------
#Winner: Khan
#-------------------------

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import os
import csv

file = os.path.join("Resources","election_data.csv")

# Create data lists
candidates = []
uniquecandidate = []
votes = []
votepct = []

# Initialize the variables
count = 0   # Number of votes recorded.

# Open the CSV using the set path "file"

with open(file, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

    # Loop through each row for information
    for row in csvreader:    
      count = count + 1  # Use count to count the number votes in this dataset

      #Read candidate name from column 3
      candidates.append(row[2])

    # Create a set to cull the unique candidate names
    for person in set(candidates):
        uniquecandidate.append(person)
        
        a = candidates.count(person)  # a is the total votes per candidate
        votes.append(a)
        
        b = round(((a/count)*100),3)    # b is the rounded percent of total votes per candidate
        votepct.append(b)
        
    maxvotes = max(votes)
    winner = uniquecandidate[votes.index(maxvotes)]
    
# how to sort descending by % of vote
# why is rounding kind of iffy

# Print to terminal 
print("=========================")
print("Election Results")   
print("=========================")
print("Total Votes :" + str(count))    
print("-------------------------")
for i in range(len(uniquecandidate)):
    print(uniquecandidate[i] + ": " + str(votepct[i]) +"% (" + str(votes[i])+ " votes)")
print("=========================")
print("The Winner is: " + winner)
print("=========================")

# Print to text file
with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(unique_candidate))):
        text.write(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + " votes)\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------------\n")
