#!/usr/bin/env python3

try:
    # Using Python 3, create an input form, using the input(), asking the the user to enter their first name, middle inital and last name. Output the result as full name to the terminal. Use a variable to store the fullName and then use the print() with parameterization. Format the variable names using firstName, etc.

    # Ask the user for their first name
    firstName = input("What is your first name? ")

    # Ask the user for their middle initial
    middleInitial = input("What is your middle initial? ")

    # Ask the user for their last name
    lastName = input("What is your last name? ")

    # Create a variable to store the full name
    fullName = firstName + " " + middleInitial + ". " + lastName

    # Output the full name to the terminal
    print("Your full name is:", fullName) # parameterization

    # regex101.com
    # variable format: var_fname, var_lname, var_mi, var_address, var_city, var_state, var_zip, var_phone, var_email
    # column format: fname, lname, mi, address, city, state, zip, phone, email
    # formats.py
    # Using Python 3, create an input form, using the input(), asking the the user to enter their first name, middle inital, last name, address, city, state, zip code, phone number and email address. The email address is required. Test the pattern of the email address to make sure it is valid, using the re module. Then output the variables to columns in a csv file named "contacts.csv".

    # import the regular expression module
    import re

    # Ask the user for their first name
    firstName = input("What is your first name? ")

    # Ask the user for their middle initial
    middleInitial = input("What is your middle initial? ")

    # Ask the user for their last name
    lastName = input("What is your last name? ")

    # Ask the user for their address
    address = input("What is your address? ")

    # Ask the user for their city
    city = input("What is your city? ")

    # Ask the user for their state
    state = input("What is your state? ")

    # Ask the user for their zip code
    zipCode = input("What is your zip code? ")

    # Ask the user for their phone number
    phoneNumber = input("What is your phone number? ")

    # Ask the user for their email address
    emailAddress = input("What is your email address? ")

    # Test the pattern of the email address to make sure it is valid
    if re.match(r"[^@]+@[^@]+\.[^@]+", emailAddress):
        print("Valid email address")
    else:
        print("Invalid email address")

    # Output the variables to columns in a csv file named "contacts.csv"
    # open the file in append mode
    with open("contacts.csv", "a") as file:
        # write the variables to the file
        file.write(firstName + "," + middleInitial + "," + lastName + "," + address + "," + city + "," + state + "," + zipCode + "," + phoneNumber + "," + emailAddress + "\n")
finally:
    print("Done.")