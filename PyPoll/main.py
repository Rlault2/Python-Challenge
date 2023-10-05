import os
import csv
# Define the file path
election_csv = os.path.join("Resources","election_data.csv")

# Initialize variables to store data
total_votes = 0
candidates = {}
winner = ""
max_votes = 0

# Open and read the CSV file
with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)  # Store the header

    # Loop through each row in the file
    for row in csvreader:
        voter_id, county, candidate = row

        # Count total votes
        total_votes += 1

        # Track candidates and their votes
        candidates[candidate] = candidates.get(candidate, 0) + 1

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Find the percenatge of votes each candidate received
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

    # Figure out who won
    if votes > max_votes:
        max_votes = votes
        winner = candidate

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Save the results to a text file
with open("election_results.txt", "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        txtfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")
