# Add our dependencies
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Initialize total vote counter
total_votes = 0
#Candidates
candidate_options = []
candidate_votes = {}
#Counties
county_list = []
county_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Largest county and county voter tunrnout
county_turnout = ""
county_winner = 0
c_winning_percentage = 0

# Open the elections results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    #Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Print the candidate name from each row
        candidate_name = row[2]
        #Extract county name
        county_name = row[1]
        # If the candidate does not match any existing candidate add to list.
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
        # If the county does not match any existing county add to list.
        if county_name not in county_list:
            #Add it to the list of counties:
            county_list.append(county_name)
            #Begin tracking county voting count.
            county_votes[county_name] = 0
        #Add a vote to that county'a count.
        county_votes[county_name] += 1
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f'County Votes:\n')
    
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Retrieving from county dictionary, iterate through the county list.
    for county_name in county_list:
        #Retrieve the vote for each county.
        c_votes = county_votes[county_name]
        #Calculate the percentagef of votes per county. 
        c_vote_percentage = float(c_votes) / float(total_votes) * 100
         #Print each county, their voter count, and percentage to the terminal.
        county_results = (f"{county_name}: {c_vote_percentage:.1f}% ({c_votes:,})\n")
        # Print county with their voter count, and percentage to the terminal.
        print(county_results)
        #  Save the candidate results to our text file.
        txt_file.write(county_results)
        #Determine winning county
        if (c_votes > county_winner) and (c_vote_percentage > c_winning_percentage):
            c_winning_count = c_votes
            c_winning_percentage = c_vote_percentage
            c_winning_county = county_name
    
    #Determine county with largest turnout
    winning_county_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {c_winning_county}\n"
        f"-------------------------\n")
    
    print(winning_county_summary)
    # Save the winning county's name to the text file.
    txt_file.write(winning_county_summary) 
           
    # Determine the percentage of votes for each candidate by looping through the counts.
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage =  float(votes) / float(total_votes) * 100
        # Print out the winning candidate, vote count and percentage to terminal.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")   
        # Print candidates with their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
        
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    
    print(winning_candidate_summary)
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)