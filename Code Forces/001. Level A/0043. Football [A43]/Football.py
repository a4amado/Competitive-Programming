number_of_goals = int(input())

goals = []

for i in range(number_of_goals):
    goals.append(input())

teams = {}

for idx, item in enumerate(goals):
    
    try:
        current_count = teams[item]
        teams[item] += 1
    except KeyError:
        teams[item] = 1


winner = ""
current = 0

for idx, item in enumerate(list(teams)):
    if (teams[item] > current):
        winner = item
        current = teams[item]

print(winner)