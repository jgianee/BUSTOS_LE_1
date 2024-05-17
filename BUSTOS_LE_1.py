# Dictionary to store game library with their quantities and rental costs
import time
import os

game_library = {
    "Donkey Kong": {"quantity": 3, "cost": 2},
    "Super Mario Bros": {"quantity": 5, "cost": 3},
    "Tetris": {"quantity": 2, "cost": 1}
    # Add more games as needed
}

# Dictionary to store user accounts with their balances and points
user_accounts = {}

# Admin account details
admin_username = "admin"
admin_password = "adminpass"

# Function to display available games with their numbers and rental costs
def display_available_games():
    print("Game Library")
    n = 1
    for game, info in game_library.items():
        print(f"{n}. {game}:")
        n += 1
        for name, value in info.items():
            print(f"\t{name.title()}: {value}")

# Function to register a new user
def register_user():
    global user_accounts
    print("Register Window")
    username = input("Enter username: ")
    if username in user_accounts.keys():
        print("Username already exists. Choose another one.")
    if username == "":
        return
    else:
        password = input("Enter password: ")
        if password == "":
            return
        else:
            user_accounts[username] = {"password": password, "balance": 0.00, "points": 0, "inventory": {}}
            print("Account registered successfully.")
            time.sleep(1)
            os.system('cls')
            return

# Function to rent a game
def rent_game(username):
    if user_accounts[username]["balance"] == 0:
        print("Insufficient balance. Please top up first before renting a game.")
        input("\nPress ENTER to go back to menu.")
        return
    while True:
        try:
            print("Greetings!,", username)
            display_available_games()
            print("Balance:", user_accounts[username]["balance"])
            game_number = input("Enter a game to rent (number only): ")
            if game_number == "":
                return
            game_number = int(game_number)
            if 1 <= game_number <= len(game_library):
                game = list(game_library.keys())[game_number - 1]
                if game_library[game]["quantity"] > 0:
                    quantity = int(input(f"Enter how many copy/s of {game} to rent: "))
                    if 1 <= quantity <= game_library[game]["quantity"]:
                        os.system('cls')
                        print(f"\n{'-'*50}")
                        print(f"Rented {quantity} copy/s of {game}.")
                        game_library[game]["quantity"] -= quantity
                        if game in user_accounts[username]["inventory"]:
                            user_accounts[username]["inventory"][game]["copy/s"] += quantity
                        else:
                            user_accounts[username]["inventory"][game] = {"copy/s": quantity}
                        cost = quantity * game_library[game]["cost"]
                        cost = (cost)
                        balance = user_accounts[username]["balance"] - cost
                        points = cost / 2
                        user_accounts[username]["balance"] = balance
                        user_accounts[username]["points"] += int(points)
                        if game_library[game]["quantity"] == 0:
                            del game_library[game]
                        print(f"Total cost to rent {quantity} copy/s of {game} is {cost}.")
                        print(f"{cost} deducted from balance.")
                        print(f"{int(points)} points earned from renting.")
                        time.sleep(1)
                        print(f"\n{'-'*50}")
                        break
                    else:
                        print(f"There are only {game_library[game]['quantity']} copy/s of {game}.")
                        input("\nPress ENTER to continue.")
            else:
                print(f"Choose from 1 to {len(game_library)} only.")
                input("\nPress ENTER to continue.")
                os.system('cls')
        except ValueError:
            print(f"Please enter a positive integer only.")
            input("\nPress ENTER to continue.")
            os.system('cls')

# Function to return a game
def return_game(username):
    if not user_accounts[username]["inventory"]:
        print("You have nothing in your inventory to return.")
        input("\nPress ENTER to continue.")
        return
    else:
        while True:
            try:
                display_inventory(username)
                game_number = input("Enter the number of the game to return: ")
                if game_number == "":
                    return
                
                game_number = int(game_number)
                inventory = user_accounts[username]["inventory"]
                
                if 1 <= game_number <= len(inventory):
                    game = list(inventory.keys())[game_number - 1]
                    quantity = input(f"Enter number of copies of '{game}' to return: ")
                    
                    if quantity == "":
                        return
                    
                    quantity = int(quantity)
                    
                    if quantity <= 0:
                        print("Please enter a positive value.")
                        return
                        
                    if quantity > inventory[game]["copy/s"]:
                        print("You don't have that many copies to return.")
                        return
                    
                    inventory[game]["copy/s"] -= quantity
                    game_library[game]["quantity"] += quantity
                    
                    if inventory[game]["copy/s"] == 0:
                        del user_accounts[username]["inventory"][game]
                        os.system('cls')
                        print(f"\n{'-'*50}")
                        print(f"All copies of '{game}' returned and removed from inventory.")
                    else:
                        print(f"{quantity} copy/s of '{game}' returned.")
                    print(f"\n{'-'*50}")
                    time.sleep(1)
                    display_inventory(username)
                else:
                    print(f"Invalid game number. Please choose from 1 to {len(inventory)}.")
                input("\nPress ENTER to continue.")
                break
            except ValueError:
                print("Please enter a positive integer only.")


