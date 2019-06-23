# Ultimo intento mio .... Pypoll... 22June2019

#import libraries OS and CSV to use
import os
import csv

# path of data without folder.
csvpath = os.path.join('election_data.csv')
# fields are Voter ID, County, and Candidate

#Inicialize  var to acumulate votes 
acum_votes = 0
#Create an structure to put aggregated data x candidate
#also create the list to put uni1ue candidates & cum.votes collected
# join all data to create the output
summary_res= {} 
who = [] # unique candidates
votes_who = []  # put sum votes
percent_who = []  # put % 
who_win = []
name = [] 

#open data to iterate a get variables
with open(csvpath, 'r') as csvfile:
    csvread = csv.reader(csvfile)
    next(csvread) #skipping the first row
    #iterate the file to sum and identify candidates
    for row in csvread:
        acum_votes += 1 
        if row[2] in summary_res.keys():
            summary_res[row[2]] = summary_res[row[2]] + 1  #candidates 
        else:
            summary_res[row[2]] = 1
            
            
#acum_votes

# candidates and number of votes with order in dic
who = [] # unique candidates
votes_who = []  # put sum votes

for key, value in summary_res.items():
    who.append(key)
    votes_who.append(value)

#who,votes_who   gives (['Khan', 'Correy', 'Li', "O'Tooley"], [2218231, 704200, 492940, 105630])

# Calcualte % of votes per candidate and put in its list
percent_who = []
for n in votes_who:
    percent_who.append(round(n/acum_votes*100, 1))

#percent_who gives [63.0, 20.0, 14.0, 3.0]

# join the three list in one
new_file = list(zip(who, votes_who, percent_who))
#new_file  gives ('Khan', 2218231, 63.0),
# ('Correy', 704200, 20.0),
# ('Li', 492940, 14.0),
# ("O'Tooley", 105630, 3.0)]

#find winner through number of votes
who_win = []
for name in new_file:
    if max(votes_who) == name[1]:
        who_win.append(name[0])

#who_win equals ['Khan']

win = who_win[0]
#win gives 'Khan'

#create file to store results
Results = os.path.join('Winner_Poll.txt')

#write final results
with open(Results, 'w') as txtfile:
    txtfile.writelines('Total Votes =' + str(acum_votes)+ ')\n')
    for res in new_file:
        txtfile.writelines(res[0] + ": " + str(res[2]) +'% votes are (' + str(res[1]) + ')\n')
    txtfile.writelines('The Winner is : ' + win )

with open(Results, 'r') as readfile:
    print(readfile.read())
# THE END