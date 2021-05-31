# This programs belongs to Mr. Stupidity x 100

import keyword
from typing_extensions import ParamSpecKwargs
from datetime import date

def addContact():
    contact = input("Enter the mobile number: ")
    ContactName = input("Enter the contact name: ")
    ContactsFileCreationOrWriting = open("contacts.txt", "a")
    FileContent = ContactsFileCreationOrWriting.write(f"\n{date.today()} | {contact} | {ContactName}\n")


def deleteContact():
    pass

def listAllContact():
    pass

def SourceCode():
    pass

def GithubRedirection():
    pass



if __name__ == '__main__':
    print("\n\n***************Contact Manager at your service sir/madam!!!!***************\n\n")

    Instructions = "To view all contacts hit 'A' on your keyboard\n\nTo add a new contact hit 'T' on your keyboard\n\nTo delete a contact hit 'D' on the keyboard\n\n(For Devs)Type 'src' to get the source code the program.\n\nTo be the redirected to the Github repo type 'gh redir'.\n\n"

    print(Instructions)

    UserInput = input("Enter here: ")
    MainInput = UserInput.lower()


    if MainInput == "a":
        listAllContact()

    elif MainInput == "t":
        addContact()

    elif MainInput == "d":
        deleteContact()

    elif MainInput == "src":
        SourceCode()

    elif MainInput == "gh redir":
        GithubRedirection()