import os
import csv

# Path to collect data from the Resources folder
budget_data = os.path.join("Resources", "budget_data.csv")

# Initialize variables
total_months = 0
net_total = 0
previous_profit_loss = 0
changes = []
greatest_increase = {"date": "", "profits": 0}
greatest_decrease = {"date": "", "profits": 0}

# Open and read CSV file
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    csv_header = next(csvreader)

    # Iterate through rows in CSV file
    for row in csvreader:
        # Extract data from current row
        date = row[0]
        profit_loss = int(row[1])

        # Calculate total number of months and net total
        total_months += 1
        net_total += profit_loss

        # Calculate the change in profit/loss and update the greatest increase and decrease
        if total_months > 1:
            change = profit_loss - previous_profit_loss
            changes.append(change)

            if change > greatest_increase["profits"]:
                greatest_increase.update({"date": date, "profits": change})

            if change < greatest_decrease["profits"]:
                greatest_decrease.update({"date": date, "profits": change})

        # Update previous profit and loss for the next iteration
        previous_profit_loss = profit_loss

# Calculate the average change
average_change = sum(changes) / len(changes)

# Print Analysis to terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['profits']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['profits']})")

# Export results to a text file
output = open("output.text","w")

line1 = ("Financial Analysis")
line2 = ("----------------------------")
line3 = str(f"Total Months:{total_months}")
line4 = str(f"Total: ${net_total}")
line5 = str(f"Average Change: ${average_change:.2f}")
line6 = str(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['profits']})")
line7 = str(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['profits']})")
output.write(f"{line1}\n{line2}\n{line3}\n{line4}\n{line5}\n{line6}\n{line7}")




