
"""
word = "hello"
print(word.index("l"))




guess_word = "bryan"
correct_letters = 0
already_guessed = []


while correct_letters < len(guess_word):
	guess_letter = input("Guess a letter: ")
	
	if guess_letter in already_guessed:
		continue

	already_guessed.append(guess_letter)

	for letter in range(len(guess_word)):
		if guess_letter == guess_word[letter]:
			print(guess_word[letter] + " is in position " + str(letter))
			correct_letters += 1
"""
"""
test_list = []
test_list.append(5)
print(test_list)
test_list.append(6)
print(test_list)

second_test = [6,7,8,9]
print(second_test)
second_test.append(10)
print(second_test)


already_guessed = []

already_guessed.append("b")
already_guessed.append("o")
print(already_guessed)

print("b" in already_guessed)
print("l" in already_guessed)

"""
"""

for owen in range(4):
	print(owen + 1)

myList = ["bryan", "emma", "owen"]

for person in myList:
	print(person)

evens = [0,2,4,6,8]

for number in evens:
	print(number)
"""

animal_list = ["bear","cat","dog"]
fruit_list = ["apple","pear","banana"]

def fruitOrAnimal(word):
	if word in animal_list:
		print("Animal")
	if word in fruit_list:
		print("Fruit")

user_done = False

while not user_done:
	inWord = input("Word: ")
	if inWord == "done":
		user_done = True
	else:
		fruitOrAnimal(inWord)