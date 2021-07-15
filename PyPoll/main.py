#import libraries
from collections import namedtuple
import csv
import os

#resource path
poll_csv = os.path.join("Resources", "election_data.csv")

#output path
output = os.path.join("Analysis", "pypoll_ouput.txt")

#define some variables
candidates = []
candidate_percent = []
candidate_votes = []
total_votes = 0

#read in csv 
with open(poll_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)
#loop through and count total votes + create list of candidates + add a vote for each occurrence of candidate
    for rows in csvreader:
        total_votes += 1
        if rows[2] not in candidates:
            candidates.append(rows[2])
            index = candidates.index(rows[2])
            candidate_votes.append(1)
        else:
            index = candidates.index(rows[2])
            candidate_votes[index] +=1

#loop through candidate votes list to caluclate vote %
    for votes in candidate_votes:
        vote_share = (votes/total_votes)*100
        vote_share = round(vote_share)
        vote_share = "%.3f%%" % vote_share
        candidate_percent.append(vote_share)

        
winner = max(candidate_votes)
index = candidate_votes.index(winner)
elected = candidates[index]

print(f"Election Results\n")
print(f"------------------------\n")
print(f"Total votes: {total_votes}\n")
print(f"------------------------\n")
for i in range(len(candidates)):
    print(f"{candidates[i]} : {str(candidate_percent[i])} ({str(candidate_votes[i])})")
print(f"------------------------\n")
print(f"Winner: {elected}\n")

        
    
#export output to .txt file
with open(output,'w') as textfile:
    textfile.write(f"Election Results\n")  
    textfile.write(f"------------------------\n")
    textfile.write(f"Total votes: {total_votes}\n")
    textfile.write(f"------------------------\n")
    for i in range(len(candidates)):
        textfile.write(f"{candidates[i]} : {str(candidate_percent[i])} ({str(candidate_votes[i])})\n")
    textfile.write(f"------------------------\n")
    textfile.write(f"Winner: {elected}")