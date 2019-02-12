import csv
import os

#setting the file path
fname = os.path.join("budget_data.csv")

with open(fname, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=',')
    
    #setting up descriptive var_names
    total_months = 0
    net_total = 0
    diff = 0
    prof_loss = []
    date_list = []
    avg_chg = []
    
    for i in csvreader:
        total_months += 1
        net_total +=int(i["Profit/Losses"])
        prof_loss.append(int(i["Profit/Losses"]))
        date_list.append(i["Date"])
     
    #will loop through the profit_loss list items to get the difference   
    #and will create a new list of the diff of second num - first num
    i = 1
    while i < len(prof_loss):
        diff = prof_loss[i] - prof_loss[i-1]
        avg_chg.append(diff)
        i +=1
    
    total_avg_chg = sum(avg_chg)/ len(avg_chg)
    greatest_inc = max(avg_chg)
    greatest_dec = min(avg_chg)
    
    #merged the avg_chg list to the date list, however starting at index 1
    #for date_list, because the first value of avg_chg was dropped
    merge = zip(date_list[1:], avg_chg)
    
    for i in merge:
        if i[1] == greatest_inc:
            inc_date = i[0]
        if i[1] == greatest_dec:
            dec_date = i[0]
            
    print(f"Financail Analysis")
    print("-------------------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${round(total_avg_chg,2)}")
    print(f"Greatest Increase in Profits: {inc_date}, (${greatest_inc})")
    print(f"Greatest Decrease in Profits: {dec_date}, (${greatest_dec})")
    
with open('financial_analysis.txt', 'w') as wf:
    
    wf.write(f"Financail Analysis\n")
    wf.write("-----------------------------------------------------------\n")
    wf.write(f"Total Months: {total_months}\n")
    wf.write(f"Total: ${net_total}\n")
    wf.write(f"Average Change: ${round(total_avg_chg,2)}\n")
    wf.write(f"Greatest Increase in Profits: {inc_date}, (${greatest_inc})\n")
    wf.write(f"Greatest Decrease in Profits: {dec_date}, (${greatest_dec})\n")
    
    