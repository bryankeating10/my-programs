# This is my third attempt at making an algorithm that automatically
# tells people who they are paying or getting from, and how much from
# each person. This diverges from the second attempt by using a built in
# sort function with a different matching process and also incorperates
# automatic emails to the players with their information
# February 25, 2024

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
BRYAN = Player("Bryan","bktstaccnt01@gmail.com",900)
RJ = Player("RJ","bktstaccnt01@gmail.com",100)
PJ = Player("PJ","bktstaccnt01@gmail.com",100)
LOU = Player("Lou","bktstaccnt01@gmail.com",400)
CAM = Player("Cam","bktstaccnt01@gmail.com",300)
KYLE = Player("Kyle","bktstaccnt01@gmail.com",200)
JOE = Player("Joe","bktstaccnt01@gmail.com",800)
MATT = Player("Matt","bktstaccnt01@gmail.com",500)
HEN = Player("Hen","bktstaccnt01@gmail.com",600)
AIDEN = Player("Aiden","bktstaccnt01@gmail.com",600)
KEVIN = Player("Kevin","bktstaccnt01@gmail.com",700)
JASON = Player("Jason","bktstaccnt01@gmail.com",455)
ANGEL = Player("Angel","bktstaccnt01@gmail.com",600)
RYAN = Player("Ryan","bktstaccnt01@gmail.com",50)

# List of Players
players = [BRYAN,LOU,RJ,PJ,CAM,KYLE,JOE,MATT,HEN,AIDEN,KEVIN,JASON,ANGEL]

# Actions of existing players
KYLE.rebuy(114)
RYAN.rebuy(80)
ANGEL.rebuy(400)
PJ.rebuy(350)
RJ.rebuy(400)
BRYAN.cashout(746)
RJ.cashout(655)
LOU.cashout(523)
CAM.cashout(452)
KEVIN.cashout(500)
PJ.cashout(562)
KYLE.cashout(245)
JOE.cashout(650)
MATT.cashout(884)
HEN.cashout(624)
AIDEN.cashout(455)
JASON.cashout(223)
ANGEL.cashout(1000)
RYAN.cashout(130)

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
#print(balanceList)
#for player in players:
#	print(player.name + str(player.balance))
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

#T
#print()
#print(len(sortedPlayers))
#print(sortedPlayers)
#print("winners")
#for winner in winners:
#	print(winner.name + str(winner.balance))
#
#print("losers")
#for loser in losers:
#	print(loser.name + str(loser.balance))
#DT

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
"""
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
"""
# Testing Done

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
server.login(sender,password)
print("Logged in")

# Sends an email to each winner regarding who is paying them
for winner in winners:
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
for loser in losers:
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

		