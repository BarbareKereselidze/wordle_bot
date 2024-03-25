# wordle_bot

This is a Python implementation and a bot of the popular word-guessing game Wordle. 
The game provides feedback on each guess, indicating which letters are correct, which are in the wrong position, 
and which are not in the solution at all. The player has six attempts to guess the correct word. 
If the player wants help with the guesses, they should type "bot", which will automatically guess the next 
most probable guess based on left guesses and their letter frequencies.


## Notes:

* The answer gets automatically retrieved from the Mashable website by parsing the page.
* The player can make a guess on their own as well as let the bot make a guess for them <br>
  If you are stuck write "bot" in the input. 
* Bot guesses are based on the Wordle guess list and not the allowed word list. <br>
  However, the user can make a guess from the allowed guess list just like in real Wordle. 
* The repository provides both the allowed guess list and answer guess lists in txt formats in alphabetical order. 

## How To Use:

* Make sure to install the required modules listed in requirements.txt:
```
   pip install -r requirements.txt
   ```
* Update the configuration details in config.ini before executing the scripts.

## Example Gameplay:

The color scheme of the outputs when you run the code will be similar to the original wordle: 
* green indicates a correct letter in the correct position
* yellow indicates a correct letter in the wrong position
* red indicates an incorrect letter

```
Attempt 1/6: apple
APPLE
Attempt 2/6: bot
SULLY
Attempt 3/6: bot
BUILT
Attempt 4/6: build
BUILD
Congratulations! ٩̋(ˊ•͈ ꇴ •͈ˋ)و
```
