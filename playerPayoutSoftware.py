# This is my first attempt at making an algorithm that automatically
# tells people who they are paying or getting from, and how much from
# each person


class Player(object):
	def __init__(self, name, buyIn):
		self.name = name
		self.balance = -buyIn
	def rebuy(self,amount):
		self.balance -= amount
	def cashout(self,amount):
		self.balance += amount

# Players and Buy In
BRYAN = Player("bryan",200)
RJ = Player("rj",200)
PJ = Player("pj",200)
LOU = Player("lou",140)
CAM = Player("cam",100)
KYLE = Player("kyle",200)

# List of Players
players = [BRYAN,LOU,RJ,PJ,CAM,KYLE]

# Actions of existing players
RJ.rebuy(200)
PJ.rebuy(200)
CAM.rebuy(200)
PJ.rebuy(250)
RJ.rebuy(800)
BRYAN.cashout(662)
RJ.cashout(1200)
LOU.cashout(150)
CAM.cashout(500)
PJ.cashout(700)


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

# Creates a sorted list of players by balance
sortedPlayers = [players[0]]
for i in range(len(players)):
	for j in range(i):
		if players[i].balance < sortedPlayers[j].balance:
			# Testing
			print("Iteration number " + str(i))
			for sortedPlayer in sortedPlayers:
				print(sortedPlayer.name + ": " + str(sortedPlayer.balance))
			# Done testing


			insertIndex = sortedPlayers.index(players[j])
			sortedPlayers.insert(insertIndex-1,players[i])
			print("Person to be sorted: %s = %i" % (players[i].name,players[i].balance))
			break
		elif i == j:
			# Testing 
			print("Iteration number " + str(i))
			for sortedPlayer in sortedPlayers:
				print(sortedPlayer.name + ": " + str(sortedPlayer.balance))
			# Done Testing
				
			
			sortedPlayers.append(players[i])
			break

print("Iteration number 6")
for sortedPlayer in sortedPlayers:
	print(sortedPlayer.name + ": " + str(sortedPlayer.balance))