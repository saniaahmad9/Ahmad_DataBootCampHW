import csv

budget_data = "/Users/saniaahmad/Desktop/Ahmad_DataBootCampHW/Homework03/PyBank/budget_data.csv"

total_months = 0
prev_revenue = 0
month_of_change = []
revenue_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 1000000000000000000]
total_revenue = 0

with open(budget_data, newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(reader)
    print(f"Header: {csv_header}")
    
    for row in reader:
            total_months = total_months + 1
            total_revenue = total_revenue + int(row[1])
            
            revenue_change = int(row[1]) - prev_revenue
            prev_revenue = int(row[1])
            revenue_change_list = revenue_change_list + [revenue_change]
            month_of_change = month_of_change + [row[0]]
            
            if (revenue_change > greatest_increase[1]):
                greatest_increase[0] = row[0]
                greatest_increase[1] = revenue_change
                
            
            if (revenue_change < greatest_decrease[1]):
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = revenue_change
            
                
revenue_avg = sum(revenue_change_list) / len(revenue_change_list)

print(revenue_change)

print("Financial Analysis")
print("-------------------------")
print("Total Months: " + str(total_months))
print("Total Revenue: " + "$" + str(total_revenue))
print("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 
print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")
    

