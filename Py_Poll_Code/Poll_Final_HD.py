#Importing data from the CSV file
import os
import csv

#Set path for file
csvpath = os.path.join("..","Resources","election_data.csv")

# Declare variables to create lists for the data provided
votes = []
Khan = []
Correy = []
Li = []
OTooley = []

#Open the CSV
with open(csvpath, newline = '', encoding = 'utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
   
    #Read and skip the header of the csv file
    csvheader = next(csvfile)
    
    #Go through each row in the CSV file
    for row in csvreader:
        
        #Append the total votes to their corresponding lists
        votes.append(row[0])
        
        #if statements to count the total votes of each candidate
        if row[2] == "Khan":
            Khan.append(row[0])
        
        elif row [2] == "Correy":
            Correy.append(row[0])
        
        elif row[2] == "Li":
            Li.append(row[0])
            
        elif row[2] == "O'Tooley":
            OTooley.append(row[0])
        
        
    #Count the total number of votes and the total votes for each candidate   
    total_votes = len(votes) 
    Khan_votes = len(Khan)
    Correy_votes = len(Correy)
    Li_votes = len(Li)
    OTooley_votes = len(OTooley)
    
    
    #Percentage of votes per candidate
    Khan_percent = "{:.3%}".format((Khan_votes/total_votes))
    Correy_percent = "{:.3%}".format((Correy_votes/total_votes))
    Li_percent = "{:.3%}".format((Li_votes/total_votes))
    OTooley_percent = "{:.3%}".format((OTooley_votes/total_votes))
    
    #To find winner, create a dictionary with both the candidate names and their vote count total as lists
    candidates = ["Khan", "Correy", "Li","O'Tooley"]
    candidates_votes = [Khan_votes, Correy_votes, Li_votes, OTooley_votes]

    #Zip both lists and have the key=candidates and the value=candidates_votes; then use a max funtion to find the candidate with the highest count of votes
    candidates_and_votes = dict(zip(candidates,candidates_votes))
    key = max(candidates_and_votes, key=candidates_and_votes.get)

    
#Generic Text for introduction
print ("Election Results :")
print ("--------------------")

#Count + Percentages Output
print(f'Total Votes:{len(votes)}')
print ("--------------------")
print(f'Khan Total Votes: {(Khan_percent)} ({len(Khan)})')
print(f'Correy Total Votes: {(Correy_percent)} ({len(Correy)})')
print(f'Li Total Votes: {(Li_percent)} ({len(Li)})')
print(f"O'Tooley Total Votes: {(OTooley_percent)} ({len(OTooley)})")
print ("--------------------")

#Winner Output
print(f' Winner: {key}')
print("---------------------")


#Output of Election Results in txt
output=(
   f"Election Results\n"
   f"----------------------------\n"
   f"Total Votes:{len(votes)}\n"
   f"----------------------------\n"
   f"Khan Total Votes: {(Khan_percent)} ({len(Khan)})\n"
   f"Correy Total Votes: {(Correy_percent)} ({len(Correy)})\n"
   f"Li Total Votes: {(Li_percent)} ({len(Li)})\n"
   f"O'Tooley Total Votes: {(OTooley_percent)} ({len(OTooley)})\n"
   f"----------------------------\n"
   f" Winner: {key}\n"
   f"----------------------------\n"
   )

output_file = os.path.join("..","Txt_files","poll.txt")
with open(output_file,"w", newline='') as txt_file:
    txt_file.write(output)