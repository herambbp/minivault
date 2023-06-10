import os
import time
import datetime
import pdf
import pyttsx3
from pwinput import *
import json
import encrypt
import jarvis
import re
welcomest = "Welcome to MiniVault App"
engine = pyttsx3.init()
voice = engine.getProperty('voices')  
engine.setProperty('voice', voice[1].id)
engine.setProperty('rate', 155)
users,namelog,passbookData,BAL,transactions ={},{},{},{},{}
def speak(text):
    engine.say(text)
    engine.runAndWait()

def updateData(self):
    passbookData[self.username] = self.transactions

    with open("data.json", "r") as file:
        existing_data = json.load(file)
    namelog=existing_data['namelog']
    existing_data["BAL"][self.username] =self.balance

    existing_data["passbookData"][self.username] = self.transactions


    with open("data.json", "w") as file:
        json.dump(existing_data, file, indent=4)

class Customer:
    '''This is a MiniVault Application'''
    bankName = 'MYBANK'

    def __init__(self, username, name, balance=0.0):
        self.name = name
        self.username = username
        with open(data_file, 'r') as file:
            data = json.load(file)
            users = data.get('users',{})
            namelog = data["namelog"]
            passbookData = data.get('passbookData',{})
            if username in users:
                BAL = data.get('BAL',{})
                self.transactions = passbookData.get(self.username,[])
                self.balance = BAL.get(username, 0)
            else:
                self.balance=balance
                self.transactions=[]
                updateData(self)

    def deposit(self, amount):
        print(f"Username: {self.username} ") 
        self.balance = self.balance + amount
        msg = f"Dear {self.name},you have deposited {amount} rupees in your account and your bank balance is {self.balance} rupees"
        print(msg)
        speak(msg)

        with open(data_file, 'r') as file:
            data = json.load(file)
            namelog = data["namelog"]
            self.transactions.append({"type": "Deposit", "amount":amount,"balance": self.balance, "date": str(datetime.datetime.now())})
        updateData(self)
    def deposit_fund(self, amount):
        self.balance = self.balance + amount

        with open(data_file, 'r') as file:
            data = json.load(file)
            namelog = data["namelog"]
            self.transactions.append({"type": "Received fund", "amount":amount,"balance": self.balance, "date": str(datetime.datetime.now())})
        updateData(self)

    def withdraw(self, amount):
        print(f"Username: {self.username} ")
        if amount <= self.balance:
            self.balance = self.balance-amount
            msg = f"Dear {self.name},you have withdrawed {amount} rupees in your account and your bank balance is {self.balance} rupees"
            print(msg)
            speak(msg)
            with open(data_file, 'r') as file:
                data = json.load(file)
                namelog = data["namelog"]
                self.transactions.append({"type": "Withdraw", "amount":amount,"balance": self.balance, "date": str(datetime.datetime.now())})

            updateData(self)

        else:
            print("You do not have sufficient balance")
            speak("You do not have sufficient balance")

    def transfer_funds(self, recipient, amount):
        if self.balance >= amount:
            self.balance -= amount
            recipient.deposit_fund(amount)
            with open(data_file, 'r') as file:
                data = json.load(file)
                namelog = data["namelog"]
                self.transactions.append({"type": f"TF:{recipient.username}", "amount": amount,"balance":self.balance, "date": str(datetime.datetime.now())})
            print(f"Dear {self.name}, successfully transferred {amount} rupees to {recipient.name}.\nNow your bank balance is {self.balance} rupees")
            speak(f"Dear {self.name}, successfully transferred {amount} rupees to {recipient.name}.\nNow your bank balance is {self.balance} rupees")
        else:
            print("Insufficient balance for transfer.")
        self.balance = BAL[self.username] = self.balance
        recipient.balance = BAL[recipient.username] = recipient.balance
       

        updateData(self)

    def viewPassbook(self):
        with open(data_file, 'r') as file:
            data = json.load(file)
            users = data.get('users',{})
            namelog = data["namelog"]
            passbookData = data.get('passbookData',{})
            self.transactions = passbookData.get(self.username, [])
        pdf.generate_transaction_pdf(self.username, self.transactions, self.name)




    def logOut(self):
        os.system('cls')
        passbookData[self.username] = self.transactions
        print(f"{self.name},thank you for using MYBANK")
        updateData(self)
        time.sleep(5)
        os.system('cls')
        homeScreen()



data_file = "data.json"

def createAccount():
    os.system('cls')
    print(welcomest)
    print("CREATE AN ACCOUNT")
    name = input("Enter your Name: ").strip().title()
    pattern = r"^[A-Za-z\s]+$"

    if re.match(pattern, name):
        pass
    else:
        print("Invalid name.Type your name using alphabetic characters (A-Z, a-z) only.")
        input("Press enter to continue...")
        createAccount()
    username_instructions ="Instructions: \nThe username can only contain letters (both uppercase and lowercase), numbers, and underscores. \nNo special characters or spaces are allowed in the username."
    print(username_instructions)
    username = input("Enter your username: ")
    pattern = r"^[a-zA-Z0-9_]+$"

    if re.match(pattern, username):
        with open(data_file, 'r') as file:
            data = json.load(file)
            users = data.get('users', {})
            namelog = data.get('namelog', {})

            if username in users:
                msg = "You already have an account in MINIVAULT application. Please LogIn or try creating a new account with a different username."
                print(msg)
                speak(msg)
                time.sleep(5)
                homeScreen()
            else:
                print("Instructions:\nEnter a password that is at least 8 characters long, and includes at least one uppercase letter, one lowercase letter, one digit, and one special character from the set: !@#$%^&*().")
                password = pwinput("Enter Password: ", '.')
                re_password = pwinput("Re-enter Password: ", '.')
                if password == re_password:
                    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*()]).{8,}$"
                    match = re.match(pattern, password)
                    if match:
                        en_pass = encrypt.caesar(password, "encode")
                        users[username] = en_pass[0]
                        namelog[username] = [name, en_pass[1]]  # Add the username as a key with the associated encryption key
                        data['users'] = users
                        data['namelog'] = namelog
                        with open(data_file, 'w') as file:
                            json.dump(data, file)
                        c = Customer(username, name)
                        login()
                    else:
                        print("Invalid password\n\n Instructions: \nEnter a password that is at least 8 characters long, and includes at least one uppercase letter, one lowercase letter, one digit, and one special character from the set: !@#$%^&*().")

                else:
                    print("Entered and Re-entered Password do not match! Please try again.")
                    input("Press enter to continue...")

                    createAccount()       
    else:
        print("Invalid username.Wait for 10 seconds...")
        print(username_instructions)
        time.sleep(10)
        input("Press enter to continue...")
        createAccount()

