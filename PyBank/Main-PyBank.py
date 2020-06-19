# Your task is to create a Python script that analyzes the records to calculate each of the following:
    # The total number of months included in the dataset
    # The net total amount of "Profit/Losses" over the entire period
    # The average of the changes in "Profit/Losses" over the entire period
    # The greatest increase in profits(date and amount) over the entire period
    # The greatest decrease in losses(date and amount) over the entire period

# As an example, your analysis should look similar to the one below:
    # Financial Analysis
    # ----------------------------
    # Total Months: 86
    # Total: $38382578
    # Average  Change: $-2315.12
    # Greatest Increase in Profits: Feb-2012 ($1926159)
    # Greatest Decrease in Profits: Sep-2013 ($-2196167)

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
#-----------------------------------------------------------------------------------------------------------------------

# importing modules
import os
import csv

# module for reading csv files
csvpath = os.path.join("Resources","PyBank_budget_data.csv")
# reading csv data file
with open(csvpath) as csvfile:
    budgetData = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(budgetData)

    monthsTotal = sum(1 for row in budgetData)
    print (monthsTotal)
    
    # read each row of data after the header
    #for row in budgetData:
        
