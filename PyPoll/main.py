from dataclasses import dataclass 
import csv

@dataclass
class Ballot:
    id: str
    county: str
    candidate: str

data = open("./election_data.csv")
data = list(csv.reader(data))
# print(data)



ballots = []

for x in data[1:]: 
    ballots.append(Ballot( x[0], x[1], x[2] ))

print(ballots[0:10])

totalvotes = len(ballots)
print(totalvotes)

votes_per_candidate = {}


for ballot in ballots:
        if ballot.candidate in votes_per_candidate:
            votes_per_candidate[ballot.candidate]= votes_per_candidate[ballot.candidate] +1
        else:
            votes_per_candidate[ballot.candidate] = 1
print(votes_per_candidate)


for candidate,votes in votes_per_candidate.items() :

    print(candidate, 100*(votes/totalvotes), votes)
    

winner = max(votes_per_candidate, key = lambda x : votes_per_candidate[x])
print(f"Winner: {winner}")

