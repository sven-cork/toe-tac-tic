import random
import sys
import time
from os import system, name
from time import sleep
from termcolor import colored

computer_score = 0
player_score = 0
player = ""
computer = ""

game_board = ["-", "-", "-",
              "-", "-", "-",
              "-", "-", "-"]

game_logo = """
            +---+---+---+
            | X | - | - |
            +---+---+---+
            | - | X | - |
            +---+---+---+
            | O | - | O |
            +---+---+---+
            """

intro_message = colored("""Welcome to Toe-Tac-Tic.
Choose your character and hit those three slots in a row
to beat the computer!!""", "cyan")


def select_player():
    """
    Allows player to select team character 'X' or 'O'.
    """
    global player
    global computer

    warning_message = "Incorrect option, select either 'X' or 'O'"

    player = ""
    while True:
        print("\n")
        player = input("\nPlayer select team 'X' or 'O':\n").upper()
        if player == "X" or player == "O":
            break
        else:
            print(colored(warning_message, "red"))

    computer = ""
    if player == "X":
        computer = "O"
    else:
        computer = "X"


def typewriter_effect(string):
    """
    Typewriter effect (each character delayed) for text printed to Terminal.
    """

    for character in string:
        time.sleep(.08)
        sys.stdout.write(character)
        sys.stdout.flush()


def screen_cleared():
    """
    Pauses and clears the screen after specified amount of seconds.
    """

    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def display_board(game_board):
    """
    Prints gameboard
    """

    print("\n")
    print(colored("+---+---+---+", "red"))
    print(colored("| ", 'red') + game_board[0] + colored(" | ", "red")
          + game_board[1] + colored(" | ", "red") + game_board[2]
          + colored(" | ", "red"))
    print(colored("+---+---+---+", "red"))
    print(colored("| ", 'red') + game_board[3] + colored(" | ", "red")
          + game_board[4] + colored(" | ", "red") + game_board[5]
          + colored(" | ", "red"))
    print(colored("+---+---+---+", "red"))
    print(colored("| ", 'red') + game_board[6] + colored(" | ", "red")
          + game_board[7] + colored(" | ", "red") + game_board[8]
          + colored(" | ", "red"))
    print(colored("+---+---+---+", "red"))


def user_input(game_board):
    """
    User selects slot to place X or O. Checks if slot already taken and if so
    prompts user to select a new slow.
    """

    global player
    while True:
        print("\n")

        try:
            user_input = int(input("Select a slot (1-9) on the gameboard:\n"))
            if (user_input >= 1 and user_input <= 9 and
               (game_board[user_input - 1] == "-")):
                game_board[user_input - 1] = player
                break
            else:
                display_board(game_board)
                print(colored("\nSlot already taken or \
invalid number, try again!", "red"))
        except Exception:
            display_board(game_board)
            print(colored("Incorrect character entered, try again!", "red"))


def update_score(winner_character):
    """Keeps track of wins for player or computer until game is quit"""

    global player
    global computer
    global player_score
    global computer_score

    new_line = "\n"

    if winner_character == player:
        player_score += 1
    else:
        computer_score += 1

    print("\n")
    print(f"Player score: {player_score}")
    print(f"Computer score: {computer_score}")


def check_character_to_winner(slot_character):
    """
    checks if winner is player or computer and return a string
    either 'player' or 'computer
    """

    if slot_character == player:
        return "player"
    else:
        return "computer"


def check_winner(game_board):
    """
    Checks winner if three of the same characters (X or O) have been
    selected either horizontaly, vertically or diagonaly
    """

    display_board(game_board)

    new_line = '\n'
    winner_message = colored("is the winner!!", "yellow")

    # check horizontal win condition
    if (game_board[0] == game_board[1] == game_board[2] and
            game_board[0] != "-"):
        winner = check_character_to_winner(game_board[0])
        print(f"{new_line}{game_board[0]} ({winner})", winner_message)
        update_score(game_board[0])
        play_again()
    elif (game_board[3] == game_board[4] == game_board[5] and
            game_board[3] != "-"):
        winner = check_character_to_winner(game_board[3])
        print(f"{new_line}{game_board[3]} ({winner})", winner_message)
        update_score(game_board[3])
        play_again()

    elif (game_board[6] == game_board[7] == game_board[8] and
            game_board[6] != "-"):
        winner = check_character_to_winner(game_board[6])
        print(f"{new_line}{game_board[6]} ({winner})", winner_message)
        update_score(game_board[6])
        play_again()

    # check vertical win condition
    elif (game_board[0] == game_board[3] == game_board[6] and
            game_board[0] != "-"):
        winner = check_character_to_winner(game_board[0])
        print(f"{new_line}{game_board[0]} ({winner})", winner_message)
        update_score(game_board[0])
        play_again()

    elif (game_board[1] == game_board[4] == game_board[7] and
            game_board[1] != "-"):
        winner = check_character_to_winner(game_board[1])
        print(f"{new_line}{game_board[1]} ({winner})", winner_message)
        update_score(game_board[1])
        play_again()

    elif (game_board[2] == game_board[5] == game_board[8] and
            game_board[2] != "-"):
        winner = check_character_to_winner(game_board[2])
        print(f"{new_line}{game_board[2]} ({winner})", winner_message)
        update_score(game_board[2])
        play_again()

    # check diagnoal win condition
    elif (game_board[0] == game_board[4] == game_board[8] and
            game_board[0] != "-"):
        winner = check_character_to_winner(game_board[0])
        print(f"{new_line}{game_board[0]} ({winner})", winner_message)
        update_score(game_board[0])
        play_again()

    elif (game_board[2] == game_board[4] == game_board[6] and
            game_board[2] != "-"):
        winner = check_character_to_winner(game_board[2])
        print(f"{new_line}{game_board[2]} ({winner})", winner_message)
        update_score(game_board[2])
        play_again()

    if game_board.count("-") == 0:
        print("\n")
        print("This round was a draw, no winner")
        play_again()


def computer_turn():
    """
    Computer turn based on random generated number
    applied to non occupied gameboard slot
    """

    while True:
        random_number = random.randint(1, 9)
        if (game_board[random_number - 1] != "X"
                and game_board[random_number - 1] != "O"):
            game_board[random_number - 1] = computer
            display_board(game_board)
            break


def play_again():
    """
    Offer player to play again while correcting for lowercase
    and invalid letters.
    """
    global game_board
    global player_score
    global computer_score

    play_again_selection = ""

    while True:
        play_again_selection = input("\nWould you like to \
continue, 'Yes' or 'No' (Y/N):\n").upper()
        if play_again_selection == "Y" or play_again_selection == "N":
            break
        else:
            print(colored("Enter valid string 'Y' or 'N'", "red"))

    if play_again_selection == "Y":

        sleep(0.5)
        screen_cleared()

        game_board = ["-", "-", "-",
                      "-", "-", "-",
                      "-", "-", "-"]
        print("\nPlayer score: ", player_score,
              "\nComputer score:", computer_score)
        main()

    else:
        print("\n")
        sleep(0.5)
        screen_cleared()
        typewriter_effect(colored("Goodbye Player...\n", "cyan"))
        print("\n")
        quit()


def main():
    """
    Game main function running all sub functions
    """

    run_game = True
    while run_game:
        display_board(game_board)
        user_input(game_board)
        sleep(0.5)
        screen_cleared()
        check_winner(game_board)
        sleep(0.5)
        screen_cleared()
        computer_turn()
        check_winner(game_board)
        sleep(0.5)
        screen_cleared()


print(game_logo)
typewriter_effect(intro_message)
select_player()
sleep(1)
screen_cleared()
main()
