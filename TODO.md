#### 1. Save Feature
##### - For now, it would save the latest game semi-automatically.
#### 2. Game Play Feature
~~2.0 Frontend~~
##### 2.1 Game Scoring Feature 
##### 2.1.1 Correct Calculations
##### 2.2 Random Word Assignment Feature
##### 2.3 Turn Passing Feature(With Submit Button)
	- Currently turn can be passed, but random word assignment has not been implemented yet.
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

	2nd Refactor (May 25th - Current)
	- Remove 'currentLetters' in gameData.json and replace with player1Letters and player2Letters
	- Modify the letter erasing function.

