#import libraries
import csv 
import os

#file path to csv data
budget_csv = os.path.join("Resources", "budget_data.csv")
#file path to output
output = os.path.join("Analysis", "output.txt")

#define list variables
total_months = []
running_pl = []
monthly_change = []

#read in csv
with open(budget_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader) 
    #loop through csv: add month to list, add profit to list
    for rows in csvreader:
        total_months.append(rows[0])
        running_pl.append(int(rows[1]))
        
    #loop through running total to calculate monthly difference
    #send monthly difference to list variable
    for i in range(len(running_pl)-1):
        monthly_change.append(running_pl[i+1]-running_pl[i])

#calculations based on list
month_count = len(total_months)
total = sum(running_pl)
average_change = round(sum(monthly_change)/len(monthly_change),2)
max_change = max(monthly_change)
min_change = min(monthly_change)

#store output in a variable
analysis_output =  (f"Financial Analysis\n"
                    f"------------------------\n"
                    f"Total Months: {month_count}\n"
                    f"Total: ${total}\n"
                    f"Average Change: ${average_change}\n"
                    f"Greatest Increase in Profits: ${max_change}\n"
                    f"Greatest Decrease in Profits: ${min_change}\n"
                    )

#print output to terminal
print(analysis_output)

#export output to .txt file
with open(output,'w') as textfile:
    textfile.write(analysis_output)

