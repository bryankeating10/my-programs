class PokerTracker(object):
	def __init__(self,session,notes):
		self.session = session
		self.notes = notes
	name = "Wildhorse"
	DOB = "January 15, 2003"

class SessionInfo(object):
	def __init__(self,date,day,buyin,cashout):
		self.date = date
		self.day = day
		self.buyin = buyin
		self.cashout = cashout

	

ultimateTracker = PokerTracker("Buy in: 900 Cash out: 1169", "Bought in way too much. Played okay. Ran hot")
print(ultimateTracker.DOB)
print(ultimateTracker.name)
print(ultimateTracker.session)
print(ultimateTracker.notes)



class Vehicle:
	def __init__(self) -> None:
		pass
	def moves(self):
		print("gooo")
	
myCar = Vehicle()
myCar.moves()
