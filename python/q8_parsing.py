# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

def football_q8():
    import csv
    f = open("football.csv")
    csv_f=csv.reader(f)

    goals=[]
    for row in csv_f:
        goals.append(row[-3])
    goals.pop(0)
    goals=[int(i) for i in goals]

    f = open("football.csv")
    csv_f=csv.reader(f)

    goals_allowed=[]
    for row in csv_f:
        goals_allowed.append(row[-2])
    goals_allowed.pop(0)
    goals_allowed=[int(i) for i in goals_allowed]

    differences=[abs(x-y) for x,y in zip(goals, goals_allowed)]

    f = open("football.csv")
    csv_f = csv.reader(f)

    team = []
    for row in csv_f:
        team.append(row[0])
    team.pop(0)

    t = sorted(zip(differences, team))
    x=t[0]
    y=x[-1]
    print "The team with the smallest difference in 'for' and 'against' goals is %s." % y