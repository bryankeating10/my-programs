# This is my second attempt at making an algorithm that automatically
# tells people who they are paying or getting from, and how much from
# each person. This diverges from the first attempt by using a built in
# sort function to order the players by end of night balance

class Player(object):
	def __init__(self, name, buyIn):
		self.name = name
		self.balance = -buyIn
		self.payable = {}
		self.recievable = {}
		self.stillNeedsToPay = 0
		self.stillNeedsToRecieve = 0

	def rebuy(self,amount):
		self.balance -= amount
	def cashout(self,amount):
		self.balance += amount

	def isWinner(self):
		self.stillNeedsToRecieve = self.balance
	def isLoser(self):
		self.stillNeedsToPay = self.balance
	
print()

# Players and Buy In
BRYAN = Player("Bryan",200)
RJ = Player("RJ",900)
PJ = Player("PJ",450)
LOU = Player("Lou",140)
CAM = Player("Cam",300)
KYLE = Player("Kyle",150)
JOE = Player("Joe",200)
MATT = Player("Matt",200)
HEN = Player("Hen",500)
AIDEN = Player("Aiden",668)
KEVIN = Player("Kevin",99)

# List of Players
players = [BRYAN,LOU,RJ,PJ,CAM,KYLE,JOE,MATT,HEN,AIDEN,KEVIN]

# Actions of existing players
BRYAN.cashout(200)
RJ.cashout(900)
LOU.cashout(140)
CAM.cashout(300)
KEVIN.cashout(150)
PJ.cashout(450)
KYLE.cashout(415)
JOE.cashout(815)
MATT.cashout(150)
HEN.cashout(287)

# Total balance should equal zero
total = 0
for player in players:
	total += player.balance
if total > 0:
	print("There is $%s missing" % total)
elif total < 0:
	print("The is an extra $%s" % -total)
else:
	print("The money is right")
print()

# Removes players who are breakeven
playerNum = 0
while True:
	if playerNum == len(players):
		break
	if players[playerNum].balance == 0:
		players.remove(players[playerNum])
	else:
		playerNum += 1

# Creates a sorted list of players by balance
# in order to minimize the amount of venmo transactions
balanceList = []
for player in players:
	balanceList.append(player.balance)
balanceList.sort()
sortedPlayers = [0] * len(players)

for player in players:
	position = 0
	for playerBalance in balanceList:
		if player.balance == playerBalance:
			sortedPlayers[position] = player
			break
		else:
			position += 1

# Testing	
#for player in sortedPlayers:
#	print("%s : %i" % (player.name, player.balance))
# Testing Done

# Splits the player list into people who owe and people
# who are owed
winners = []
losers = []

for player in sortedPlayers:
	if player.balance < 0:
		player.isLoser()
		losers.append(player)
	else:
		player.isWinner()
		winners.append(player)
winners.reverse()

# Testing
#print("Winners: ")	
#for player in winners:
#	print("%s : %i" % (player.name, player.balance))
#
#print("Losers: ")
#for player in losers:
#	print("%s : %i" % (player.name, player.balance))
# Testing Done
	
# Updates the payable and recievable dictionaries
# with the name and amount that will be paid to them
# or from them
for winner in winners:
	for loser in losers:
		# If the winner and loser owe and are owed the same amount
		if loser.stillNeedsToPay == 0:
			continue
		if winner.stillNeedsToRecieve == -loser.stillNeedsToPay:
			# print("Equals -- Winner: %s    Loser: %s" % (winner.name,loser.name))
			# Dictionaries update with who and how much they are each
			# getting or recieving from
			winner.recievable[loser.name] = winner.stillNeedsToRecieve
			loser.payable[winner.name] = winner.stillNeedsToRecieve
			
			# The amount that is unaccounted for these players so far 
			# is set to zero 
			winner.stillNeedsToRecieve = 0
			loser.stillNeedsToPay = 0
			break
		# If the winner is owed less than the loser owes
		elif winner.stillNeedsToRecieve < -loser.stillNeedsToPay:
			# print("Loser Greater -- Winner: %s    Loser: %s" % (winner.name,loser.name))
			# Dictionaries update with who and how much they are each
			# getting or recieving from
			winner.recievable[loser.name] = winner.stillNeedsToRecieve
			loser.payable[winner.name] = winner.stillNeedsToRecieve
			# The amount the loser still owes is decreased by the amount
			# the winner was owed
			loser.stillNeedsToPay += winner.stillNeedsToRecieve
			# And the amount the winner is owed is set to zero
			winner.stillNeedsToRecieve = 0
			break
		# If the winner is owed more than the loser owes, it must
		# move though more iterations to account for the difference
		else:
			# print("Winner Greater -- Winner: %s    Loser: %s" % (winner.name,loser.name))
			# Dictionaries update with who and how much they are each
			# getting or recieving from
			winner.recievable[loser.name] = -loser.stillNeedsToPay
			loser.payable[winner.name] = -loser.stillNeedsToPay
			# The amount the winner is owed is decreased by the amount
			# the loser owes
			winner.stillNeedsToRecieve += loser.stillNeedsToPay
			# The amount the loser owes is set to zero
			loser.stillNeedsToPay = 0

# Testing
#print("Winners: ")	
#print()
#for player in winners:
#	print("%s : %i" % (player.name, player.balance))
#	print(player.recievable)
#	print()

#print("Losers: ")
#print()
#for player in losers:
#	print("%s : %i" % (player.name, player.balance))
#	print(player.payable)
#	print()
# Testing Done

print("Winner Recievables:")
print()
for winner in winners:
	print("%s is owed $%i" % (winner.name,winner.balance))
	for item in winner.recievable:
		print("%s will pay him $%i" % (item,winner.recievable[item]))
	print()

print("Loser Payables:")
print()
for loser in losers:
	print("%s owes $%i" % (loser.name,-loser.balance))
	for item in loser.payable:
		print("He will pay %s $%i" % (item,loser.payable[item]))
	print()