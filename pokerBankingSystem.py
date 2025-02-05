def buyIn(player,amount,dict):
	dict[player] = -amount

def rebuy(player,amount,dict):
	dict[player] -= amount

def cashout(player,amount,dict):
	dict[player] += amount

testDict = {"bryan":-200,"PJ":-162}
buyIn("RJ",600,testDict)
rebuy("bryan",150,testDict)
cashout("RJ",1000,testDict)

print(testDict)