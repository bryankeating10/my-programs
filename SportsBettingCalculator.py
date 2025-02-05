# Code incomplete 01/24/2024


""" 
This function takes a list of implied odds
and returns the respective bet sizes to ensure
a consistent profit
"""
def dutchingCalculator(imOdds,totalBalance):
	dutchBets = []

	"""
	The reductionFactor variable stores the amount that
	is lost due to the total casino payout not covering
	the total probability of winning. This is how casinos
	make money
	"""
	reductionFactor = 1/sum(imOdds)
	for odds in imOdds:
		dutchBets.append(round(totalBalance * odds * reductionFactor,3))
	
	dutchBets.append("Lost to casino: " + str(round(dutchBets[4]*imOdds[4],3)))
	return dutchBets



"""
This funciton takes a list of american odds
and returns the respective implied odds
"""
def usaOdds2Prob(usaOdds):
	impliedOdds = []
	for odds in usaOdds:
		if odds > 0:
			impliedOdds.append(round(100/(100+odds),3))
		else:
			impliedOdds.append(round(-odds/(100-odds),3))

	return impliedOdds

testUSA = [100,200,300,400,500,-100,-200,-300,-400,-500]

testImpliedOdds = usaOdds2Prob(testUSA)
testDutch = dutchingCalculator(testImpliedOdds,100)

print(testDutch)