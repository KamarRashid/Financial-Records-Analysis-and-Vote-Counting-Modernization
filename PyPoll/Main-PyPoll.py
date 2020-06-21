# Your task is to create a Python script that analyzes the votes and calculates each of the following:
    # The total number of votes cast
    # A complete list of candidates who received votes
    # The percentage of votes each candidate won
    # The total number of votes each candidate won
    # The winner of the election based on popular vote.

# As an example, your analysis should look similar to the one below:
    # Election Results
    # -------------------------
    # Total Votes: 3521001
    # -------------------------
    # Khan: 63.000 % (2218231)
    # Correy: 20.000 % (704200)
    # Li: 14.000 % (492940)
    # O'Tooley: 3.000 % (105630)
    # -------------------------
    # Winner: Khan
    # -------------------------

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
#-----------------------------------------------------------------------------------------------------------------------

# importing modules
import os
import csv
from collections import Counter

# module for reading csv files
csvpath = os.path.join("Resources", "PyPoll_election_data.csv")
# reading csv data file
with open(csvpath) as csvfile:
    csvReader = csv.reader(csvfile, delimiter=",")

    #header of data set
    csv_header = next(csvReader)

    # creating a dictionary of poll data from reader
    candidateVotes = {}
    candidatePercent = {}
    # decalre variables
    votesTotal = 0

    # analysis calculations
    # looping through candidate name row in csvReader file
    for row in csvReader:
        candidateName = row[2]
        # calculating total # of votes
        votesTotal += 1
        # name.append()
        # adding candidate name to dict and giving it a vote count
        if candidateName not in candidateVotes:
            # 2 dicts: for votes toals and another to calculate votes %
            candidateVotes[candidateName] = 1
            candidatePercent[candidateName] = 1

        # counting # votes for each candidate
        else:
            # 2 dicts: for votes toals and another to calculate votes %
            candidateVotes[candidateName] += 1
            candidatePercent[candidateName] += 1

    # calculating the percentages candidates received
    for key in candidatePercent:
        candidatePercent[key] = round((candidatePercent[key] / votesTotal) * 100,2)

    # calculating winner of election
    winnerKey = max(candidateVotes, key=candidateVotes.get)
    
    # printing analysis to terminal
    print("")
    print("-------------------------------------------------")
    print("Election Results")
    print("-------------------------------------------------")
    print(f"Total Votes: {votesTotal}")
    print("-------------------------------------------------")
    #printing candidate voter stats
    for key in candidateVotes:
        print(f"Candidate: {key} | Vote %: {candidatePercent[key]} % | Votes:{candidateVotes[key]}")
    print("-------------------------------------------------")
    print(f"Winner: {winnerKey}")
    print("-------------------------------------------------")

    #print analysis to text file
    with open("Poll_Report.txt", "w") as text_file:
        print("---------------------------------------------------", file=text_file)
        print("Election Results", file=text_file)
        print("---------------------------------------------------", file=text_file)
        print(f"Total Votes: {votesTotal}", file=text_file)
        print("---------------------------------------------------", file=text_file)
        #printing candidate voter stats
        for key in candidateVotes:
            print(f"Candidate: {key} | Vote %: {candidatePercent[key]} % | Votes: {candidateVotes[key]}", file=text_file)
        print("---------------------------------------------------", file=text_file)
        print(f"Winner: {winnerKey}", file=text_file)
        print("---------------------------------------------------", file=text_file)
        text_file.close()
