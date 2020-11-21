#Dana Woodruff
#PyPoll Nov 2020

import os
import csv

file = os.path.join("Resources","election_data.csv")

# Create data lists
candidates = []        #All candidates
uniquecandidate = []   #Each candidate
votes = []             #All votes
votepct = []           #Percentage votes

# Initialize the variables
count = 0   # Number of votes recorded.

# Open the CSV using the set path "file"

with open(file, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

    # Loop through each row for information
    for row in csvreader:    
      count = count + 1  # Use count to count the number votes in this dataset

      #Read candidate name from column 3 and add to list.
      candidates.append(row[2])

    # Create a set to cull the unique candidate names
    for person in set(candidates):
        uniquecandidate.append(person)
        
        a = candidates.count(person)  # a is the total votes per candidate
        votes.append(a)
        
        b = (a/count)*100   # b is the rounded percent of total votes per candidate
        votepct.append(b)
        
    maxvotes = max(votes)   # Uses function of max to determine maximum value assigned to each candidate
    winner = uniquecandidate[votes.index(maxvotes)] # Using maxvotes as index it finds this value and return's candidate name associated with value.
    
#Variables to create slices for commas.
    c = str(count)
    d = (c[0:1])
    e = (c[1:4])
    f = (c[4:7])

#Sorting in descending order of votes
for i in range(len(uniquecandidate)):
    result = zip(uniquecandidate, votes, votepct) # zips lists together for sorting
result_list = list(result)

result_list.sort(key=lambda x: x[1], reverse=True) # want to sort by vote number

name_elements = [name[0] for name in result_list]  #sorted name list by vote
vote_elements = [vote1[1] for vote1 in result_list]  #sorted vote list by vote
pct_elements = [pct[2] for pct in result_list]     #sorted percent list by vote

# Print to terminal 
print("===============================")
print("Election Results")   
print("===============================")
print("Total Votes :" + str(d) +","+ str(e)+"," +str(f))    
print("-------------------------------")
print("Khan:   ","{:.3f}".format(pct_elements[0]),"%  (",vote_elements[0],"votes)")
print("Correy: ","{:.3f}".format(pct_elements[1]),"%  (",vote_elements[1],"votes)")
print("Li:     ","{:.3f}".format(pct_elements[2]),"%  (",vote_elements[2],"votes)")
print("O'Tooley:","{:.3f}".format(pct_elements[3]),"%  (",vote_elements[3],"votes)")
print("===============================")
print("The Winner is: " + winner)
print("===============================")

# Print to text file
with open("election_results.txt", 'w') as text:
    text.write("================================\n")
    text.write("Election Results\n")
    text.write("================================\n")
    text.write("Total Vote: " + str(d) +","+ str(e)+"," +str(f) + "\n")
    text.write("--------------------------------\n")
    for i in range(len(set(uniquecandidate))):
        text.write(uniquecandidate[i] + ": " + "{:.3f}".format(votepct[i]) +"% (" + str(votes[i]) + " votes)\n")
    text.write("================================\n")
    text.write("The winner is: " + winner + "\n")
    text.write("================================\n")
