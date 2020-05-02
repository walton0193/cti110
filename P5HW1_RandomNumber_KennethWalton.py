def mainMenu():
    print("MAIN MENU")
    print("1. Play Game")
    print("2. Exit")

selection = int(input("Enter your choice"))
return int(selection)


while True:
    selection = menu()
    if selection == "1":

        import random
        start_over = True

        print("Number Game")

        while start_over:
            number = random.randint(1, 100)

            guess = int(input("Enter your guess"))
            counter = 1

        while guess !=number and guess != -1:
            if guess > number:
                print("That number is too high")
        else:
            print("That number is too low")
            guess = int(input("Enter your guess:"))
            counter += 1

        if guess != -1:
            print("That is the correct number! It took", counter, "guesses")
        else:
            start_over = False

if selection == "2":
    exit

else:
    print("Error: Please enter a choice from the menu")
    
    
