# ## PyBank

# ![Revenue](Images/revenue-per-lead.jpg)

# * In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

# * Your task is to create a Python script that analyzes the records to calculate each of the following:

import os
import csv

csvpath = os.path.join("..","PyBank","budget_data.csv")


with open(csvpath, newline="") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)


    mylist = list(csvreader)
   
    month_count = 0
    net_profit = 0
    this_month_revenue = 0
    last_month_revenue = 0
    revenue_change = 0
    revenue_changes = []
    months = []


# Read each row of data after the header
for row in mylist:
        #print(row)
        #print(len(row(0)))
        #print(row[1])

        month_count = month_count + 1
        months.append(row[0])
        this_month_revenue = int(row[1])
        net_profit = net_profit + this_month_revenue
        if month_count > 1:
            revenue_change = this_month_revenue - last_month_revenue
            revenue_changes.append(revenue_change)
        last_month_revenue = this_month_revenue
    



# analyze the month by month results
sum_rev_changes = sum(revenue_changes)
average_change = sum_rev_changes / (month_count - 1)
max_change = max(revenue_changes)
min_change = min(revenue_changes)
max_month_index = revenue_changes.index(max_change)
min_month_index = revenue_changes.index(min_change)
max_month = months[max_month_index]
min_month = months[min_month_index]

print(f"Total Months: {month_count}")
print(f"Total Revenue: ${net_profit}")
print(f"Average Revenue Change: ${average_change}")
print(f"Greatest Increase in Revenue: {max_month} (${max_change})")
print(f"Greatest Decrease in Revenue: {min_month} (${min_change})")

    