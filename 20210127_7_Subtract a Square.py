# Code author : Khaled Waleed Salah, First academic year
# Date: 26 February 2022
# Institution : Faculty of Computers and Artificial intelligence - Cairo University
# Prepared for Dr.Mohammed El-Ramly, for assignment 1
# Purpose : Subtract A Square game



from os import system, name
# intializing the coins' number, subtract and a boolean condition to detect who is the last player
subtract = 0
last_player = True

# initializing the coins' number, subtract and a boolean condition to detect who is the last player
while True:
    try:
        coins = int(input("Please enter the number of coins you want to play with (must be an integer between (25, 1,000,000 ) inclusive : "))
        if coins > 1000000 or coins < 25:
            int("s")
        else:
            break
    except:
        print("Invalid input.")

# to clear the terminal for cleaner game:
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

# a function to ask player for input and detect if that  input is valid, it does have defensive programmin
def play_player_X_(player):
    global last_player
    while True:
        # try except to defend against characters and empty input etc....
        try:
            subtract_ = float(
                input(
                    f"\nplayer {player} please enter a squared number from 1 to 6 inclusive ( 1, 4, 9, 16, 25, 36) : "))
            # checking if input is in the acceptable range
            if subtract_ not in [1, 4, 9, 16, 25, 36]:
                # if the input is not in the acceptable range then deliberately throw an error to activate the try except
                int("s")
            else:
                # changing the last player to later decide the winner
                if player == 1:
                    last_player = True
                else:
                    last_player = False
                    # return the final valid user input
                return subtract_
            # if input threw an error for any reason then tell user and ask for input again
        except :
            print("Not a valid input, please enter a valid squared integer below. ")

# as it says, update game state using input when called
def update_game(subtract__):
    global coins
    # subtract the input from coins to update game
    coins -= subtract__
    # prints the current state of game if coins are more than 1
    if coins > 0:
        print(f"left coins are: {int(coins)}")

# to check if there is a winner
def is_game_done():
    global coins, last_player
    # bool to check if the game is done but it does not return to give chance
    # to the rest of the function to print the winner and ask to play again
    if coins <= 0:
        is_current_game_done = True
    else:
        is_current_game_done = False

    if is_current_game_done:
        # if coins are zero or less than zero then declare winner using the last player condition
        if last_player:
            print("\nCongrats player 1, you won ! .... good luck next time player 2")
        else:
            print("\nCongrats player 2, you won ! .... good luck next time player 1")
            # activate function to ask again
        if ask_to_play_again():
            play_again = False
        else:
            play_again = True
            # return that game is done and return if we want to play again
        return [is_current_game_done, play_again]
    else:
        return [False]

# ask the user if they want to play agian
def ask_to_play_again():
    global coins
    while True:
        play_again = input("Type (y) to play again, (n) to exit: ")
        if play_again == 'n':
            print("\nThank you for playing !")
            return False;
        if play_again == 'y':
            while True:
                try:
                    coins = int(input(
                        "please enter the number of coins you want to play with (must be an integer between (25, 1,000,000 ) inclusive : "))
                    if coins > 1000000 or coins < 25:
                        int("s")
                    else:
                        break
                except:
                    print("Invalid input.")
            clear()
            print(f"Number of coins is : {coins}")
            return True



# the main game loop
while True:
    # first player players
    subtract = play_player_X_(1)
    clear()
    # update game status ( internally and on display)
    update_game(subtract)

    # check if the game is done
    # if someone wins declare their name and end
    done = is_game_done()
    if done[0]:
        if done[1]:
            break
        else:
            continue

    # second player plays
    subtract = play_player_X_(2)
    clear()
    # update game status ( internally and display)
    update_game(subtract)

    # check if the game is done
    # if someone wins declare their name and end
    done = is_game_done()
    if done[0]:
        if done[1]:
            break
        else:
            continue

z = input("Press Enter key to exit.")