# Function to top-up user account
def top_up_account(username):
    print("Top up Window")
    print("Balance: ", user_accounts[username]["balance"])
    while True:
        try:
            amount = input("Enter amount to add to your balance: ")
            if amount == "":
                return
            amount = float(amount)
            if amount <= 0:
                print("Please enter a positive number only.")
                input("\nPress ENTER to continue.")
                os.system('cls')
            else:
                user_accounts[username]["balance"] += amount
                time.sleep(1)
                print("\nBalance updated successfully.")
                print("Balance: ", user_accounts[username]["balance"])
                input("\nPress ENTER to continue.")
                break
        except ValueError:
            print("Please enter a positive integer only.")
            input("\nPress ENTER to continue.")
            os.system('cls')

# Function to display user's inventory
def display_inventory(username):
    inventory = user_accounts[username]["inventory"]
    if not inventory:
        print("Inventory is empty.")
    else:
        print(f"{username}'s Inventory")
        n = 1
        for game, details in inventory.items():
            print(f"{n}. {game}")
            print(f"\tQuantity: {details['copy/s']} pc/s")
            n+=1
    input("\nPress ENTER to continue.")

# Function for admin to update game details
def admin_update_game():
    while True:
        try:
            display_available_games()
            print("1. Edit Game")
            print("2. Add Game")
            print("3. Remove Game")
            choice = input("Enter option: ")
            if choice == "":
                break
            choice = int(choice)
            if choice == 1:
                os.system('cls')
                print(f"\n{'-'*50}")
                while True:
                    n = 1
                    for game in (game_library.keys()):
                        print(f"{n}. {game}")
                        n += 1
                    game_number = input("Choose a game to edit (number only): ")
                    if game_number == "":
                        return
                    game_number = int(game_number)
                    if 1 <= game_number <= len(game_library.keys()):
                        game = list(game_library.keys())[game_number - 1]
                        while True:
                            os.system('cls')
                            print(f"\n{'-'*50}")
                            print("1. Change Game Name")
                            print("2. Change Quantity")
                            print("3. Change Cost")
                            option = input("Enter option: ")
                            if option == "":
                                return
                            option = int(option)
                            if option == 1:
                                new_name = input(f"Enter new name for {game}: ")
                                if new_name == "":
                                    return
                                if new_name in game_library:
                                    print("That name already exists in the game library.")
                                else:
                                    game_details = game_library.pop(game)
                                    game_library[new_name.title()] = game_details
                                    print(f"{game} has been changed to {new_name}.\n")
                                    time.sleep(1)
                                    os.system('cls')
                                    print(f"\n{'-'*50}")
                            elif option == 2:
                                new_quantity = input(f"Enter new quantity for {game}: ")
                                if new_quantity == "":
                                    return
                                else:
                                    new_quantity = int(new_quantity)
                                    game_library[game]["quantity"] = new_quantity
                                    print(f"Quantity for {game} has been changed to {new_quantity}.\n")
                                    time.sleep(1)
                                    os.system('cls')
                                    print(f"\n{'-'*50}")
                            elif option == 3:
                                new_cost = input(f"Enter new cost for {game}: ")
                                if new_cost == "":
                                    return
                                else:
                                    new_cost = int(new_cost)
                                    game_library[game]["cost"] = new_cost
                                    print(f"Cost for {game} has been changed to {new_cost}.\n")
                                    time.sleep(1)
                                    os.system('cls')
                                    print(f"\n{'-'*50}")                            
                            else:
                                print("Choose from 1-3 only.")
                                input("\nPress ENTER to continue.")
                                os.system('cls')
                    else:
                        print(f"Choose from 1 to {len(game_library.keys())} only.")
                        input("\nPress ENTER to continue.")
                        os.system('cls')
            elif choice == 2:
                os.system('cls')
                print(f"\n{'-'*50}")
                game_add = input("Enter the name of a game to be added: ")
                if game_add == "":
                    return
                if game_add not in game_library.keys():
                    quantity = input("Enter quantity of game: ")
                    if quantity == "":
                        return
                    quantity = int(quantity)
                    if quantity > 0:
                        cost = input(f"Enter cost per copy of {game_add}: ")
                        if cost == "":
                            return
                        cost = int(cost)
                        if cost >= 1:
                            game_library[game_add] = {"quantity": quantity, "cost": cost}
                            print(f"{game_add} has been added to game library.")
                            time.sleep(1)
                            os.system('cls')
                            print(f"\n{'-'*50}")
                        else:
                            print("Enter a positive value.")             
                            input("\nPress ENTER to continue.")
                    else:
                        print("Enter a positive value.")
                        input("\nPress ENTER to continue.")
                else:
                    print("This game is already in the library.")
                    input("\nPress ENTER to continue.")
            elif choice == 3:
                while True:
                    os.system('cls')
                    print(f"\n{'-'*50}")
                    n = 1
                    for game in game_library.keys():
                        print(f"{n}. {game}")
                        n += 1
                    remove_game = input("Enter the game to be removed (number only): ")
                    if remove_game == "":
                        return
                    remove_game = int(remove_game)
                    if 1 <= remove_game <= len(game_library.keys()):
                        game = list(game_library.keys())[remove_game - 1]
                        del game_library[game]
                        print(f"{game} removed from game library.")
                        time.sleep(1)
                        os.system('cls')
                        print(f"\n{'-'*50}")
                    else:
                        print(f"Choose from 1 to {len(game_library.keys())} only.")
                        input("\nPress ENTER to continue.")      
                        os.system('cls')
            else:
                print("Choose from 1-3 only.")
                input("\nPress ENTER to continue.")
                os.system('cls')
        except ValueError:
            print("Please enter a positive integer only.")
            input("\nPress ENTER to continue.")
            os.system('cls')

