import csv
import os

date=[]
profit=[]
change=[]

print("Financial Analysis")
print("------------------------------------------")

csvpath = os.path.join("budget_data.csv")

with open(csvpath) as csvfile:
    reader=csv.reader(csvfile)

    for row in reader:
        date.append(row[0])
        profit.append(row[1])

#remove header from dates list
date.pop(0)

# Count number of dates
months=(len(date))
print("Total Months: " + str(months))

#remove header from profit list
profit.pop(0) 

#convert strings to integers in profit list
for i in range(0, len(profit)):
    profit[i] = int(profit[i])

total_profit = sum(profit)

print("Total Profit: $" + str(total_profit))

#create a list of each change from the profit list. new list is called "change"
for i in range(1, len(profit)):
    c = (profit[i] - profit[i-1])
    
    change.append(c)

#print(change)

add_sum = 0
#find the sum of all the changes in profit/loss
for i in range(0, len(change)):
    add_sum = add_sum + change[i]

#print("Sum of profit/loss changes: " + str(add_sum)) 

average_change = (add_sum/len(change))

print("Average Change is: $" + str(average_change))

#find max change value and corresponding date

max_change = max(change)

for i in range(0, len(change)):
    if change[i] == max_change:
        max_date = date[i + 1]
# max_date = date + 1 because there was no change the first recorded month.  Therefore the change list is short 1 length and corresponds to the month in the next row

print("The largest gain in profit was: $" + str(max_change) + " in " + str(max_date))

# find the biggest loss and corresponding date

max_loss = min(change)

for i in range(0, len(change)):
    if change[i] == max_loss:
        min_date = date[i + 1]

print("The biggest loss was: $" + str(max_loss) + " in " + str(min_date))

with open('analysis/financial_analysis.txt', 'w') as f:
    f.write("Financial Analysis")
    f.write("\n" "------------------------------------------")
    f.write("\n" "Total Months: " + str(months))
    f.write("\n" "Total Profit: $" + str(total_profit))
    f.write("\n" "Average Change is: $" + str(average_change))
    f.write("\n" "The largest gain in profit was: $" + str(max_change) + " in " + str(max_date))
    f.write("\n" "The biggest loss was: $" + str(max_loss) + " in " + str(min_date))