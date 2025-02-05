class Player(object):
	def __init__(self, name,email, buyIn):
		self.name = name
		self.email = email
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
BRYAN = Player("Bryan","ru.bryankeating@outlook.com",200)
RJ = Player("RJ","ru.bryankeating@outlook.com",380)
PJ = Player("PJ","ru.bryankeating@outlook.com",200)
LOU = Player("Lou","ru.bryankeating@outlook.com",200)
CAM = Player("Cam","ru.bryankeating@outlook.com",200)
KYLE = Player("Kyle","ru.bryankeating@outlook.com",200)
JOE = Player("Joe","ru.bryankeating@outlook.com",200)
MATT = Player("Matt","ru.bryankeating@outlook.com",190)
HEN = Player("Hen","ru.bryankeating@outlook.com",200)
AIDEN = Player("Aiden","ru.bryankeating@outlook.com",200)
KEVIN = Player("Kevin","ru.bryankeating@outlook.com",200)

# List of Players
players = [RJ,LOU,BRYAN,PJ,CAM,KYLE,JOE,MATT,HEN,AIDEN,KEVIN]

# Actions of existing players
BRYAN.cashout(200)
RJ.cashout(210)
LOU.cashout(220)
CAM.cashout(220)
KEVIN.cashout(223)
PJ.cashout(220)
KYLE.cashout(220)
JOE.cashout(220)
MATT.cashout(220)
HEN.cashout(220)
AIDEN.cashout(197)

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

#T
print(balanceList)
print(len(balanceList))

#DT
	
accessedPlayers = []
for j in range(len(balanceList)):
	for i in range(len(players)):
		if players[i] in accessedPlayers:
			continue
		if players[i].balance == balanceList[j]:
			sortedPlayers[j] = players[i]
			accessedPlayers.append(players[i])
			break

print(sortedPlayers)
for player in sortedPlayers:
	print(player.name + " : " + str(player.balance))
#DT