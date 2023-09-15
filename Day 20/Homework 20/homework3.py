Crew_Members = ["Gio Gagnidze","Kevkishvili","Jemiko Qiqava","Luka Turadze","Luka Zazashvili","Davit Meparishvili","Luka Tevzadze","alexandre katsarava"]

cool_list = []


for i in Crew_Members:
    if len(i) >= 16:
        cool_list.append(i)
print(cool_list)