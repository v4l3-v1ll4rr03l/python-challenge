#imports
import csv

#specify file
f = open("PyBank/Resources/budget_data.csv", "r")

#read file
f_read = f.readlines()

#create variables to track and store relevant values
header = ''

tot_months = 0
net_tot = 0

curr_change = 0

max_inc_date = ""
max_inc = 0

max_dec_date = ""
max_dec = 0

init_num = 0
prev_num = 0
num = 0

#read file line by line
for line in f_read:

    #store values individual line of code
    temp = line.split(",")

    #make relevant calculations for non-header rows
    if tot_months > 0:
        #change string to int for calculations
        num = int(str(temp[1].split("\n")[0]))

        net_tot += num

        #calculate changes accounting for signs of profit/loss
        curr_change = num - prev_num

        #update variables used to track max increases and decreases
        if curr_change > max_inc:
            max_inc_date = temp[0]
            max_inc = curr_change
        if curr_change < max_dec:
            max_dec_date = temp[0]
            max_dec = curr_change
        if tot_months == 1:
            init_num = num
    else:
        header = line
    
    #store previous profit/loss
    prev_num = num

    #increment number of months
    tot_months += 1

#calculate average change
avg_change = int(((prev_num - init_num) / (tot_months - 2)) * 100)
avg_change = avg_change / 100

#open file to write results
f = open("PyBank/analysis.txt", "w")

#write results
f.write("\nFinancial Analysis\n----------------------------")
f.write("\nTotal Months: " + str(tot_months - 1))
f.write("\nTotal: $" + str(net_tot))
f.write("\nAverage Change: $" + str(avg_change))
f.write("\nGreatest Increase in Profits: " + max_inc_date + " ($" + str(max_inc) + ")")
f.write("\nGreatest Decrease in Profits: " + max_dec_date + " ($" + str(max_dec) + ")")

f.close()
