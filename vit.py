while True:
    print("\n Personal Health Logger ")
    print("1. Add Health Entry")
    print("2. View All Entries")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        date = input("Enter today's date (DD/MM/YYYY): ")
        water = input("Enter water intake (liters): ")
        sleep = input("Enter sleep hours: ")
        exercise = input("Enter exercise minutes: ")
        mood = input("Enter your mood today: ")

        # Save the entry into a text file
        file = open("health_log.txt", "a")
        file.write("Date: " + date +
                   ", Water: " + water +
                   "L, Sleep: " + sleep +
                   "hrs, Exercise: " + exercise +
                   "mins, Mood: " + mood + "\n")
        file.close()

        print("Entry saved successfully!\n")

    elif choice == "2":
        print("\nSaved Health Entries \n")
        try:
            file = open("health_log.txt", "r")
            print(file.read())
            file.close()
        except:
            print("No entries found. Please add some first.")

    elif choice == "3":
        print("Thank you! Stay healthy ")
        break

    else:
        print("Invalid choice, please try again.")
