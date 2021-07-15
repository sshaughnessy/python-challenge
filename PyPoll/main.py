#import libraries
import csv
import os

#resource path
poll_csv = os.path.join("Resources", "election_data.csv")

#output path
#output = os.path.join("Analysis", "pypoll_ouput.txt")

#define some variables

vote_count = {}
candidate_votes = {}
total_votes = 0

#read in csv 
with open(poll_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
#loop through and add candidate name for every row to a list
    for rows in csvreader:
        total_votes += 1
        
        if rows




        
        

    
    
