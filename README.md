# chess

The aim of the work was to develop a classic desktop application for playing chess and implement an integrated chess engine that allows playing games against the computer. The impact of using selected methods of optimizing state space search on the algorithm's efficiency was investigated.

## Main menu
After launching the program, the main menu is displayed, allowing the user to switch between different application panels. The user can choose to play a game, start a new analysis, change application settings, or exit the program. The user can return to the main menu from any application panel.

## Playing with engine
During the game, the user makes moves by clicking on the selected squares on the chessboard. The information on the side panel is continuously updated during the game. At any time, the user can export the ongoing game to a PGN file by clicking the appropriate button and selecting the location to save it in a designated system window. The chessboard is appropriately rotated depending on the side playing the game.

![Game](https://github.com/kzarnowski/chess/blob/main/showcase/game.gif)

## Game analysis
In the analysis mode, the most important element of the interface is the button to import a game from a PGN file. After loading the game, information about the players, result, and location and time of the game is displayed at the top. The user can navigate through the game forward and backward using the arrows at the bottom.

![Analysis](https://github.com/kzarnowski/chess/blob/main/showcase/analysis.gif)

## Settings
Users can customize the application to their needs in the settings panel. They can choose the side for playing the game, change the graphical theme of the chessboard, and adjust the engine level. There are also advanced parameters available to enable or disable optimization methods for searching game tree. Each group has a default option set initially. A graphical representation is also provided, showing a brief explanation of how each piece moves, as well as a link to a full description of the rules.

![Settings](https://github.com/kzarnowski/chess/blob/main/showcase/settings.jpg)