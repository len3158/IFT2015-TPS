from Tp2_1055234_1047837_b1 import Tp2_1055234_1047837_b1
PONC = ["!",'"',"'",")","(",",",".",";",":","?", "-", "_","«"]
#class test():
#		table = Tp2_1055234_1047837_b1()
#		table.insert("bonjour toi")
#		table.insert("manger chat")
#		table.insert("salut")
#		table.insert("salut")
#		table.insert("salutt")
#		table.insert("manger chien")
#		table.insert("mangerchoroclat")
#		table.insert("Bonjour moi")
#		
#		print("Afficher la table apres insertion de 11 element")
#		print(table)
#        
#        
#		table["manger chien"] = 7
#		del table["bonjour toi"]
#		print("Afficher la table apres (manger chien = 7) et delete (bonjour toi)") 
#		print(table)
tableTest = Tp2_1055234_1047837_b1()
tableHugo = Tp2_1055234_1047837_b1()
"""Represents text with doublet frequencies."""
def treatText(table, filename):
	prevword = None
	with open(filename) as f:
		lines = f.readlines()
		for line in lines:
			line = line.rstrip()
			if line == '': continue
			words = treatLine(line)
			#print(len(words))
			####### À COMPLÉTER ############################################
			for item in range(len(words)):
				try:
					if words[item+1] is not None:
						#print(words[item]+" "+words[item+1])
						table.insert(words[item]+" "+words[item+1])
				except IndexError:
					pass

def treatLine(line):
	"""
	Separates words and removes punctuation.
	"""
	noponc = ""
	for c in line:
		if c in PONC:
			noponc = noponc + " "
		else:
			noponc = noponc + c
	words = noponc.split()
	wlower = []
	for w in words:
		if len(w) > 2:
			wlower.append(w.lower())
	return wlower
		
#if __name__=="main":
#table = Tp2_1055234_1047837_b1()
#treatText(tableTest,"test.txt")
treatText(tableHugo,"hugo.txt")
print(tableHugo)

		

		
                
		

		

	
