# This programs belongs to Mr. Stupidity x 100

import keyword
from typing import MutableSequence
from typing_extensions import ParamSpecKwargs
from datetime import date
import string
from colored import fg, bg, attr


def addContact():
    try:
        contact = input("Enter the mobile number: ")
        ContactName = input("Enter the contact name: ")
        ContactsFileCreationOrWriting = open("contacts.txt", "a")
        confirmation = input(f"Contact Name: {ContactName}\nContact Number: {contact}\nConfirm credentials? [Y/N]: ")
        EndConfirmation = confirmation.lower()
        for i in string.ascii_lowercase:
            if i in contact:
                print("Invalid Number. Contains alphabets")
            elif i not in contact:
                if EndConfirmation == "y":
                    FileContent = ContactsFileCreationOrWriting.write(f"\n{date.today()} | {contact} | {ContactName}\n")
                elif EndConfirmation == "n":
                    addContact()
                else:
                    print("Failed loading script main")
            else:
                print("Failed loading script main")
    except Exception as e:
        print(e)


def deleteContact():
    pass

def listAllContact():
    file = open("contacts.txt", "r")
    FileContent = file.read()
    print(FileContent)

def SourceCode():
    pass

def GithubRedirection():
    pass



if __name__ == '__main__':
    print("\n\n***************Contact Manager at your service sir/madam!!!!***************\n\n")

    Instructions = "To view all contacts hit 'A' on your keyboard\n\nTo add a new contact hit 'T' on your keyboard\n\nTo delete a contact hit 'D' on the keyboard\n\n(For Devs)Type 'src' to get the source code the program.\n\nTo be the redirected to the Github repo type 'gh redir'.\n\n"

    print(Instructions)
    while True:
        UserInput = input(f"{fg('chartreuse_2a')}Enter here: {attr('reset')}")
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
        
        elif MainInput == "exit":
            exit()
        elif MainInput == "quit":
            exit()