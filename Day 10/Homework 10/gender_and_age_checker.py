print("Valid answers are man and woman and non binary")

print("--------------------------------------------------")

gender_check = input("What Gender are you? : ")
age_check = int(input("How old are you? : "))


if age_check >= 65 and gender_check == "man":
    print("Pensia Gekutvnit")
else:
    if age_check >= 60 and gender_check == "woman":
        print("Tqven Pensia Gekutvnit")
if gender_check == "non binary":
    print("Get out of here!! you bitch bitch")
