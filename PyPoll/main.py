#PyPoll
# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip headers
    next(csvreader)

    total_vote = 0
    khan_vote = 0
    correy_vote = 0
    li_vote = 0
    otooley_vote = 0

    for row in csvreader:
        total_vote += 1

        if row[2] == 'Khan':
            khan_vote += 1
        if row[2] == 'Correy':
            correy_vote += 1
        if row[2] == 'Li':
            li_vote += 1
        if row[2] == 'O\'Tooley':
            otooley_vote += 1
    
    khan_pct = "{:.2%}".format(khan_vote / total_vote)
    correy_pct = "{:.2%}".format(correy_vote / total_vote)
    li_pct = "{:.2%}".format(li_vote / total_vote)
    otooley_pct = "{:.2%}".format(otooley_vote / total_vote)

    if khan_pct > correy_pct and khan_pct > li_pct and khan_pct > otooley_pct:
        winner = 'Khan'
    if correy_pct > khan_pct and correy_pct > li_pct and correy_pct > otooley_pct:
        winner = 'Correy'
    if li_pct > khan_pct and li_pct > correy_pct and li_pct > otooley_pct:
        winner = 'Li'
    if otooley_pct > khan_pct and otooley_pct > correy_pct and otooley_pct > li_pct:
        winner = 'O\'Tooley'

    output_data = (
        f'Election Results\n'
        f'----------------------------\n'
        f'Total Votes: {total_vote}\n'
        f'----------------------------\n'
        f'Khan: {khan_pct} ({khan_vote})\n'
        f'Correy: {correy_pct} ({correy_vote})\n'
        f'Li: {li_pct} ({li_vote})\n'
        f'O\'Tooley: {otooley_pct} ({otooley_vote})\n'
        f'----------------------------\n'   
        f'Winner: {winner}')

    print(output_data)

    #creates file for analysis
    with open("analysis/analysis.txt","w") as analysis_file:

        #this is writing the lines to the file
        analysis_file.write(output_data)