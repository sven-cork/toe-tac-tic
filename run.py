import random

game_board = ["-", "-", "-",
              "-", "-", "-",
              "-", "-", "-"]
              
print(game_board)

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
    print("+---+---+---+")
    print("| " + game_board[0] + " | " + game_board[1] + \
    " | " + game_board[2] + " | ")
    print("+---+---+---+")
    print("| " + game_board[3] + " | " + game_board[4] + \
    " | " + game_board[5] + " | ")
    print("+---+---+---+")
    print("| " + game_board[6] + " | " + game_board[7] + \
    " | " + game_board[8] + " | ")
    print("+---+---+---+")

#select slot on board and update board
def user_input(game_board):
    """
    User selects slot to place X or O. Checks if slot already taken and if so 
    prompts user to select a new slow.
    """

    user_input = int(input("Select a free slot (number 1-9) on the game board to achive three in a row: "))
    if user_input >= 1 and user_input <= 9 and (game_board[user_input - 1] != "X" or game_board[user_input - 1] != "O"):
        game_board[user_input - 1] = player
    else:
        print("Try again")

#winner?

def check_winner(game_board):
    #check horizontal win condition
    if game_board[0] == game_board[1] == game_board[2]\
    and game_board[0] != "-":
        print(f"{game_board[0]} is the winner!!")
        run_game = False
    elif game_board[3] == game_board[4] == game_board[5] and game_board[3] != "-":
        print(f"{game_board[3]} is the winner!!")
        run_game = False
    elif game_board[6] == game_board[7] == game_board[8] and game_board[6] != "-":  
        print(f"{game_board[6]} is the winner!!")
        run_game = False

    #check vertical win condition
    if game_board[0] == game_board[2] == game_board[6] \
    and game_board[0] != "-":
        print(f"{game_board[0]} is the winner!!")
        run_game = False
    elif game_board[1] == game_board[3] == game_board[6] \
    and game_board[1] != "-":
        print(f"{game_board[1]} is the winner!!")
        run_game = False
    elif game_board[2] == game_board[5] == game_board[8] \
    and game_board[2] != "-":  
        print(f"{game_board[2]} is the winner!!")
        run_game = False

    #check diagnoal win condition
    if game_board[0] == game_board[4] == game_board[8] \
    and game_board[0] != "-":
        print(f"{game_board[0]} is the winner!!")
        run_game = False
    elif game_board[2] == game_board[4] == game_board[6] \
    and game_board[2] != "-":
        print(f"{game_board[2]} is the winner!!")
        run_game = False
        

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

def main():
    run_game = True
    while run_game:
    #select_player()
        display_board(game_board)
        user_input(game_board)
        print("Player is: ", player)
        print("Computer is:", computer)
        display_board(game_board)
        check_winner(game_board)
        computer_turn()
        check_winner(game_board)

main()