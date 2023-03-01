# Toe Tac Tic

Play the classic Tic Tac Toe game against the computer scoring by entering your symbol three times in a row: horizontal, vertical or diagonal.
This is project module 3 of Code Institute Full Stack Developer course, focusing on Python and Terminal based GUI.

![Screenshot of game board](/assets/images/game_board.png)

## Table of contents

- [Features](#features)
  - [Logo with Start Screen](#logo-with-start-screen)
  - [Gameboard](#gameboard-area)
  - [Results](#results)
  - [Play again](#play-again)
  - [Future Ideas](#future-ideas)

- [Design](#design)
- [Game Logic](#game-logic)
  - [Flowchart](#flowchart)
- [Technologies Utilised](#technologies-utilised)
- [Testing](#testing)
- [Validation](#validation)
  - PEP8
- [Deployment](#deployment)
  - [Forking](#forking)
- [Credits](#credits)

## Features

- ### Logo With Start Screen
  - Upon starting the game the user is greeted with a game board picture and the start screen as below:

  ![Screenshot of Le Crossword heading](/assets/images/crossword_heading.png) 

- ### Gameboard
  - 9 slots, initially empty.
  - Each empty slot represented by dash character.
  - Each turn the player and computer chooses to place their character in an empty slot.
  - Three characters in a row results in a win.

  ![Screenshot of results area](/assets/images/default_gameboard.png) 

- ### Results
  - Upon scoring three characters in a row the winner character is displayed.
  - Game score is displayed below with the total score for player and computer
  from starting the first game

  ![Screenshot of results area](/assets/images/results.png) 
 
- ### Play again
  - Upon scoring a win the player is presented with an option to continue the game (y/n).

  ![Screenshot of option to continue game](/assets/images/continue_game.png)

- ### Footer
  - The footer contains social media links for Facebook, Twitter and Instagram.
  - The links are stylised icons from Font Awesome.
  
  ![Screenshot of Footer Area](/assets/images/footer.png)

- ### Future Ideas
  - The option of playing a few different crosswords, perhaps toggling between easy, medium and hard.
  - Best of scoreboard offering user to enter name at start of game.
        
## Design
  - Courier New was chosen for header font style as this I believe evokes a sense of classic old newspapper.
  - The hero image has few colors and the wooden tiles provides a dominant earthy tone against which the crossword area is well balanced.
  - Considering the crossword area is busy with 25 tiles, the rest of the website is kept minimalistic with mostly dark or white colors and I belive this achieves a nice harmony for the overall impression.

## Game Logic
  - ### Flowchart
  ![Flowchart image](/assets/images/flowchart.png)


## Technologies Utilised

- [Fontawesome](https://fontawesome.com/) was used for green check marks, red "x" marks and social media icons in the Footer.
- Preview.app for macOS was used to re-size images used with Love Art.
- [GitPod](https://gitpod.io/) was used to code HTML, CSS and.


## Testing

Manual testing was carried out for character input and win conditions:

 |    Feature Tested        |      Expected Result                     |        Actual Result       |        Pass/Fail           |  
 |:-------------------------|:---------------------------------------- |:---------------------------|:---------------------------|                               
 | Character input to select team|Only "X" or "O" accepted characters| Any other character entered other than "X" or "O" prompts to re-enter character    |        Pass                |
  | Character input to select team corrects for lower case letter entered|Lower case letter "x" or "o" are accepted| Lower case letter "x" or "o" are accepted  |        Pass                |
  | Slot number entered occupied or beyond range 1-9 | Only empty slots (-) and within range 1-9 are selectable | Non-empty slot or out of range selection (1-9) prompts to re-select slot   |        Pass                |
  | Player horizontal win (3 possible horizontal rows for win) | Any same character occupying any of the 3 horizontal rows results in win| Works as expected  |        Pass                |
  | Player vertical win (3 possible vertical columns for win)| Any same character occupying any of the 3 vertical columns results in win |    Works as expected |       Pass              |
  | Player diagonal win (2 possible diagonals for win) |  Any same character occupying any of the 2 diagonals results in win   |       Works as expected.              |     Pass
  
--------------------------------------------------------------------------------------

Testing Le Crossword for different devices using Google Developer tools

|    Device        |      Result                     |
|:-----------------|:--------------------------------|
|  iPhone 12 Pro   |      Works as expected          |
|  iPhone SE       |      Works as expected          |
|  Samsung Galaxy A51/71       |      Works as expected          |
|  iPad Air     |      Works as expected, however crossword area could be made larger|
|  Surface Pro 7    |      Works as expected, however in portrait mode the content is pushed on the top of the display|
|  Next Hub   |      Works as expected|

--------------------------------------------------------------------------------------

Browser Testing

|    Browser (version)       |      Result                     |
|:-----------------|:--------------------------------|
|  Google Chrome (108.0.5359.124)  |      Works as expected          |
|  Safari (15.6.1)       |      Works as expected          |
|  Firefox (107.0.1)       |      Works as expected          |

--------------------------------------------------------------------------------------


## Validation

### HTML Validation
- [W3 HTML Checker](https://validator.w3.org/nu/#textarea) was used to test HTML validation. The website passed as per below screenshot.

<details>

<summary>HTML validation for html.index/</summary>

![W3 HTML Checker result for index.html](/assets/images/html_check.png)

</details>

### CSS Validation

- [W3 CSS Checker](https://jigsaw.w3.org/css-validator/) was used to test CSS validation. The website passed as per below screenshot.

<details>

<summary>CSS Checker for style.css</summary>

![W3 CSS Checker result for style.css](/assets/images/css_validation.png)

</details>

### JavaScript Validation
JavaScript validation was performed using [JSHint](https://jshint.com/) and the following results were returned:
 - No errors were found.
 - There are 7 functions in the script.js file.
 - The function with the largest signature takes 2 arguments, while the median is 0.
 - There are 92 statements in the largest function, while the median is 2.
 - The most complex function has a cyclomatic complexity value of 46, while the median is 1.

## Performance/Accessibility 

Google Chrome Developer Tools Lighthouse feature was used to test Performance and Accessibility. 
For both desktop and mobile versions of Lighthouse a score over 90% were achieved for all metrics. 


### Lighthouse Desktop version test outcome

<details>
<summary>Desktop Performance</summary>

![Chrome Dev Tools Lighthouse output](/assets/images/desktop_performance.png)

</details>

### Lighthouse Mobile version test outcome

<details>
<summary>Mobile Performance</summary>

![Chrome Dev Tools Lighthouse output](/assets/images/mobile_performance.png)

</details>


## Deployment

### Forking
1. Open [GitHub](https://github.com).
2. Navigate to the intended repository.
3. Select "Fork" in the top rigth corner of the page.
4. Select the owner of the fork repository in the drop menu provided.
5. Select the "Create Fork" button.
6. Your copy of the original repository has been created.


## Credits

### Images

Hero image aquired from [Pexels](#pexels.com):
 - crossword2.jpg (original name: pexels-brett-jordan-5908695.jpg) - by Brett Jordan


### Code
- JavaScript code for arrow function locating items by class borrowed from the website listed below. This code snippet added functionality to the reset button by locating all elements with a green check or red "X" mark in order for them to be removed:
https://codingbeautydev.com/blog/javascript-remove-class-from-multiple-elements/
- Code snippet from line 275 to 278 in scripts.js.


### Other

Icons for social media links are from [Fontawesome](https://fontawesome.com/).

Inspiration for the crossword format and clues (original clue text changed for this project) was borrowed from James Scalise [YouTube channel:](https://www.youtube.com/watch?v=_KunjDXYYYg&ab_channel=JamesScalise).


