# Psuedocoding

# 1. Import the data
# 2. Loop thru each vote to do the following:
#       a. Increment the total number of votes
#       b. Check if csndidate is in list of candidates
#           if yes: do nothing
#           if no: add candidate to list
#       c. Increment the votes for the candidate
# 3. Calculate the percentage of votes for each candidate
# 4. Print the following deliverables:
#       a. Total number of votes cast
#       b. Complete list of all candidates who received votes
#       c. Total number of votes for each candidate
#       d. Percentage of the total vote each candidate received

import csv
import os
import time

# Assign a variable to load a file from a path
file_to_load = os.path.join("election_analysis", "resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("election_analysis","analysis", "election_analysis.txt")

# Open the election results and read the file
start_time = time.time()

# Declare variables outside loops & before opening files
total_votes = 0
candidate_votes = {}
vote_percentages = {}

with open(file_to_load) as election_data:
    # file_reader = csv.reader(election_data)
    # for row in file_reader:
    #     print(row)

    # Print the header row
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)

    # Perform analysis
    # Get total votes
    # Starts at row 2 since first row is read above while getting headers
    for row in file_reader:
        total_votes += 1

        # Check if candidate is already on list
        # Add candidate to dictionary and set number of votes to 1 if not already in dict
        if row[2] not in candidate_votes.keys():
            candidate_votes[row[2]] = 1
        # Increment candidate's votes by 1 if already in dictionary
        else:
            candidate_votes[row[2]] += 1

    # Calculate percentage of votes each candidate received
    for candidate in candidate_votes.keys():
        vote_percentages[candidate] = f"{float(100*candidate_votes[candidate] / total_votes):.1f}%"

winning_candidate = ""
winning_votes = 0
for candidate in candidate_votes:
    if candidate_votes[candidate] >= winning_votes:
        winning_votes = candidate_votes[candidate]
        winning_candidate = candidate

with open(file_to_save, 'w') as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total votes: {total_votes}\n"
        f"-------------------------\n"
    )

    txt_file.write(election_results)

    for candidate in candidate_votes:
        candidate_results = f"{candidate}: {candidate_votes[candidate]} ({vote_percentages[candidate]})"
        txt_file.write(f"{candidate_results}\n")

    txt_file.write(f"-------------------------\n")

    winner = (
        f"Winning candidate: {winning_candidate}\n"
        f"Winning votes: {candidate_votes[winning_candidate]}\n"
        f"Winning percentage: {vote_percentages[winning_candidate]}\n"
        f"-------------------------\n"
    )

    txt_file.write(winner)


print(f"Total votes:                {total_votes}\n\n")
for candidate in candidate_votes:
    print(
        f"{candidate}: {candidate_votes[candidate]} votes ({vote_percentages[candidate]})\n")
print(
    f"{winning_candidate} won the election with {vote_percentages[winning_candidate]} ({candidate_votes[winning_candidate]} votes) of the total vote ({total_votes} votes).\n")

end_time = time.time()
print(f"Runtime:                    {end_time - start_time:.2f} seconds")
