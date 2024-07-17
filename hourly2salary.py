"""
This function converts wage to salary assuming 
8 hour 5 day work weeks 52 weeks of the year, unless
otherwise input
"""

def hourly2salary(hourlyRate,hoursPerDay = 8, daysPerWeek = 5, weeksPerYear = 52):
	return hourlyRate * hoursPerDay * daysPerWeek * weeksPerYear

print(hourly2salary(40))
print(hourly2salary(40,9))
print(hourly2salary(50,weeksPerYear = 48))
print(hourly2salary(150,daysPerWeek = 1))
print(hourly2salary(400,9,weeksPerYear = 26))