import os
import csv


votes = []
candidate_list = []
candidates = []

csvpath = os.path.join('', "election_data.csv")

with open(csvpath) as csvfile:
    reader=csv.reader(csvfile)

    for row in reader:
        votes.append(row[0])
        candidates.append(row[2])

    #remove header in votes list
    votes.pop(0)
    vote_count = len(votes)

    print("ELECTION RESULTS")
    print("    ")
    print("A Total of " + str(vote_count) + " votes were cast.")
    print("  ") 

    #remove header from Candidates list
    candidates.pop(0)

    #find unique values in "candidates" list
    candidate_set = set(candidates)
    candidate_list = list(candidate_set)

    print("The list of possible candidates are:" + str(candidate_list))
    print("-------------------------------")

    #for name in candidate_list:
     #   print(name)

    #create empty lists for each candidate
    khan = []
    otooley = []
    li = []
    correy = []
    #add each candidate to their own list each time they appear
    for each in candidates:
        if each == "Khan":
            khan.append(each)
        elif each == "O'Tooley":
            otooley.append(each)
        elif each == "Li":
            li.append(each)
        elif each == "Correy":
            correy.append(each)

    #find percentage of votes each candidate received
    correy_percent = len(correy)/vote_count
    otooley_percent = len(otooley)/vote_count
    li_percent = len(li)/vote_count
    khan_percent = len(khan)/vote_count
    

    print("Correy: " + str(len(correy)) + "    {:.2%}".format(correy_percent))
    print("O'Tooley: " + str(len(otooley)) + "    {:.2%}".format(otooley_percent))
    print("Li: " + str(len(li)) + "    {:.2%}".format(li_percent))
    print("Khan: " + str(len(khan)) + "    {:.2%}".format(khan_percent))

    print("WINNER:  Khan")

with open('analysis/election_analysis.txt', 'w') as f:
    f.write("ELECTION RESULTS" "\n")
    f.write("    " "\n")
    f.write("A Total of " + str(vote_count) + " votes were cast." "\n")
    f.write("  " "\n")
    f.write("The list of possible candidates are:" + str(candidate_list) )
    f.write( "\n" "-------------------------------" "\n")
    f.write("Correy: " + str(len(correy)) + "    {:.2%}".format(correy_percent))
    f.write("\n" "O'Tooley: " + str(len(otooley)) + "    {:.2%}".format(otooley_percent))
    f.write("\n" "Li: " + str(len(li)) + "    {:.2%}".format(li_percent))
    f.write("\n" "Khan: " + str(len(khan)) + "    {:.2%}".format(khan_percent))
    f.write( '\n' "WINNER:  Khan")
    