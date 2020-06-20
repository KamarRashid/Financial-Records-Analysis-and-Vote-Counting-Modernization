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
    csvReader = csv.reader(csvfile, delimiter=",")
    
    #header of data set
    csv_header = next(csvReader)
    
    #creating a list of budget data from reader
    budgetData = list(csvReader)
    # print (budgetData)

    #creating lists of dates and profit/losses from budgetData list
    budgetDate = list((rows[0] for rows in budgetData))
    budgetPL = list((int(rows[1]) for rows in budgetData))
    
    # print(budgetDate)
    # print(budgetPL)
    
    # analysis calculations
    # calculating total months in dataset
    monthsTotal = len(budgetData)

    # calculating net total of profil/loss over entire period
    p_lTotal = sum(budgetPL)

    # calculating average change in profil/loss over entire period
    # creating list to store moving changes
    sumChange = []
    # looping through rows in profit/loss list
    for rows in range(1,len(budgetPL)):
        # if rows <= len(budgetPL):
            #storing moving changes in a new list called sumChange
            # sumChange.append(budgetPL[rows]-budgetPL[rows-1])
        #storing moving changes in a new list called sumChange
        sumChange.append(budgetPL[rows]-budgetPL[rows-1])
    # calculating the average of changes: sum of changes/# of changes
    avgChange = sum(sumChange) / len(sumChange)

    # calculating greatest increase and decrease in profits
    # variables
    increase_maxProfit = 0
    increase_year = ""
    decrease_maxProfit = 0
    decrease_year = ""
    counterMax = 1
    counterMin = 1

    # looping through list of profit/loss changes
    for row in sumChange:

        # calculating the greatest increase in profits
        if row > increase_maxProfit:
            increase_maxProfit = row
            # indexing year to increase
            increase_year = budgetDate[counterMax]
        counterMax =+ 1
    
        # calculating the greatest decrease in profits
        if row < decrease_maxProfit:
            decrease_maxProfit = row
            # indexing year to decrease
            decrease_year = budgetDate[counterMin]
        counterMin =+ 1
            
    # printing analysis to terminal
    print ("-------------------------------------------------")
    print ("Financial Analysis")
    print ("-------------------------------------------------")
    print (f"Total Months: {monthsTotal}")
    print (f"Total: ${p_lTotal}")
    print (f"Average Change: ${round(avgChange,2)}")
    print (f"Greatest Increase in Profits: {increase_year} ${increase_maxProfit}")
    print (f"Greatest Decrease in Profits: {decrease_year} ${decrease_maxProfit}")