def login(vinput):
    os.system('cls')
    print(welcomest)
    print("LOG IN")
    username = input("Enter your username: ").strip()
    password = pwinput("Enter your Password: ", '.')

    with open(data_file, 'r') as file:
        data = json.load(file)
        users = data.get('users', {})
        namelog = data.get('namelog', {})

        if username in users:
            if password == encrypt.caesar(users[username],"decode",namelog[username][1])[0]:
                name = namelog[username][0]
                loggedIn(username,vinput, name)
            else:
                print("Please enter a valid username and password. Wait for 10 seconds.")
                speak("Please enter a valid username and password. Wait for 10 seconds.")
                time.sleep(10)
                while True:
                    opt = input("Enter L for login or C to create an account: ").upper()
                    if opt == 'L':
                        login()
                    elif opt == 'C':
                        createAccount()
                    else:
                        print("Enter a valid option")
        else:
            print("Please enter a valid Username. Wait for 10 seconds.")
            speak("Please enter a valid Username. Wait for 10 seconds")
            time.sleep(10)
            while True:
                opt = input("Enter L for login or C to create an account: ").upper()
                speak("Enter L for login or C to create an account")
                if opt == 'L':
                    login()
                elif opt == 'C':
                    createAccount()
                else:
                    print("Enter a valid option")
                    speak("Enter a valid option")
    os.system('cls')

def loggedIn(username,vinput, name="User"):
    c = Customer(username, name)
    rupee_symbol = '₹'.encode('utf-8').decode('utf-8')
    os.system('cls')
    print(f"MINIVAULT CUSTOMER: {name}")


    while True:
        opt = input("D-Deposit | W-Withdraw | TF-Transfer Funds | VP-ViewPassbook | LO-LogOut: ").upper()

        if opt == 'D':
            try:
                speak("Enter the amount you want to deposit")
                if vinput==True:
                    print(f"Enter the amount you want to deposit: {rupee_symbol}")
                    amount = int(jarvis.voice_input().strip())
                else:
                    amount = int(input(f"Enter the amount you want to deposit: {rupee_symbol}"))
                    c.deposit(amount)
            except ValueError:
                speak("Kindly enter amount in numbers only")
                print("Kindly enter amount in numbers only eg. 2999")
        elif opt == 'W':
            try:
                speak("Enter the amount you want to withdraw")
                if vinput==True:
                    print(f"Enter the amount you want to withdraw: {rupee_symbol}")
                    amount = int(jarvis.voice_input().strip())
                else:
                    amount = int(input(f"Enter the amount you want to withdraw: {rupee_symbol}"))
                c.withdraw(amount)
            except ValueError:
                speak("Kindly enter amount in numbers only")
                print("Kindly enter amount in numbers only eg. 2999")
        elif opt == "TF":
            speak("Enter username of bankholder you want to deposit amount in")
            if vinput==True:
                print("Enter username of bankholder you want to deposit amount in: ")
                tf_user = jarvis.voice_input().strip()
            else:
                tf_user = input("Enter username of bankholder you want to deposit amount in: ")
                    
            with open(data_file, 'r') as file:
                data = json.load(file)
                users = data.get('users', {})
                namelog = data.get('namelog', {})
            if tf_user in users:
                tf_name = namelog[tf_user][0]
                tf_key = namelog[tf_user][1]
                recipient = Customer(tf_user, tf_name)
                speak("Enter the amount you want to deposit")
                amount = int(input(f"Enter the amount you want to deposit: {rupee_symbol}"))
                c.transfer_funds( recipient, amount)
            else:
                speak("Username not found! Kindly Try again")
                print("Username not found! Kindly Try again...")
                time.sleep(5)
                loggedIn(username,name)
        elif opt == "VP":
            c.viewPassbook()
        elif opt == 'LO':
            c.logOut()
            break
        else:
            speak("Please enter a valid option.")
            print("Please enter a valid option.")


def homeScreen():
    os.system("cls")
    print(welcomest)
    speak(welcomest)
    vinp_choice = input("How do you want to input? V-Voice | T-Text : ").upper()
    def vinp():
        
        if vinp_choice == "V":
            return True
        elif vinp_choice == "T":
            return False
        else:
            print("Please enter correct opt...V for Voice and T for Text..")
            time.sleep(5)
            vinp()
    vinput = vinp()
    if vinput == True:
        speak("Do you want to login or create account? ")
        print("LogIn | Create Account: ")
        signOpt = jarvis.voice_input().strip()
    else:
        speak("Type L for login or C for create account")
        signOpt = input("L- LogIn | C-Create Account: ")
    if signOpt.lower() in ['l','login']:
        login(vinput)
    elif signOpt.lower() == ['c','create account']:
        createAccount()
    else:
        homeScreen()


homeScreen()