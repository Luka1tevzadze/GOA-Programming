import random

crew_members = ["Andria Skhh","Dachi Sazandrishvili","Davit Meparishvili","Gio Gagnidze","Giorgi Gelashvili","Jemuka Kaxidze","Luka Kevkhishvili","Luka Tevzadze","Luka Turadze","Luka Turadze","Nikoloz Gogniashvili","Nikolozi Natchkebia","Soso Valishvili","Temo Maglakelidze","Luka Zazashvili"]

crew_1_members = [member for member in crew_members if member.endswith("i")]

# crew_member_choose = random.choice(crew_members)

choose = random.choice(crew_1_members)
choose1 = random.choice(crew_members)
choose2 = choose + " is cool"
choose3 = choose1 + " studies good"
choose4 = [choose2,choose3]

print(random.choice(choose4))