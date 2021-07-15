#import libraries
import csv 
import os

#file path to csv data
budget_csv = os.path.join("Resources", "budget_data.csv")

total_months = []
running_pl = []
monthly_change = []

with open(budget_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader) #example defined this variable... can I just call the next function?
    
    for rows in csvreader:
        total_months.append(rows[0])
        running_pl.append(int(rows[1]))
        

    for i in range(len(running_pl)-1):
        monthly_change.append(running_pl[i+1]-running_pl[i])

month_count = len(total_months)
total = sum(running_pl)
average_change = round(sum(monthly_change)/len(monthly_change),2)
max_change = max(monthly_change)
min_change = min(monthly_change)

print("Financial Analysis")
print("------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: ${max_change}")
print(f"Greatest Decrease in Profits: ${min_change}")



