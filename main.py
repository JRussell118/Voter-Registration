"""This program asks the user for their name, age, and location info to register them to vote"""
def main():
    """Defines the code of the program in main"""
    print("Welcome to the Voter Registration Application Program.")

    # Asks the user if they would like to vote
    shutdown = input("Would you like to register to vote? (y/n)")

    # If shutdown is equal to n, prints a closing message and ends the program
    if shutdown == 'n':
        print("Closing the program. Goodbye.")
        return
    # inputs the user's first name
    f_name = input("What is your first name?")
    # inputs the user's last name
    l_name = input("What is your last name?")

    # If shutdown is equal to n, prints a closing message and ends the program
    shutdown = input("Do you want to continue your registration? (y/n)")
    if shutdown == 'n':
        print("Closing the program. Goodbye.")
        return

    # inputs the user's age
    age = int(input("How old are you?"))
    # Checks if the user's age is valid, and re-prompts if not
    while age > 120:
        age = int(input("The age you entered is invalid, please reenter."))

    # If shutdown is equal to n, prints a closing message and ends the program
    shutdown = input("Do you want to continue your registration? (y/n)")
    if shutdown == 'n':
        print("Closing the program. Goodbye.")
        return
    # inputs the user's citizenship
    citizen = input("Are you a citizen of the U.S.? (y/n)")

    # If shutdown is equal to n, prints a closing message and ends the program
    shutdown = input("Do you want to continue your registration? (y/n)")
    if shutdown == 'n':
        print("Closing the program. Goodbye.")
        return
    # inputs the user's state
    state = input("What state do you live in?")

    # Checks the length of the state, and re-prompts if it's not 2 letters
    while len(state) > 2:
        state = input("Please enter the two letter abbreviation of your state.")

    # If shutdown is equal to n, prints a closing message and ends the program
    shutdown = input("Do you want to continue your registration? (y/n)")
    if shutdown == 'n':
        print("Closing the program. Goodbye.")
        return
    # inputs the users zipcode
    zipcode = int(input("What is your area's zipcode?"))

    # Prints all of the user's input information
    print("Here is your registration information:")
    print(f"Name: {f_name} {l_name}\nAge: {age}")
    print(f"U.S. Citizen: {citizen}\nState: {state}\nZipcode: {zipcode}")

    # Checks if the age or citizenship is invalid for registration
    if age < 18 or citizen == 'n':

        # Prints a message based on which variable was invalid
        if age < 18:
            print("Based on your information, you are not the appropriate age to register.")
        if citizen == 'n':
            print("Based on your information, you are not a U.S. citizen and cannot register.")

    # else, prints a confirmation message
    else:
        print("You are now registered and eligible to vote.")


main()
