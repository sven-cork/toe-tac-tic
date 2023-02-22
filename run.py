import random
from termcolor import colored

computer_score = 0
player_score = 0

print("""
Beat the computer in classic Tic-Tac-Toe.

Choose side and score three in a row for a win.
""")

game_board = ["-", "-", "-",
              "-", "-", "-",
              "-", "-", "-"]

player = ""
while True: 
    player = input("Player select team 'X' or 'O': ").upper()
    if player == "X" or player == "O":
        break

computer = ""
if player == "X":
    computer = "O"
else:
    computer = "X"

#global variables:
#game_board
#player?

#functions:
#display board
#select_player
#select slot on board and update board
#winner
#computer turn
#winner

#select_player
"""
    def select_player():

    
    #Let player select team "X" or "O". Checks if either
    of the valid teams (characters) have been selected
    and corrects for lower case entered character."

    player = ""

    while True: 
        player = input("Player select team 'X' or 'O': ").upper()
        if player == "X" or player == "O":
            break
    print(player)
    return player
"""

def display_board(game_board):
    print(colored("+---+---+---+", "red"))
    print(colored("| ", 'red') + game_board[0] + colored(" | ", "red") + game_board[1] + \
    colored(" | ", "red") + game_board[2] + colored(" | ", "red"))
    print(colored("+---+---+---+", "red"))
    print(colored("| ", 'red') + game_board[3] + colored(" | ", "red") + game_board[4] + \
    colored(" | ", "red") + game_board[5] + colored(" | ", "red"))
    print(colored("+---+---+---+", "red"))
    print(colored("| ", 'red') + game_board[6] + colored(" | ", "red") + game_board[7] + \
    colored(" | ", "red") + game_board[8] + colored(" | ", "red"))
    print(colored("+---+---+---+", "red"))

#select slot on board and update board
def user_input(game_board):
    """
    User selects slot to place X or O. Checks if slot already taken and if so 
    prompts user to select a new slow.
    """

    user_input = int(input("Select a slot (1-9) on the game board: "))
    if user_input >= 1 and user_input <= 9 and (game_board[user_input - 1] != "X"
        or game_board[user_input - 1] != "O"):
        game_board[user_input - 1] = player
    else:
        print("Try again")

#winner?

def update_score(winner_character):
    global player
    global computer
    global player_score
    global computer_score

    print(f"Updating score for: {winner_character}")
    print(f"Player score: {player_score}")
    print(f"Computer score: {computer_score}")

    if winner_character == player:
        player_score += 1
    else:
        computer_score += 1

def check_winner(game_board):
    """Checks winner if three of the same characters (X or O) have been 
    selected either horizontaly, vertically or diagonaly"""

    #check horizontal win condition
    if game_board[0] == game_board[1] == game_board[2]\
    and game_board[0] != "-":
        print(f"{game_board[0]} is the winner!!")
        update_score(game_board[0])
        
        #run_game = False
        play_again()
    elif game_board[3] == game_board[4] == game_board[5] and game_board[3] != "-":
        print(f"{game_board[3]} is the winner!!")
        update_score(game_board[3])

        #run_game = False
        play_again()
    elif game_board[6] == game_board[7] == game_board[8] and game_board[6] != "-":  
        print(f"{game_board[6]} is the winner!!")
        update_score(game_board[6])
        #run_game = False
        play_again()
    #check vertical win condition
    if game_board[0] == game_board[3] == game_board[6] \
    and game_board[0] != "-":
        print(f"{game_board[0]} is the winner!!")
        update_score(game_board[0])
        #run_game = False
        play_again()
    elif game_board[1] == game_board[4] == game_board[7] \
    and game_board[1] != "-":
        print(f"{game_board[1]} is the winner!!")
        update_score(game_board[1])
        #run_game = False
        play_again()
    elif game_board[2] == game_board[5] == game_board[8] \
    and game_board[2] != "-":  
        print(f"{game_board[2]} is the winner!!")
        update_score(game_board[2])
        #run_game = False
        play_again()

    #check diagnoal win condition
    if game_board[0] == game_board[4] == game_board[8] \
    and game_board[0] != "-":
        print(f"{game_board[0]} is the winner!!")
        update_score(game_board[0])
        #run_game = False
        play_again()
    elif game_board[2] == game_board[4] == game_board[6] \
    and game_board[2] != "-":
        print(f"{game_board[2]} is the winner!!")
        update_score(game_board[2])
        #run_game = False
        play_again()
        
#Computer turn based on random generated number applied to non occupied game board slot
def computer_turn():
    while True:
        random_number = random.randint(1,9)
        print("Random number: ", random_number)
        if game_board[random_number - 1] != "X" \
        and game_board[random_number - 1] != "O":
            game_board[random_number - 1] = computer
            print("computer selected: ", random_number)
            display_board(game_board)
            break

def play_again():

    play_again_selection = ""

    while True:
        play_again_selection = input("Would you like to continue, yes or no (y/n): ").upper()
        if play_again_selection == "Y" or play_again_selection == "N":
            break
        else:
            print("Enter valid string 'y' or 'n'")
    
    if play_again_selection == "Y":
        global game_board
        game_board = ["-", "-", "-",
                      "-", "-", "-",
                      "-", "-", "-"]
        print("Player score: ", player, "\nComputer score:", computer_score)
        main()
    
    else:
        print("Player score: ", player, "\nComputer score:", computer_score)
        quit()

    
def shark():
    shark = """
                                 ^`.                     o
     ^_              \  \                  o  o
     \ \             {   \                 o
     {  \           /     `~~~--__
     {   \___----~~'              `~~-_     ______          _____
      \                         /// a  `~._(_||___)________/___
      / /~~~~-, ,__.    ,      ///  __,,,,)      o  ______/    
      \/      \/    `~~~;   ,---~~-_`~= \ \------o-'            
                       /   /            / /
                      '._.'           _/_/
                                      ';|
                                        """
    print(shark)

def main():
    run_game = True
    while run_game:
    #select_player()
        shark()
        display_board(game_board)
        user_input(game_board)
        print(f"Player character is: {player}")
        print(f"Computer character is: {computer}")
        print("Player is: ", player)
        print("Computer is:", computer)
        display_board(game_board)
        check_winner(game_board)
        computer_turn()
        check_winner(game_board)

main()