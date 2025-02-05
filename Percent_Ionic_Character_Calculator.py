import math
"""
This function takes a dictionary containing
compounds and their atomic component 
electronegativities and prints the percent
ionic character for each
January 26, 2024
"""

def percentIC_02(compound_Dict):
	for compound in compound_Dict:
		Xa, Xb = compound_Dict[compound]
		squareDif = (Xa - Xb)**2
		decimal = 1 - math.exp(-0.25 * squareDif)
		return_Percent = decimal * 100
		print("The percent ionic character for " + compound + " is " + \
				str(round(return_Percent,2)) + "%")

electronegativities_dict = \
	{"TiO2":[1.8,3.5],"ZnTe":[1.6,2.1],"CsCl":[0.7,3.0], \
  	"InSb":[1.7,1.9],"MgCl2":[1.2,3.0],"PO4":[2.2,3.4]}

percentIC_02(electronegativities_dict)