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

votes.sort(reverse=True)

for i in range(len(uniquecandidate)):
    result = zip(uniquecandidate, votes, votepct) # zips lists together
result_list = list(result)

result_list.sort(key=lambda x: x[1], reverse=True) # want to sort by vote number

# Print to terminal 
print("===============================")
print("Election Results")   
print("===============================")
print("Total Votes :" + str(d) +","+ str(e)+"," +str(f))    
print("-------------------------------")
for i in range(len(uniquecandidate)):
    print(uniquecandidate[i] + ": " + "{:.3f}".format(votepct[i]) +"% (" + str(votes[i])+ " votes)")
print("===============================")
print("The Winner is: " + winner)
print("===============================")

# Print to text file
with open('election_results.txt', 'w') as text:
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
