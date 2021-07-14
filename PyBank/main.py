import csv 

file = "Resources/budget_data.csv"

with open(file) as budgetcsv:
    csvreader = csv.reader(budgetcsv, delimeter=",")

    csvheader = next(budgetcsv)

    for row in csvreader:
        