# Function for admin login
def admin_login():
    print("Admin Login Window")
    while True:
        username = input("Enter admin username: ")
        if username == "":
            break
        if username == admin_username:
            while True:
                password = input(f"Enter password for {admin_username} (leave blank to exit): ")
                if password == "":
                    return
                if password == admin_password:
                    print("Admin Login successful.")
                    time.sleep(1)
                    os.system('cls')
                    print(f"\n{'-'*50}")
                    admin_menu(admin_username)
                    break
                else:
                    print("Incorrect password.")           
        else:
            print("Admin username not found.")

# Admin menu
def admin_menu(admin_username):
    while True:
        try:
            os.system('cls')
            print(f"\n{'-'*50}")
            print(f"Welcome, {admin_username}!")
            print("Admin Menu")
            print("1. Update Game Details.")
            print("2. Game Inventory")
            print("3. Logout")
            choice = int(input("Enter choice: "))
            if choice == 1:
                os.system('cls')
                print(f"\n{'-'*50}")
                admin_update_game()
            elif choice == 2:
                os.system('cls')
                print(f"\n{'-'*50}")
                display_game_inventory()
            elif choice == 3:
                os.system('cls')
                home = "Returning to home screen..."
                for char in home:
                    print(char, end="")
                    time.sleep(0.02)
                print("\n")
                return
            else:
                print("Choose from 1 to 3 only.")
                input("\nPress ENTER to continue")
                os.system('cls')
        except ValueError:
            print("Please enter a positive integer only.")
            input("\nPress ENTER to continue.")
            os.system('cls')

# Function for users to redeem points for a free game rental
def redeem_free_rental(username):
    if user_accounts[username]["points"] < 3:
        print("Insufficient points to redeem free game rental. Atleast 3 points is needed.")
        input("\nPress ENTER to go back to menu.")
    else:
        print("Game Library")
        n = 1
        for game in game_library.keys():
            print(f"{n}. {game}")
            n += 1
        print("Points:", user_accounts[username]["points"])
        choice = input("Choose a game to redeem with points: ")
        if choice == "":
            return
        else:
            choice = int(choice)
            game = list(game_library.keys())[choice - 1]
            if game in user_accounts[username]["inventory"]:
                user_accounts[username]["inventory"][game]["copy/s"] += 1
            else:
                user_accounts[username]["inventory"][game] = {"copy/s": 1}
            user_accounts[username]["points"] -= 3
            os.system('cls')
            print(f"\n{'-'*50}")
            print(f"{game} redeemed successfully. Added to Inventory.")
            print(f"3 point deducted.")
            time.sleep(1)
            print(f"\n{'-'*50}")

