#In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)

# You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:

# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.

# As an example, your analysis should look similar to the one below:

import os
import csv

csvpath = os.path.join("..","PyPoll","election_data.csv")
x = 1
print(x)

#Creates dictionary to be used for candidate name and vote count.
poll = {}

# The total number of votes each candidate won
vote_count = 0

with open (csvpath, newline="") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")

    # A complete list of candidates who received votes
    csv_header = next(csvreader)
    
    print(csv_header)

    # column assignment
    for row in csvreader:
        vote_count += 1
        if row[2] in poll.keys():
            poll[row[2]] += 1
        else:
            poll[row[2]] = 1

    print(f'Election Results')
    print(f'----------------------')
    print(f'Total Number of Votes: {vote_count}')
    print(f'----------------------')

    for key, value in poll.items():
        print(f'{key}: {round((value/vote_count* 100),3)}% ({value})')
    print(f'----------------------')
    print(f'Winner: '+ max(poll, key=poll.get))
    print(f'----------------------')


