#import libraries
import csv
import os

#resource path
poll_csv = os.path.join("Resources", "election_data.csv")

#output path
#output = os.path.join("Analysis", "pypoll_ouput.txt")

#define some variables

candidate_percent = {}
candidate_votes = {}
total_votes = 0

#read in csv 
with open(poll_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
#loop through and count total votes + create dictionary of candidates w/ votes
    for rows in csvreader:
        total_votes += 1
        
        if rows[2] in candidate_votes:
            candidate_votes[rows[2]] +=1
        else:
            candidate_votes = 1

#loop through candidate directory to find vote %
    for candidate in candidate_votes:
        candidate_percent = (candidate_votes[candidate]/total_votes)*100

        




        
        

    
    
