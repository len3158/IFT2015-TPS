from Tp2_1055234_1047837_b1 import Tp2_1055234_1047837_b1
import time
import math
PONC = ["!",'"',"'",")","(",",",".",";",":","?", "-", "_","«","»"]
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
tableVerne = Tp2_1055234_1047837_b1()
tableZola = Tp2_1055234_1047837_b1()
tableBalzac = Tp2_1055234_1047837_b1()
tableHugo = Tp2_1055234_1047837_b1()
tableSegur = Tp2_1055234_1047837_b1()
tableVoltaire = Tp2_1055234_1047837_b1()
tableMystere = Tp2_1055234_1047837_b1()
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

def dist_between_ds(d1, d2):
	commond = dict()
	thisn = 0
	othern = 0
	dist = 0
	for k in d1.keys():
		x = d1[k]
		if k in d2:
			y = d2[k]
			commond[k] = (x, y)
			thisn += x
			othern += y
	for k in d2.keys():
		if k in commond:
			continue
		y = d2[k]
		if k in d1:
			x = d1[k]
			commond[k] = (x, y)
			thisn += x
			othern += y
	for k in commond.keys():
		x = commond[k]
		dist += (x[0]/thisn - x[1]/othern)**2
	dist = dist / len(commond.keys())
	dist = math.sqrt(dist)
	return dist
#if __name__=="main":

treatText(tableHugo, "hugo.txt")
treatText(tableMystere, "mystere.txt")
dist_between_ds(tableHugo, tableMystere)
			
			
			
#table = Tp2_1055234_1047837_b1()
#treatText(tableTest,"test.txt")
#print("Taille initiale : "+str(tableVerne._taille))
#start_time = time.time()
#treatText(tableVerne, "verne.txt")
#print("verne: " + str(time.time() - start_time))
#
#start_time = time.time()	
#treatText(tableZola, "zola.txt")
#print("zola: " + str(time.time() - start_time))
#
#start_time = time.time()
#treatText(tableBalzac, "balzac.txt")
#print("balzac: " + str(time.time() - start_time))
#
#start_time = time.time()
#treatText(tableHugo,"hugo.txt")
#print("hugo: " + str(time.time() - start_time))
#
#start_time = time.time()
#treatText(tableSegur, "segur.txt")
#print("segur: " + str(time.time() - start_time))
#
#start_time = time.time()
#treatText(tableVoltaire, "voltaire.txt")
#print("voltaire: " + str(time.time() - start_time))
#
#start_time = time.time()
#treatText(tableMystere, "mystere.txt")
#print("mystere: " + str(time.time() - start_time))
#print(tableVerne)
#print(tableZola)
#print(tableBalzac)
#print(tableSegur)
#print(tableHugo)
#print(tableVoltaire)
#print(tableMystere)
#print("Verne: ")

#print(tableHugo)

		

		
                
		

		

	
