import os
import csv
# Define the file path
budget_csv = os.path.join("Resources","budget_data.csv")

# Initialize variables to store the data needed
total_months = 0
net_total = 0
previous_profit_loss = 0
total_change = 0
max_profit = float("-inf")
max_loss = float("inf")
max_profit_date = ""
max_loss_date = ""

# Open and read the CSV file
with open(budget_csv, 'r') as csvfile:
    # Split the data on commas and store the header
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    # Track Profit Loss and its change
    previous_profit_loss = None
    total_change = 0
    
    # Loop through each row in the file
    for row in csvreader:
        date, profit_loss = row
        
        # Convert Profit/Loss to an integer
        profit_loss = int(profit_loss)
        
        # Count total months
        total_months += 1
        
        # Calculate net total
        net_total += profit_loss
        
        # Calculate change from the previous month (skip on the first month)
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            total_change += change
            
            # Find the greatest increase in profits and its date
            if change > max_profit:
                max_profit = change
                max_profit_date = date
            
            # Find the greatest decrease in profits and its date
            if change < max_loss:
                max_loss = change
                max_loss_date = date
        
        # Set the current profit/loss as the previous for the next iteration
        previous_profit_loss = profit_loss

# Calculate the average change (skip if there is only one month)
if total_months > 1:
    average_change = total_change / (total_months - 1)

# Print the results 
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Net Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {max_profit_date} (${max_profit})")
print(f"Greatest Decrease in Profits: {max_loss_date} (${max_loss})")

# Export the results to a text file
analysis = os.path.join("..", "PyBank", "analysis.txt")
with open(analysis, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Net Total: ${net_total}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {max_profit_date} (${max_profit})\n")
    txtfile.write(f"Greatest Decrease in Profits: {max_loss_date} (${max_loss})\n")

