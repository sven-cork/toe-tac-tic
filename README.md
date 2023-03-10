# Toe Tac Tic

Play the classic Tic Tac Toe game against the computer scoring by entering your symbol three times in a row: horizontal, vertical or diagonal.
This is project module 3 of Code Institute Full Stack Developer course, focusing on Python and Terminal based GUI.

![Screenshot of game board](/assets/images/game_board.png)

## Table of contents

- [UI/UX](#ui/ux)
  - [Features](#features)
    - [Logo with Start Screen](#logo-with-start-screen)
    - [Gameboard](#gameboard)
    - [Results](#results)
    - [Play again](#play-again)
    - [Exit game](#exit-game)

- [User stories](#user-stories)
- [Colorscheme](#colorscheme)
- [Game Logic/Flowchart](#game-logic/flowchart)
- [Technologies Used](#technologies-used)
  - [Languages](#languages)
  - [Modules](#modules)
- [Development Environment, Version Control and Deployment/Storage](#custom-names)
- [Testing](#testing)
- [Validation](#validation)
  - [PEP8](#pep8)
- [Deployment](#deployment)
  - [Forking with GitHub](#forking-with-github)
  - [Cloning with GitHub](#cloning-with-github)
  - [Deploying with Heroku](#deploying-with-heroku)
- [Future implementations](#future-implementations)
- [Credits](#credits)

## UI/UX

- ### Features
  - #### Logo With Start Screen
    - Upon starting the game the user is greeted with a game board picture and the start screen as below:

  ![Screenshot of start screen](/assets/images/welcome.png) 

  - #### Gameboard
    - 9 slots, initially empty.
    - Each empty slot represented by dash character.
    - Each turn the player and computer chooses to place their character in an empty slot.
    - Three characters in a row results in a win.

  ![Screenshot of results area](/assets/images/default_gameboard.png) 

  - #### Results
    - Upon scoring three characters in a row the winner character is displayed.
  
  ![Screenshot of winning condition](/assets/images/winner_streak.png) 

    - Game score is displayed below with the total score for player and computer
      from starting the first game.

  ![Screenshot of results area](/assets/images/results.png) 
 
  - #### Play again

    - Upon scoring a win the player is presented with an option to continue the game (y/n).

  ![Screenshot of option to continue game](/assets/images/continue_game.png)

  - #### Exit game
    - Player select 'n' to exit game.

  ![Screenshot exiting game](/assets/images/goodbye.png)


- ### User Stories
  - I would like a new visitor to experience or achive:
    - Start a new game quickly.
    - Understand the game mechanism. 
    - Keep track of the score.
    - Get a thrill competing against the computer.
    - Have the option to exit out of the game quickly.

- ### Colorscheme
    - Colorama was used to color winner message yellow.

    ![Screenshot of winner message](/assets/images/winner_message.png)

    - Alert message and gameboard is presented in red color.
    
    ![Screenshot of alert message](/assets/images/alert_message.png)


- ### Game Logic/Flowchart
  ![Flowchart image](/assets/images/flowchart.png)

## Technologies Used
  ### Languages
  - Toe Tac Tic was written in Python.

  ### Modules
  - [Termcolor:](https://pypi.org/project/termcolor/) was used to color the gameboard.
  - [Random:](https://docs.python.org/3/library/random.html) was used to generate random number for computer.
  - [Time](https://docs.python.org/3/library/time.html) was used to pause the Terminal before clearing the window.
  - [Sys](https://docs.python.org/3/library/sys.html) was used to enable a typewriter effect printing intro/exit message in Terminal.
  - [Os](https://docs.python.org/3/library/os.html) two modules were imported ("system and "name") and used to enable a typewriter effect printing intro/exit message in Terminal.
 
  ### <a name="custom-names"></a>Development Environment, Version Control and Deployment/Storage

  - [Gitpod:](https://gitpod.io/workspaces) - was used for writing the game code and deploy to GitHub
  - [GitHub:](https://github.com/) - was used for hosting the program source code and supporting files
  - [Heroku:](https://github.com/) - was used for deployment and visualising the program in a web based Terminal app
  - [Lucidchart:](https://www.lucidchart.com/) - was used for creating the flowchart
  - [Pep8:](https://pep8ci.herokuapp.com/) - was used to test the program python code for errors or fomatting issues

## Testing

Manual testing was carried out for character input and win conditions:

 |    Feature Tested        |      Expected Result                     |        Actual Result       |        Pass/Fail           |  
 |:-------------------------|:---------------------------------------- |:---------------------------|:---------------------------|                               
 | Character input to select team|Only "X" or "O" accepted characters.| Any other character entered other than "X" or "O" prompts to re-enter character.    |        Pass                |
  | Character input to select team corrects for lower case letter entered.| Lower case letter "x" or "o" are accepted. | Lower case letter "x" or "o" are accepted.  |        Pass                |
  | Slot number entered occupied or beyond range 1-9. | Only empty slots (-) and within range 1-9 are selectable. | Non-empty slot or out of range selection (1-9) prompts to re-select slot.   |        Pass                |
  | Player horizontal win (3 possible horizontal rows for win). | Any same character occupying any of the 3 horizontal rows results in win. | Works as expected.  |        Pass                |
  | Player vertical win (3 possible vertical columns for win). | Any same character occupying any of the 3 vertical columns results in win. |    Works as expected. |       Pass              |
  | Player diagonal win (2 possible diagonals for win). |  Any same character occupying any of the 2 diagonals results in win.   |       Works as expected.              |     Pass |
  | Draw condition where all slots are occupied however where none of the win conditions were triggered. |   Draw condition triggered presenting a draw message and offered to play again.   |       Works as expected.              |     Pass |
  

## Validation

### PEP8
- [PEP8 CI](https://pep8ci.herokuapp.com/) was used to program syntax and formatting. All Python code passed as below:
![PEP8 CI result for Toe Tac Tic](/assets/images/pep8.png)

## Deployment

### Forking with GitHub
1. Open [GitHub](https://github.com).
2. Navigate to the intended repository.
3. Select "Fork" in the top rigth corner of the page.
4. Select the owner of the fork repository in the drop menu provided.
5. Select the "Create Fork" button.
6. Your copy of the original repository has been created.

### Cloning with GitHub
1. Open [GitHub](https://github.com).
2. Navigate to the intended repository.
3. Select the "Code" button on the top of the repository page.
4. Select the copy button for one of the three options: "HTTPS", "SSH" or "GitHub CLI".
5. Open Terminal (or command line tool) on your local computer.
6. In Terminal change the current working directory to the directory where the clone will reside.
7. In Terminal type: "git clone" followed by a space. Paste the URL copied in (step 4.).
8. In Terminal press "Enter"/"Return" to create a local copy of the repository on your computer.

### Deploying with Heroku
1. From your GitPod workspace, copy the entire content of creds.json file. This will be needed in step 6.
2. Create an account with [Heroku](https://heroku.com) and sign in.
3. Open Heroku Dashboard and select "Create a new app" button.
4. Give the app a unique name and select "Create app".
5. To apply settings select the "Settings" button.
6. Select "Reveal Config Vars".
7. In the "Keys" field enter "CREDS".
8. In the "Value" field paste the content of creds.json (step 1.). Select "Add".
9. In the second "Value" field enter "PORT". In the corresponding "Value" field enter "8000".
7. From the "Buildpacks" section select "Add buildpack". Add python and nodejs and ensure the resulting order
is listed 'heroku/python' followed by 'heroku/nodejs'. 
8. From the 'Deployment' tab select "GitHub" in the "Deployment method" section. Select "Connect to GitHub" at the bottom of the page.
9. In the search field search for your GitHub repository name.
10. Select "Connect" to link up with the GitHub repository.
11. Further down the page select deployment method automatic ("Enable Automatic Deploys") or manual ("Deploy branch").

## Future implementations
- To control the position of the game in the Terminal window I am exploring curses with Python.

## Credits

### Code
- Inspiration for gameboard design was taken from [Code Coach](https://www.youtube.com/watch?v=dK6gJw4-NCo&list=PLzoTxk8WON8ZgLPBK9YYZlHoJzm0QUR8F&index=1&ab_channel=CodeCoach) YouTube channel.

- Code to generate a typewriter effect was borrowed from this [Stackoverflow](https://stackoverflow.com/questions/20302331/typing-effect-in-python) thread.

- Code to clear screen was borrowed from this [geeksforgeeks](https://www.geeksforgeeks.org/clear-screen-python/) article. 


### Special thanks

- To my mentor Ronan McClelland giving feedback of using curses to control Terminal positioning. For the next project this will
be implemented however in general for development this will come very handy.

- To Code Institue tutor Martin for suggesting a clear method with sleep delay as an alternative to curses.




