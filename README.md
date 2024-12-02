# __The Hangman Game__

#### Video Demo: <https://youtu.be/v0Mjbqotm-A?si=gmvfev2Kw6dM1GJL>
---

### __Description:__
 This is The Hangman Game. The player need to guess six-letter word. There are 50 different words 2 for every English alphabet letter except X, and thier meanings from Cambridge Online Dictionary.

 There are three difficulty levels in this game - easy, mid and hard. They need to be entered as sys argument. If there is no argument, the - mid level will be used by default.

 There is a difference between the levels. At "easy" level, the player receive a hint as soon as they start the game. At "mid" level, they receive a hint only after two unsuccessful guesses. At "hard", the player do not receive a hint  at all.


### __Project structure:__
 - `project.py` - conains Python code;
 - `test_project.py`- contains functions for PyTest;
 - `project_words.csv` - contains words and their meanings;
 - `deadman_0.txt` - illustration for game;
 - `deadman_1.txt` - illustration for game;
 - `deadman_2.txt` - illustration for game;
 - `deadman_3.txt` - illustration for game;
 - `README.md`

### __Libraries:__
 - _Random_ - This library selects a random word to play with.
 - _Sys_ - This library is used to determine the difficulty level when starting the game.
 - _Csv_ - This library is needed in this case to get words and their definitions from csv-file.

 ## __Usage:__

Here is one of possible scenarios.

```python project.py```

```
______
Letter: a
_a__a_
Letter: e
  _____________
  |            |
  |
  |
  |
  |
  |
  |
  |
--------------
Letter: s
_a_sa_
Letter:
You should input one English letter
Letter: r
  _____________
  |            |
  |          (-.-)
  |            -
  |            |
  |            |
  |
  |
  |
--------------
Hint: A pleasant-smelling substance used as the base for medical or beauty treatments.
Letter: b
ba_sa_
Letter: l
balsa_
Letter: m
You won! :)
The word: balsam
```

And let's look at "easy" level and losing.

``` python project.py easy```
```
Hint: A pleasant-smelling substance used as the base for medical or beauty treatments.
______
Letter: i
  _____________
  |            |
  |
  |
  |
  |
  |
  |
  |
--------------
Letter: e
  _____________
  |            |
  |          (-.-)
  |            -
  |            |
  |            |
  |
  |
  |
--------------
Letter: t
  _____________
  |            |
  |          (-.-)
  |            -
  |          / | \
  |         /  |  \
  |
  |
  |
--------------
Letter: o
  _____________
  |            |
  |          (-.-)
  |            -
  |          / | \
  |         /  |  \
  |           /\
  |          /  \
  |
--------------
You lose it. :(
The word: balsam
```

## __Functions__

The project contains 9 functions and one of them is `main()`.

 - __`get_sys_argv()`__ - Gets sys argument and returns it in string format. Sets the defult value to "mid" if sys argument is missing.
 - __`get_level(level)`__ - Accepts a level value as a string and returns as an integer. _This function are tested by pytest._
 - __`get_all_words()`__ - Retrieves all words and their meanings from the csv-file and puts them in the global dictionary.
 - __`get_word()`__ - Returns a random word for the game.
 - __`guess(word,level)`__ - It takes the meaning of the word and the level of the game. Creates a list from a given word. Creates a list that will be shown to the player, initially consisting of six "_". The game value is created, which is initially True. There is also a hint flag for the middle level. A counter of incorrect guessing attempts is created. If the level is "easy", a hint will be shown there. In the game cycle, if " _" is still in the list that is being shown and the number of failed tries is below 4, the game is on, otherwise the game ends with a loss or victory. If the player is at an "mid" level and the number of failed attempts is 2, then a hint will be shown. It is suggested to enter a letter, if more than one letter of the English alphabet is entered, a message about it will be displayed. If the entered letter is in the word any number of times, each one will be displayed in a list that is shown to the player.
 - __`get_help(word)`__ - Returns a meaning of the given word from global dictionary.  _This function are tested by pytest._
 - __`is_it_letter(letter)`__ - Returns True if given letter is one English letter. Otherwise raise ValueError.  _This function are tested by pytest._
 - __`get_deadman(number_of_tries)`__ - Prints out illustrations in case of wrong letter.


### Made by `Tamarova Maria`
