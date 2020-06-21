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

    #creating a list of poll data from reader
    pollData = list(csvReader)
    # print (pollData)

    #creating lists of voter ids, countys and candidates from pollData list
    voterID = list((int(rows[0]) for rows in pollData))
    county = list((rows[1] for rows in pollData))
    candidate = list((rows[2] for rows in pollData))

    # print(voterID)
    # print(county)
    # print (candidate)

    # analysis calculations
    # calculating total # of votes cast
    votesTotal = len(voterID)
    
    # determining the unique list of candidates who got votes
    
    # mylist = ['nowplaying', 'PBS', 'PBS',
    #           'nowplaying', 'job', 'debate', 'thenandnow']
    # uniqueCandidate_set = set(candidate)
    # print(uniqueCandidate_set)

    uniqueCandidate = []
    for rows in candidate:
        if rows not in uniqueCandidate:
            uniqueCandidate.append(rows)
    print(uniqueCandidate)
    candidateNum = len(uniqueCandidate)
    
    #calculating the # of votes each candidate got
    index = 0
    voteCount = 0
    candidateVotes = []
    
    for rows in candidate:
        
        #while index > (candidateNum):

        if (uniqueCandidate[index] == rows):
            voteCount += 1
        index += 1
    # reset vote count
        candidateVotes.append(voteCount)
        voteCount = 0
            # if rows == uniqueCandidate[index]:
            #     voteCount += 1
            #     candidateVotes[index].append(voteCount)
            #     index += 1

    print (f"votes: {candidateVotes}")
    

    
    # Counter(candidate).values()
    # for name in candidateNum  
    #     for range(0:)
    #     if rows = 
    # c= Counter(candidate)
    # print(c)

    # printing analysis to terminal
    print("")
    print("-------------------------------------------------")
    print("Election Results")
    print("-------------------------------------------------")
    print(f"Total Votes: {votesTotal}")
    print("-------------------------------------------------")
    #printing candidate voter stats
    for name in range(candidateNum):
        print (name)
        # print(f"Candidate: {uniqueCandidate[name]}, Vote %: , Votes: {candidateVotes[name]}")
    print("-------------------------------------------------")
    print("Winner: ")
    print("-------------------------------------------------")

    #print analysis to text file
    with open("Poll_Report.txt", "w") as text_file:
        print("-------------------------------------------------", file=text_file)
        print("Election Results", file=text_file)
        print("-------------------------------------------------", file=text_file)
        print(f"Total Votes: {votesTotal}", file=text_file)
        print("-------------------------------------------------", file=text_file)

        text_file.close()
