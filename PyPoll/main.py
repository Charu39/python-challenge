# Import necessary modules
import os
import csv

# Path to collect data from the Resources folder
election_data = os.path.join("Resources", "election_data.csv")

# Initialize variables
total_votes = 0

# Dictionary to store candidates and their vote counts
candidates = {}

# List to store vote percentages
percent_votes = {}

# Open and read CSV file
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    csv_header = next(csvreader)

    # Iterate through rows in CSV file
    for row in csvreader:
        # Extract data from current row
        candidate = row[2]

        # Count total votes
        total_votes += 1

        # Update candidate votes in the dictionary
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

    # Calculate vote percentages
    for candidate, votes in candidates.items():
        percent_votes[candidate] = (votes / total_votes) * 100
        percent_votes[candidate] = round(percent_votes[candidate], 2)

    # Find the winner based on popular vote
    winner = max(candidates, key=candidates.get)

# Print Analysis to terminal
print("Election Results")
print("----------------------------")
print(f"Total Votes: {str(total_votes)}")
print("----------------------------")
for candidate, votes in candidates.items():
    print(f"{candidate}: {percent_votes[candidate]}% ({votes})")
print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")

# Export results to a text file
output = open("output.txt", "w")
line1 = "Election Results"
line2 = "----------------------------"
line3 = f"Total Votes: {str(total_votes)}"
line4 = "----------------------------"
output.write(f"{line1}\n{line2}\n{line3}\n{line4}")
for candidate, votes in candidates.items():
    line = f"{candidate}: {percent_votes[candidate]}% ({votes})"
    output.write(f"\n{line}")
line5 = "----------------------------"
line6 = f"Winner: {winner}"
line7 = "----------------------------"
output.write(f"\n{line5}\n{line6}\n{line7}")
output.close()
