# This code plays hangman

# Stores the word to be guessed
secretWord = input("What is the secret word?:  ")

# Stores the amount of correct letters guessed
letterCount = 0

# Stores the letters that have been guessed
alreadyGuessed = []

# Iterates until the user has guessed all letters of the word
while True:

	# Stores the letter guessed each round
	guess = input("Enter your guess letter:  ")

	# If the letter has already been guessed, the loop restarts
	if guess in alreadyGuessed:
		print("You already guessed that!")
		continue

	# Updates the list of previously guessed letters
	alreadyGuessed.append(guess)

	# Stores the positions at which the guessed letter is a match
	matchKey = []

	# Iterates through all letters in the secret word to check for
	# matches with the letter that has been guessed
	for letter in range(len(secretWord)):
		if guess == secretWord[letter]:
			# Adds the position of the correct letter guess
			matchKey.append(letter)
			# Adds one to the amount of correct letters guessed
			letterCount += 1

	# If all the letters have been guessed, the game terminates
	if letterCount == len(secretWord):
			print("You got it! - '" + secretWord + "'")
			break
	
	# If there are no positions with a match, it lets the user know
	if len(matchKey) == 0:
		print("The letter '" + guess + "' is not in the word")

	# If there is more than one position with a match, it lets the 
	# user know the positions
	elif len(matchKey) != 1:
		holdStr = "The letter '" + guess + "' is in position " + str(matchKey[0])
		for position in range(len(matchKey)-1):
			holdStr += (" and " +str(matchKey[position+1]))
		print(holdStr)

	# If there is one position with a match, it lets the user 
	# know the position		
	else:
		print("The letter '" + guess + "' is in position " + str(matchKey[0]))
		