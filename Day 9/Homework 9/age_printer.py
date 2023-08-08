print("Please add 1 to your age because for example it will say this if u type like 12 it will start from 0 to 11")

ask_age = int(input("How old are you? : "))


age = int(ask_age)

for i in range(int(ask_age)):
    print("Congratulations, you turned " + str(i) + " years old")
    if i == 8:
        print("Congrats, for joining goa!")