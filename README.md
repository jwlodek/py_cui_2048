# py_cui-2048 [![Downloads](https://pepy.tech/badge/py-cui-2048)](https://pepy.tech/project/py-cui-2048)

A CUI (command line user interface) version of the 2048 game written with the help of the [py_cui](https://github.com/jwlodek/py_cui) library.

### Installation

To install `py_cui_2048`, use pip:
```
pip install py-cui-2048
```
(You should be able to also use `py_cui_2048` to install with pip.)  
Then, to run the game, use:
```
py2048
```
note that the `py2048` cli script must be installed by pip into your system path. (You should see a warning spawned by pip if this is not the case.)

### Playing the Game
<p align="center">
    <img src="docs/assets/py2048-demo.gif">
</p>

When starting a game, you can control the board actions with WASD, and the arrow keys/Enter control the menu. The rules are identical to classic 2048, meaning that same-value tiles will combine when pushed against each other. You can undo one move, as well as redo the undid move, but only one at a time.

You can also create a new game or exit. 

To win, you wish to combine tiles until you get a tile that has a value of 2048. You receive a game over message if there are no more legal moves remaining.

A typical game strategy involves placing the largest square in a corner, and ensuring that it stays there while other tiles are moved around it.

### Contributing

I would like to add support for larger board sizes, as well as custom games, and saving/loading games. If you feel that you would like to contribute this feature to the game, please feel free to fork + pull request, and as long as the changes work, I will merge them in!

### License

BSD 3-Clause License

Copyright (c) 2019-2020, Jakub Wlodek