
#Dana Woodruff
#PyBank

import os
import csv

file = os.path.join("Resources","budget_data.csv")

# Create data lists

profit = []
mthchanges = []
date = []

# Initialize the variables
 
count = 0
totalprofit = 0
beginprofit = 0
sumchangeprofits = 0
a = 0

# Open the CSV using the set path "file"

with open(file, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

    # Loop through each row for information
    for row in csvreader:    
      count = count + 1  # Use count to count the number months in this dataset
      
      date.append(row[0])   # To find date of greatest increase/decrease

      # Total Profit 
      profit.append(row[1])   #Populate "Profit" list
      totalprofit = totalprofit + int(row[1])   # Calculate the total profit
            
      # Avg change in monthly profits
      endprofit = int(row[1])
      mthchangeprofits = endprofit - beginprofit    # Calculate the avg profit change

      # Populate "mthchanges" list
      mthchanges.append(mthchangeprofits)

      sumchangeprofits = sumchangeprofits + mthchangeprofits # Calculate the sum of profit changes
      beginprofit = endprofit   # Reset beginning profit to the previous ending profit value

    #Calculate the avg change in profits
    countofchanges = count - 1   # Denominator
    a = mthchanges[0]          #Numerator. Subtracting the first month's "profit change".
    avgchange_profits = ((sumchangeprofits-a)/countofchanges)
    
    #Find the greatest increase and decrease in profits.
    greatest_inc_profits = max(mthchanges)
    greatest_dec_profits = min(mthchanges)

    increase_date = date[mthchanges.index(greatest_inc_profits)]
    decrease_date = date[mthchanges.index(greatest_dec_profits)]
    
    #Variables to create slices for commas.
    c = str(totalprofit)
    d = (c[0:2])
    e = (c[2:5])
    f = (c[5:9])
    g = str(avgchange_profits)
    h = (g[1])
    i = (g[2:5])
   
    # Print to terminal  
    print("========================================================")
    print("Financial Analysis")
    print("========================================================")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(d) +","+ str(e)+"," +str(f))
    print("Average Change: " + "$" + str(h) +","+ str(i))
    print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_inc_profits) + ")")
    print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_dec_profits)+ ")")
    print("--------------------------------------------------------")

    # Print to text file
with open('financial_analysis.txt', 'w') as text:
    text.write("========================================================\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("========================================================\n\n")
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total Profits: " + "$" + str(d) +","+ str(e)+"," +str(f) +"\n")
    text.write("    Average Change: " + '$' + str(h) +","+ str(i) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_inc_profits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_dec_profits) + ")\n")
    text.write("--------------------------------------------------------\n")