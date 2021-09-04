#Importing Data from the CSV file
import os
import csv

#Set path for file
csvpath = os.path.join("..","Resources","budget_data.csv")

# Declare variables to create lists for the data provided
months = []
profit_losses = []
change = []

#Open the csv
with open(csvpath, newline = '', encoding = 'utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #Read and skip the header of the csv file
    csvheader = next(csvfile)
    #print(csvheader)
    
    #input data into lists
    for row in csvreader:
        #append the total months and total profits to their corresponding lists
        months.append(row[0])
        profit_losses.append(int(row[1]))
        
    #Count the total number of months     
    total_months = len(months) 
    
    #Calculating net total
    net_total = sum(profit_losses)
   
    for i in range(1, len(profit_losses)):
        #Find the average between months
        change.append(profit_losses[i] - profit_losses[i-1])
        
        #Find the average of these values 
        average_change = sum(change) / len(change)
        
        #Find the date and value of the greatest increase
        greatest_increase = max(change)
        greatest_increase_date = str(months[change.index(max(change))+1])
        
        #Find the date and value of the greatest decrease
        greatest_decrease = min(change)
        greatest_decrease_date = str(months[change.index(min(change))+1])
        
    
#Generic Text to introduce analysis
print ("Financial Analysis :")
print ("--------------------")
#Analysis Results
print(f'Total Months:{len(months)}')
print(f'Total: ${sum(profit_losses)}')
print(f'Average Change: ${round(average_change)}')
print(f'Greatest Increase: {(greatest_increase_date)} ${(greatest_increase)}')
print(f'Greatest Decrease: {(greatest_decrease_date)} ${(greatest_decrease)}')

#Outputting Analysis on a txt file
    