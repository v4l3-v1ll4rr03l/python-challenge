#imports
import csv

#specify file
f = open("PyPoll/Resources/election_data.csv", "r")

#read file
f_read = f.readlines()

#create variables to track and store relevant values
header = ''
tot_votes = 0
candidates = []
votes = []

#read file line by line
for line in f_read:

    #store values individual line of code
    temp = line.split(",")
    curr_candidate = temp[2].split("\n")[0]

    if tot_votes > 0:
        if curr_candidate in candidates:
            votes[candidates.index(curr_candidate)] += 1
        else:
            candidates.append(curr_candidate)
            votes.append(1)
    
    #store header
    else:
        header = line

    tot_votes += 1

#open file to write results
f = open("PyPoll/analysis.txt", "w")

#write results
f.write("\nElection Results\n-------------------------")
f.write("\nTotal Votes: " + str(tot_votes - 1))
f.write("\n-------------------------")
i = 0
for c in candidates:
    percentage = votes[i] / tot_votes * 100
    percentage = round(percentage, 3)
    f.write("\n" + candidates[i] + ": " + str(percentage) + "% (" + str(votes[i]) + ")")
    i += 1
f.write("\n-------------------------")
f.write("\nWinner: " + candidates[votes.index(max(votes))])
f.write("\n-------------------------")

f.close()