# Function to display game inventory
def display_game_inventory():
    display_available_games()
    for username, info in user_accounts.items():
        rented_games = info["inventory"]
        if rented_games:
            print("\nRented Games:")
            print(f"{username}:")
            for game, quantity in rented_games.items():
                print(f"{game}: Quantity: {quantity}")
        else:
            print("There is no rented games.")
    input("\nPress ENTER to go back to menu.")


# Function to handle user's logged-in menu
def logged_in_menu(username):
    while True:
        try:
            os.system('cls')
            print(f"\n{'-'*50}")
            print("Video Game Rental System")
            print(f"Welcome, {username}!")
            print("1. View Available Games")
            print("2. Rent/Return Games")
            print("3. Check Inventory")
            print("4. Topup Balance")
            print("5. Logout")
            choice = int(input("Enter option: "))
            if choice == 1:
                os.system('cls')
                print(f"\n{'-'*50}")
                display_available_games()
                input("\nPress ENTER to go back to menu.")
            elif choice == 2:
                while True:
                    try:
                        os.system('cls')
                        print(f"\n{'-'*50}")
                        print("1. Rent Game")
                        print("2. Redeem Free Rental")
                        print("3. Return Game")
                        option = input("Choose an option (leave blank to exit): ")
                        if option == "":
                            break
                        option = int(option)
                        if option == 1:
                            os.system('cls')
                            print(f"\n{'-'*50}")
                            rent_game(username)
                        elif option == 2:
                            os.system('cls')
                            print(f"\n{'-'*50}")
                            redeem_free_rental(username)
                        elif option == 3:
                            os.system('cls')
                            print(f"\n{'-'*50}")
                            return_game(username)
                        else:
                            print("Please choose from 1-3 only.")
                            time.sleep(1)
                    except ValueError:
                        print("Please enter a positive integer only.")
                        time.sleep(1)
            elif choice == 3:
                os.system('cls')
                print(f"\n{'-'*50}")
                display_inventory(username)
            elif choice == 4:
                os.system('cls')
                print(f"\n{'-'*50}")
                top_up_account(username)
            elif choice == 5:
                os.system('cls')
                home = "Returning to home screen..."
                for char in home:
                    print(char, end="")
                    time.sleep(0.05)
                print("\n")
                return
            else:
                print("Please choose from 1-5 only.")
                input("\nPress ENTER to continue.")
        except ValueError:
            print("Please enter a positive integer only.")
            input("\nPress ENTER to continue.")

# Function to check user credentials
def check_credentials():
    if not user_accounts:
        print("Unable to login. No account is registered.")
        input("\nPress ENTER to go back to menu.")
    else:
        print("Login Window")
        while True:
            username = input("Enter username: ")
            if username == "":
                break
            if username not in user_accounts.keys():
                print("Username not found. Enter a registered username.")
                time.sleep(0.5)
            else:
                while True:
                    password = input(f"Enter password for {username} (leave blank to exit): ")
                    if password == "":
                        break
                    if password == user_accounts[username]["password"]:
                        print("Login successful.")
                        time.sleep(1)
                        os.system('cls')
                        logged_in_menu(username)
                    else:
                        print("Incorrect password.")
                        time.sleep(0.5)
                
# Main function to run the program
def main():
    while True:
        try:
            os.system('cls')
            print(f"\n{'-'*50}")
            print("Home Window")
            print("1. Login")
            print("2. Admin Login")
            print("3. Register")
            print("4. Exit")
            choice = int(input("Enter number only: "))
            if choice == 1:
                os.system('cls')
                print(f"\n{'-'*50}")
                check_credentials()
            elif choice == 2:
                os.system('cls')
                print(f"\n{'-'*50}")
                admin_login()
            elif choice == 3:
                os.system('cls')
                print(f"\n{'-'*50}")
                register_user()
            elif choice == 4:
                os.system('cls')
                exit = "Exiting program..."
                for char in exit:
                    print(char, end="")
                    time.sleep(0.02)
                break
            else:
                print("Choose from 1-4 only.")
                time.sleep(1)
        except ValueError:
            print("Please enter a positive integer only.")
            time.sleep(1)

if __name__ == "__main__":
    main()