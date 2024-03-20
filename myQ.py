import boto3
from Utils.Util import Util
from Account import Account

def create_account(args) -> None:
    if (len(args) != 3):
        print("Invalid args length")
        return
        
    username = args[1]
    password = args[2]

    salt = Util.generate_salt()
    hash = Util.generate_hash(password, salt)
    account = Account(username, salt=salt, hash=hash)
    account.save_to_database()
    #try:
    #    account.save_to_database() 
    #except Exception as e:
    #    print("Failed to create new account")
    #    quit()
    print("Created user ", username)

def start():#
    stop = False

    while not stop:
        response = ""
        print("> ",end='')
        try:
            response = str(input())

        except ValueError:
            print("Try Again") 
            break

        response = response.lower() 
        args = response.split(" ")
        operation = args[0]

        if operation == "create_account":
            create_account(args)

if __name__ == "__main__":
    print("----- Welcome to MyQ ------")
    start()

