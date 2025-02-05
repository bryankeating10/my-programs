secretWord = input("What is the secret word?:  ")
letterCount, alreadyGuessed = 0 , []
while True:
	guess = input("Enter your guess letter:  ")
	if guess in alreadyGuessed:
		print("You already guessed that!")
		continue
	alreadyGuessed.append(guess)
	matchKey = []
	for letter in range(len(secretWord)):
		if guess == secretWord[letter]:
			matchKey.append(letter)
			letterCount += 1
	if letterCount == len(secretWord):
			print("You got it! - '" + secretWord + "'")
			break
	if len(matchKey) == 0:
		print("The letter '" + guess + "' is not in the word")
	elif len(matchKey) != 1:
		holdStr = "The letter '" + guess + "' is in position " + str(matchKey[0])
		for position in range(len(matchKey)-1):
			holdStr += (" and " +str(matchKey[position+1]))
		print(holdStr)	
	else:
		print("The letter '" + guess + "' is in position " + str(matchKey[0]))