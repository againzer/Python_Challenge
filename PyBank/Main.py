# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

from statistics import mean

csvpath = os.path.join('Resources', 'budget_data.csv')

# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    #csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    #for row in csvreader:
        #print(row)

    #skip headers
    next(csvreader)

    rowfirst = next(csvreader)

    #set up initial variables
    total = 0
    count_rows = 0
    prev_total = int(rowfirst[1])
    net_amounts_list = []
    greatest_inc_amount = 0
    greatest_dec_amount = 0



    #start for loop
    for row in csvreader:
        count_rows += 1 #counting total rows for total month output
        total += int(row[1]) #Adding up all the values in column 2
        net_amount = int(row[1]) - prev_total #calculating the net change
        prev_total = int(row[1]) #setting previous total to current row before moving to next iteration
        net_amounts_list += [net_amount] #adding the next item in list
        if net_amount > greatest_inc_amount: #comparing net amount and storing month / amount if true
            greatest_inc_month = row[0]
            greatest_inc_amount = net_amount
        if net_amount < greatest_dec_amount: #comparing net amount and storing month / amount if true
            greatest_dec_month = row[0]
            greatest_dec_amount = net_amount
    

    
    #how do you exclude the first record its pulling my net change higher
    avg_change = sum(net_amounts_list)/len(net_amounts_list)



    output_data = (
        f'Total Months: {count_rows}\n'
        f'Total: {total}\n'
        f'Average Change: {avg_change}\n'
        f'Greatest Increase in Profits: {greatest_inc_month} ({greatest_inc_amount})\n'
        f'Greatest Decrease in Profits: {greatest_dec_month} ({greatest_dec_amount})\n'
        )

    print(output_data)

    #creates file for analysis
    with open("analysis/analysis.txt", "w" ) as analysis_file:
        #this is writing the lines again in terminal and then [none,none,none] in the file
        analysis_file.write(output_data)
        
    
