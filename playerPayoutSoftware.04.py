# Changes from playerPayoutSofware.03:
	# Email defaults to my test gmail incase player
	# does not have an email
	# Chuncks of code are defined in methods and called
	# for better programatic control
# February 26, 2024

class Player(object):
	def __init__(self, name, buyIn, email = "bktstaccnt01@gmail.com"):
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
BRYAN = Player("Bryan",150,"ru.bryankeating@gmail.com")
MEL = Player("Mel",150,"melliegems@gmail.com")


# Player List
players = [BRYAN,MEL]
lenList = len(players)

# Rebuys
BRYAN.rebuy(100)


# Total amount on table
tableTotal = 0
for player in players:
	tableTotal -= player.balance

# Cashouts
BRYAN.cashout(15)
MEL.cashout(385)


# Double check player list
def listCheck():
	x = input("All %s players are accounted for correctly ('yes'/'no'): " % str(lenList))
	if x == "Yes" or x == "yes":
		return True
	else:
		print("Incorrect number of players")
		return False

# There should be a cashout action for every player
def cashoutCorrect():
	x = input("Every player has a cashout listed ('yes'/'no'): ")
	if x == "Yes" or x == "yes":
		return True
	else:
		print("Incorrect number of cashouts")
		return False

# Total balance should equal zero
def netZeroCheck(allPlayers):
	total = 0
	for player in allPlayers:
		total += player.balance
	if total > 0:
		print("There is $%s missing" % total)
		return(False)
	elif total < 0:
		print("The is an extra $%s" % -total)
		return(False)
	else:
		print("The money is right")
		return(True)

# Removes players who are breakevn
def removeBreakEven(allPlayers):
	playerNum = 0
	while True:
		if playerNum == len(allPlayers):
			break
		if allPlayers[playerNum].balance == 0:
			allPlayers.remove(allPlayers[playerNum])
		else:
			playerNum += 1

# Creates a sorted list of players by balance
# in order to minimize the amount of venmo transactions
def sortByBalance(allPlayers):
	balanceList = []
	for player in allPlayers:
		balanceList.append(player.balance)
	balanceList.sort()
	sortedPlayersInternal = [0] * len(allPlayers)
	accessedPlayers = []
	for j in range(len(balanceList)):
		for i in range(len(allPlayers)):
			if allPlayers[i] in accessedPlayers:
				continue
			if allPlayers[i].balance == balanceList[j]:
				sortedPlayersInternal[j] = allPlayers[i]
				accessedPlayers.append(allPlayers[i])
				break
	return sortedPlayersInternal

# Splits the player list into people who owe and people
# who are owed and updates their payable and recievable
# dictionaries
def winners_vs_losers(sortedPlayersInternal):
	winners = []
	losers = []

	for player in sortedPlayersInternal:
		if player.balance < 0:
			player.isLoser()
			losers.append(player)
		else:
			player.isWinner()
			winners.append(player)
	winners.reverse()

	for winner in winners:
		for loser in losers:
			if loser.stillNeedsToPay == 0:
				continue
			if winner.stillNeedsToRecieve == -loser.stillNeedsToPay:
				winner.recievable[loser.name] = winner.stillNeedsToRecieve
				loser.payable[winner.name] = winner.stillNeedsToRecieve
				winner.stillNeedsToRecieve = 0
				loser.stillNeedsToPay = 0
				break
			elif winner.stillNeedsToRecieve < -loser.stillNeedsToPay:
				winner.recievable[loser.name] = winner.stillNeedsToRecieve
				loser.payable[winner.name] = winner.stillNeedsToRecieve
				loser.stillNeedsToPay += winner.stillNeedsToRecieve
				winner.stillNeedsToRecieve = 0
				break
			else:
				winner.recievable[loser.name] = -loser.stillNeedsToPay
				loser.payable[winner.name] = -loser.stillNeedsToPay
				winner.stillNeedsToRecieve += loser.stillNeedsToPay
				loser.stillNeedsToPay = 0

	return [winners,losers]

import time



# Executes the program:
readyToSend = False
while True:
	print("The table total from tonight was $%s" % tableTotal)
	if not(listCheck()):
		break
	if not(cashoutCorrect()):
		break
	time.sleep(1.5)
	if not(netZeroCheck(players)):
		break
	removeBreakEven(players)
	time.sleep(1.5)
	print("Breakeven players removed")
	sortedPlayers = sortByBalance(players)
	time.sleep(1.5)
	print("Players have been sorted by balance")
	winners02 = winners_vs_losers(sortedPlayers)[0]
	losers02 = winners_vs_losers(sortedPlayers)[1]
	time.sleep(1.5)
	print("Winners and losers have been separated")
	time.sleep(1.5)
	x = input("Are you ready to send the payouts? ('yes'/'no'): ")
	if x == "Yes" or x == "yes":
		readyToSend = True
		break
	else:
		print("Not ready to send")
		break
	
# Imports libraries for email sending and sets my account
# to be the sender
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
sender = "ru.bryankeating@gmail.com"
password = "fddlzjqdzwtstwdy"

# Creates the server object
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

if readyToSend:
	server.login(sender,password)
	print("Logged in")

	# Sends an email to each winner regarding who is paying them
	for winner in winners02:
		reciever = winner.email
		subject = "Transaction Record for %s" % winner.name
		body = """%s, your total winnings: $%i

You will get:
""" % (winner.name,winner.balance)
		for item in winner.recievable:
			body += """$%i from %s
""" % (winner.recievable[item],item)
		message = MIMEMultipart()
		message["From"] = sender
		message["To"] = winner.email
		message["Subject"] = subject
		message.attach(MIMEText(body))
		server.sendmail(sender,reciever,message.as_string())
		print("Email to %s sent" % winner.name)

	# Sends an email to each loser regarding who they are paying
	for loser in losers02:
		reciever = loser.email
		subject = "Transaction Record for %s" % loser.name
		body ="""%s, your total payment: $%i

You will pay:
""" % (loser.name,-loser.balance)
		for item in loser.payable:
			body += """$%i to %s
""" % (loser.payable[item],item)
		message = MIMEMultipart()
		message["From"] = sender
		message["To"] = loser.email
		message["Subject"] = subject
		message.attach(MIMEText(body))
		server.sendmail(sender,reciever,message.as_string())
		print("Email to %s sent" % loser.name)
	server.quit()
	time.sleep(1)
	print()
	print("Get home safe")
	print()
	time.sleep(1)