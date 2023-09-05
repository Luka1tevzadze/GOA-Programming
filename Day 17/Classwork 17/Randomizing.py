import random 
# crew_leaders = ['kruashvili', 'amiranashvili', 'tyeshelashvili', 'janezashvili', 'molodini', 'kereselidze', 'kurtanidze']

# print(crew_leaders[4])
# print(crew_leaders[random.randint(0,6)]) 
# print(crew_leaders[random.randint(0,6)])
# for i in range(1,4):
#     print('winner N',i,'is',random.choice(crew_leaders))

crew_leaders = ['kruashvili', 'amiranashvili', 'tyeshelashvili', 'janezashvili', 'molodini', 'kereselidze', 'kurtanidze','aruda']
winners = []
while len(winners) < 3:
    winner = random.choice(crew_leaders)
    if winner not in winners:
        winners.append(winner)
        print(winner)

crew_leaders.remove('aruda')
print(crew_leaders)

