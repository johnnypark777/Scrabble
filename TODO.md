#### 1. Save Feature
##### - For now, it would save the latest game semi-automatically.
##### 1.1 Create gameData.json when there is no such file found. 
#### 2. Game Play Feature
~~ 2.0 Frontend ~~
~~ 2.1 Game Scoring Feature ~~
~~ 2.1.1 Correct Calculations ~~
#### 2.2 Random Word Assignment Feature 
~~ 2.2.1 Correct Word Assignment ~~
###### (** #1 Priority after 3rd refactor **) 2.2.2 Better random letter distribution
~~ 2.3 Turn Passing Feature(With Submit Button) ~~
#### 3. Settings Modification Feature
#### 4. Main Menu Feature


### Refactor Log
	1st Refactor (May 18th - May 24th)
	- Change the saved data format from .py to .json
		Combine the displayCurrentLetters and displayCurrentScores function
	- Name Changes
		1. Change the name from 'boardSetup' function to 'setTileDisplay' function
		2. Change the global variable prevX and prevY to selectedX and selectedY
	 - Change the letter type from char to dict and store not only the letter but also score and multiplier
		1. Change the char array 'usedLetters' to dict array
		 	1.1 Change the save method for usedLetters array
			1.2 Change the load method for usedLetters array

	2nd Refactor (May 25th - July 4th)
	- Remove 'currentLetters' in gameData.json and replace with player1Letters and player2Letters
	- Modify the letter erasing function(Only erasing what is allowed to erase). 
		1. Assign Random letters(for now instead of making it as text input) when a player has less than 7 tiles. 
		2. Correct Word Assignments (TODO List 2.2.1) 
	- Simplify and increase the readability of the 'keyChar' function 
	- Correct Scoring Calculations (TODO List 2.1.1 -> 2.1) (** CURRENT **)
		1. Convert 'boardLetter' data from 1D to 2D. 

	Beta (Scrabble 2.0) (July 7th - Current)
	- Until further bugs found, will focus on this refactor before adding more features.  
	- Combine all player specific variables (Ex. player1Letters, player2Letters, player1Turn, player2Turn, etc)
	- Implement MVC model
		1. Implement word update
		2. Implement erase feature - done
	


###Bug Report
	- User can replace the words that are not allowed (backspace is fine) 
		- Current State: Fixed
		- Fixed by returning the function when word is pressed but is not allowed to change the default word

