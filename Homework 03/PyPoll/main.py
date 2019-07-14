import csv

poll_data = "/Users/saniaahmad/Desktop/GWARL201906DATA1/02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv"

votes = 0
winner_votes = 0
candidates = 0
candidate_choice = []
candidate_votes = {}


with open(poll_data) as poll_data:
    reader = csv.DictReader(poll_data)

    for row in reader:
        votes = votes + 1
        candidates = row["Candidate"]        

        if row["Candidate"] not in candidate_choice:
            
            candidate_choice.append(row["Candidate"])

            candidate_votes[row["Candidate"]] = 1
            
        else:
            candidate_votes[row["Candidate"]] = candidate_votes[row["Candidate"]] + 1


print("Election Results")
print("-------------------------")
print("Total Votes: " + str(votes))
print("-------------------------")

for c in candidate_votes:
        print(c + " " + str(round(((candidate_votes[c]/votes)*100))) 
        + "%" + " (" + str(candidate_votes[c]) + ")") 
        candidate_results = (c + " " + str(round(((candidate_votes[c]/votes)*100))) 
        + "%" + " (" + str(candidate_votes[c]) + ")")

print("Winner: Khan")
