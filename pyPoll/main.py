#PyPoll
import os
import csv

csvpath = os.path.join("../election_data.csv")

#The total number of votes cast
voterValue = 0
    
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)

    for row in csvreader:
        if row[0] != "string":
            voterValue += 1

#A complete list of candidates who received votes
with open(csvpath, newline='') as csvfile:

    candidateList = csv.reader(csvfile, delimiter=',', skipinitialspace=True) 
    
    csv_header = next(candidateList)

    Candidate = []
    for row in candidateList:
        if row[2] not in Candidate:
            Candidate.append(row[2])  

#The total number of votes each candidate won
khanVotes = 0
correyVotes = 0
liVotes = 0
tooleyVotes = 0
    
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    for row in csvreader:
        if row[2] == "Khan":
            khanVotes += 1
        elif row[2] == "Correy":
            correyVotes += 1
        elif row[2] == "Li":
            liVotes += 1
        elif row[2] == "O'Tooley":
            tooleyVotes += 1

#The percentage of votes each candidate won
khanPercentage = (khanVotes / voterValue) * 100
correyPercentage = (correyVotes / voterValue) * 100
liPercentage = (liVotes / voterValue) * 100
tooleyPercentage = (tooleyVotes / voterValue) * 100

#The winner of the election based on popular vote.
pollWinner = 0
winnerName = "String"

pollResults = [khanVotes, correyVotes, liVotes, tooleyVotes]

for number in pollResults:
    if (int(number) > int(pollWinner)):
        pollWinner = number

if (int(pollWinner) == int(khanVotes)):
    winnerName = "Khan"
    
elif (int(pollWinner) == int(correyVotes)):
    winnerName = "Correy"
    
elif (int(pollWinner) == int(liVotes)):
    winnerName = "Li"
    
elif (int(pollWinner) == int(tooleyVotes)):
    winnerName = "O'Tooley"

#Print election results
print("Election results")
print("-------------------------")
print(f"Total votes: {voterValue}")
print("-------------------------")
print(f"Khan: {khanPercentage}% ({khanVotes})")
print(f"Correy: {correyPercentage}% ({correyVotes})")
print(f"Li: {liPercentage}% ({liVotes})")
print(f"O'Tooley: {tooleyPercentage}% ({tooleyVotes})")
print("-------------------------")
print(f"Winner: {winnerName}")
print("-------------------------")

#Output to text file
f = open('electionResults.txt','a')
f.write("Election results")
f.write('\n' + "-------------------------")
f.write('\n' + f"Total votes: {voterValue}")
f.write('\n' + "-------------------------")
f.write('\n' + f"Khan: {khanPercentage}% ({khanVotes})")
f.write('\n' + f"Correy: {correyPercentage}% ({correyVotes})")
f.write('\n' + f"Li: {liPercentage}% ({liVotes})")
f.write('\n' + f"O'Tooley: {tooleyPercentage}% ({tooleyVotes})")
f.write('\n' + "-------------------------")
f.write('\n' + f"Winner: {winnerName}")
f.write('\n' + "-------------------------")
f.close()