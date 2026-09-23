
print("Komennot:\nJatka\nOhje\nLopeta\nSeis")

user_command = input("Anna komento: ").lower()

while user_command != "lopeta":
    if user_command == "jatka":
        print("Jatketaan seuraavaan looppiin!")

    elif user_command == "ohje":
        print("Komennot:\nJatka\nOhje\nLopeta\nSeis")

    elif user_command == "seis":
        print("Abort mission!")
        break

    user_command = input("Anna uusi komento: ").lower()

print("End")



