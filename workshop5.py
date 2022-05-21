import random

def guess_random_number(tries, start, stop) :
    num_start = start
    num_stop = stop   
    random_num = random.randint(num_start, num_stop)
    user_data = []
    while tries != 0:
        print("Number of tries left: ", tries)
        user_guess = input("Guess a number between " + str(num_start) + " and " + str(num_stop) + ": ")
        user_guess = int(user_guess)
        if user_guess > stop or user_guess < start:
            print("Pick a numbber between the range.")
        elif user_guess in user_data:
            print("You already picked that number.")
        else:
            if random_num > user_guess:
                print("Guess higher!")
                tries = tries - 1
                user_data.append(user_guess)
                print(user_data)
                if tries == 0:
                    print("You have failed to guess the number!")
                    break
            elif random_num < user_guess:
                print("Guess Lower!")
                tries = tries - 1
                user_data.append(user_guess)
                print(user_data)
                if tries == 0:
                    print("You have failed to guess the number!")
                    break
            elif user_guess == user_guess:
                print("You guessed the correct number!")
                break

def guess_random_num_linear(tries, start, stop):
    num_start = start
    num_stop = stop   
    random_num = random.randint(num_start, num_stop)
    print("The number for the program to guess is: ", random_num)
    tries = tries
    the_list = range(start, stop, 1)
    while tries != 0:
        for x in range(len(the_list)):
            print("The computer is guessing... ", x)
            if the_list[x] == random_num:
                print("Computer guessed the number at index", x)
                return True
            elif the_list != random_num:
                tries = tries - 1
                print("Number of tries left: ", tries)
                if tries == 0:
                    print("Computer have failed to guess the number!")
                    return False
                    break

def guess_random_num_binary(tries, start, stop):
    num_start = start
    num_stop = stop   
    random_num = random.randint(num_start, num_stop)
    print("The number for the program to guess is: ", random_num)
    tries = tries
    the_list = range(start, stop, 1)
    lower_bound = 0
    upper_bound = len(the_list) - 1
    while lower_bound <= upper_bound:
        pivot = (lower_bound + upper_bound) // 2
        pivot_value = the_list[pivot]

        if pivot_value == random_num:
            print("Computer guessed the number at", random_num)
            return pivot
        if pivot_value > random_num:
            upper_bound = pivot -1
            tries = tries - 1
            print("Guessing lower...")
            if tries == 0:
                print("Computer have failed to guess the number!")
                break
        elif pivot_value < random_num:
            lower_bound = pivot + 1
            tries = tries - 1
            print("Guessing higher...")
            if tries == 0:
                print("Computer have failed to guess the number!")
                break
        return -1 

def guess_random_num_user():
    while True:
        try:
            user_tries = input("Input number of tries: ")
            user_tries = int(user_tries)
        except:
            print("Invalid Input")
            continue
        if user_tries > 0:
            try:
                user_start = input("Input starting number: ")
                user_stop = input("Input end number: ")
                user_start = int(user_start)
                user_stop = int(user_stop)
            except:
                print("Invalid input")
                continue
            if user_start < 0 or user_stop <= user_start:
                print("Invalid entry. Starting number and Ending number cannot be negative number,\nand Ending number cannot be lesser than starting number.")
            else:
                print("1. User guess\n2. Linear search\n3. Bineary search")
                user_method = input("How do you want to guess the number?: ")
                if user_method == "1":
                    guess_random_number(user_tries, user_start, user_stop)
                elif user_method == "2":
                    guess_random_num_linear(user_tries, user_start, user_stop)
                elif user_method == "3":
                    guess_random_num_binary(user_tries, user_start, user_stop)
                break
        else:
            print("Invalid Input")

def guess_random_num_game():
    player = {
        "money": 10
    }
    while True:
        try:
            print("Enter 1 if you think the computer will guess the number right")
            print("Enter 2 if you think the computer will guess the number wrong")
            print("Enter 3 to exit game\n")
            user_choice = input("Guess if the computer will get the random number right: ")
            user_choice = int(user_choice)
        except:
            print("\nInvalid choice. Please try again.")
            continue
        while True:
            player_money = 10
            if user_choice == 1:
                    try:
                        player_bet = input("How much would you like to bet? You currently have: $" +  str(player["money"]) + ": ")
                        player_bet = int(player_bet)
                    except:
                        print("\nInvalid choice. Please try again.")
                        continue
                    if player_bet <= 0 or player_bet > player["money"]:
                        print("Bet amount cannot be less than 1 or greater than your total amount")
                    else: 
                        print("You have betted $" , player_bet)
                        player["money"] = player["money"] - player_bet
                        game_result = guess_random_num_linear(5, 0, 10)
                        if game_result == True:
                            print("\nYou won!\n")
                            player["money"] = (player_bet * 2) + player["money"]
                            print("You now have $", player["money"], "\n")
                            if player["money"] > 50:
                                print("\n***You win! Please play again.\n")
                                player["money"] = 10
                            break
                        elif game_result == False:
                            print("\nYou lose!\n")
                            print("You now have $", player["money"])
                            if player["money"] <= 0:
                                print("\n***Game over! You lost all of your money.***\nHeres $10 for you. Please try again\n")
                                player["money"] = 10
                            break
            elif user_choice == 2:
                    try:
                        player_bet = input("How much would you like to bet? You currently have: $" +  str(player["money"]) + ": ")
                        player_bet = int(player_bet)
                    except:
                        print("\nInvalid choice. Please try again.")
                        continue
                    if player_bet <= 0 or player_bet > player["money"]:
                        print("Bet amount cannot be less than 1 or greater than your total amount")
                    else: 
                        print("You have betted $" , player_bet)
                        player["money"] = player["money"] - player_bet
                        game_result = guess_random_num_linear(5, 0, 10)
                        if game_result == False:
                            print("\nYou won!\n")
                            player["money"] = player["money"] + (player_bet * 2)
                            print("You now have $", player["money"], "\n")
                            if player["money"] > 50:
                                print("\n***You win! Please play again.\n")
                                player["money"] = 10
                            break
                        elif game_result == True:
                            print("\nYou lose!\n")
                            print("You now have $", player["money"])
                            if player["money"] <= 0:
                                print("\n***Game over! You lost all of your money.***\nHeres $10 for you. Please try again\n")
                                player["money"] = 10
                            break
            elif user_choice == 3:
                print("Good bye")
                return
            else:
                print("\nInvalid choice. Please try again.")

# Driver code for Task 1.
# guess_random_number(5, 0, 10)

# Driver code for Task 2.
# guess_random_num_linear(5, 0, 10)

# Driver code for Task 3.
# guess_random_num_binary(5, 0, 100)

# Driver code for bonus tasks.
# guess_random_num_user()
guess_random_num_game()