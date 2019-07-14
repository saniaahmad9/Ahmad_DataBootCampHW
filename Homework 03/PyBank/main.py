import csv

budget_data = "/Users/saniaahmad/Desktop/Ahmad_DataBootCampHW/Homework03/PyBank/budget_data.csv"

total_months = 0
prev_net = 0
month = []
profit_loss_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]
total_profit_loss = 0

with open(budget_data, newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(reader)
    print(f"Header: {csv_header}")
    
    for row in reader:
            total_months = total_months + 1
            total_profit_loss = total_profit_loss + int(row[1])
            
            profit_loss = int(row[1]) - prev_net
            prev_net = int(row[1])
            profit_loss_list = profit_loss_list + [profit_loss]
            month = month + [row[0]]
            
            if (profit_loss > greatest_increase[1]):
                greatest_increase[0] = row[0]
                greatest_increase[1] = profit_loss
                
            
            if (profit_loss < greatest_decrease[1]):
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = profit_loss
            
                
net_average = sum(profit_loss_list) / len(profit_loss_list)

print(profit_loss)

print("Financial Analysis")
print("-------------------------")
print("Total Months: " + str(total_months))
print("Total Profit/Loss: " + "$" + str(total_profit_loss))
print("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 
print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")
print("Average: $" + str(net_average))
