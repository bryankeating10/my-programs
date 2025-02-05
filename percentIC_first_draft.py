""" This function takes electronegativity
of two elements that are bonded and returns
the percent ionic character of the bond
"""

import math

def percentIC(Xa,Xb):
	squareDif = (Xa-Xb)**2
	decimal = 1 - math.exp(-0.25 * squareDif)
	returnPercent = decimal * 100
	return "The percent ionic character is: " + str(round(returnPercent,2))


print(percentIC(1.8,3.5))
print(percentIC(1.6,2.1))
print(percentIC(0.7,3.0))
print(percentIC(1.7,1.9))
print(percentIC(1.2,3.0))


bond_Dict = {"TiO2":[1.8,3.5]}
print(str(bond_Dict.keys())[12:-3])
bond_Dict["CsCl"] = [1.6,2.1]
print(bond_Dict)
print(bond_Dict.keys())
x = bond_Dict.keys()
print(x)
for key in x:
	print(key)
print(bond_Dict["CsCl"][1])

