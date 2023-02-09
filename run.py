game_board = [1, 2, 3,
              4, 5, 6,
              7, 8, 9]

print(game_board)


#global variables:
#game_board
#player?

#functions:
#select_player
#select slot on board and update board
#winner
#computer turn
#winner

#select_player
def select_player():

    """
    Let player select team "X" or "O". Checks if either of the valid teams (characters) have been selected and corrects for lower case entered character."
    """

    player = ""

    while True: 
        player = input("Player select team 'X' or 'O': ").upper()
        if player == "X" or player == "O":
            break
    print(player)
    return player
    

#select slot on board and update board
def user_input(game_board):
    """
    User selects slot to place X or O. Checks if slot already taken and if so 
    prompts user to select a new slow.
    """

    user_input = int(input("Select a free slot (number 1-9) on the game board to achive three in a row: "))
    if user_input >= 1 and user_input <= 9 and game_board[user_input] != "-":
        game_board[user_input] = player

#winner?

def check_winner(game_board):
    #check horizontal win condition
    if game_board[0] == game_board[1] == game_board[2] and game_board[0] != "-":
        return game_board[0]
    elif game_board[3] == game_board[4] == game_board[5] and game_board[3] != "-":
        return game_board[2]
    elif game_board[6] == game_board[7] == game_board[8] and game_board[6] != "-":  
        return game_board[6]

    #check vertical win condition
    if game_board[0] == game_board[2] == game_board[6] and game_board[0] != "-":
        return game_board[0]
    elif game_board[1] == game_board[3] == game_board[6] and game_board[1] != "-":
        return game_board[1]
    elif game_board[2] == game_board[5] == game_board[8] and game_board[2] != "-":  
        return game_board[2]

    #check diagnoal win condition
    if game_board[0] == game_board[4] == game_board[7] and game_board[0] != "-":
        return game_board[0]
    elif game_board[2] == game_board[4] == game_board[6] and game_board[2] != "-":
        return game_board[2]


select_player()
user_input(game_board)
check_winner(game_board)