from Dictionnaire import Dictionnaire
import time
import math

PONC = ["!",'"',"'",")","(",",",".",";",":","?", "-", "_"]
"""Represents text with doublet frequencies."""
def treatText(table, filename):
	prevword = None
	with open(filename,encoding="utf8") as f:
		lines = f.readlines()
		prevLine = None
		for line in lines:
			line = line.rstrip()
			if line == '': continue
			words = treatLine(line)
			for item in range(len(words)):
				if prevLine is not None:
					table.insert(prevLine+" "+words[item])
					prevLine = None
					pass
				try:
					if words[item+1] is not None:
						#print(words[item]+" "+words[item+1])
						table.insert(words[item]+" "+words[item+1])
				except IndexError:
					prevLine = words[item]
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
	for k in d1._keys:
		x = d1[k]
		if k in d2:
			y = d2[k]
			commond[k] = (x, y)
			thisn += x
			othern += y
	for k in d2._keys:
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
	if not len(commond.keys()) == 0:
		dist = dist / len(commond.keys())
		dist = math.sqrt(dist)
		return dist
	else:
		return dist

def deviner_Texte():
	resultats = []
	tableTest = Dictionnaire()
	treatText(tableTest,"test.txt")
	tableVerne = Dictionnaire()
	treatText(tableVerne, "verne.txt")
	tableZola = Dictionnaire()	
	treatText(tableZola, "zola.txt")
	tableBalzac = Dictionnaire()
	treatText(tableBalzac, "balzac.txt")
	tableHugo = Dictionnaire()
	treatText(tableHugo,"hugo.txt")
	tableSegur = Dictionnaire()
	treatText(tableSegur, "segur.txt")
	tableVoltaire = Dictionnaire()
	treatText(tableVoltaire, "voltaire.txt")
	tableMystere = Dictionnaire()
	treatText(tableMystere, "mystere.txt")

	resultats.append([dist_between_ds(tableVerne, tableMystere), "Verne "])
	resultats.append([dist_between_ds(tableZola, tableMystere), "Zola "])
	resultats.append([dist_between_ds(tableHugo, tableMystere), "Hugo "])
	resultats.append([dist_between_ds(tableSegur, tableMystere), "Segur "])
	resultats.append([dist_between_ds(tableVoltaire, tableMystere), "Voltaire "])
	resultats.append([dist_between_ds(tableBalzac, tableMystere), "Balzac "])
	for i in resultats:
		print(i[1]+" : "+str(i[0]))
	value = min(resultats)
	print("Auteur du texte mystère: "+value[1])
	
def test_performance():		
	start_time = time.time()
	tableTest = Dictionnaire()
	treatText(tableTest,"test.txt")
	print("Temps importation du texte de Test: " + str(round(time.time() - start_time,3))+" secondes")
	
	start_time = time.time()
	tableVerne = Dictionnaire()
	treatText(tableVerne, "verne.txt")
	print("Temps importation du texte de Verne: " + str(round(time.time() - start_time,3))+" secondes")

	start_time = time.time()
	tableZola = Dictionnaire()	
	treatText(tableZola, "zola.txt")
	print("Temps importation du texte de Zola: " + str(round(time.time() - start_time,3))+" secondes")

	start_time = time.time()
	tableBalzac = Dictionnaire()
	treatText(tableBalzac, "balzac.txt")
	print("Temps importation du texte de Balzac: " + str(round(time.time() - start_time,3))+" secondes")

	start_time = time.time()
	tableHugo = Dictionnaire()
	treatText(tableHugo,"hugo.txt")
	print("Temps importation du texte de Hugo: " + str(round(time.time() - start_time,3))+" secondes")

	start_time = time.time()
	tableSegur = Dictionnaire()
	treatText(tableSegur, "segur.txt")
	print("Temps importation du texte de Segur: " + str(round(time.time() - start_time,3))+" secondes")

	start_time = time.time()
	tableVoltaire = Dictionnaire()
	treatText(tableVoltaire, "voltaire.txt")
	print("Temps importation du texte de Voltaire: " + str(round(time.time() - start_time,3))+" secondes")

	start_time = time.time()
	tableMystere = Dictionnaire()
	treatText(tableMystere, "mystere.txt")
	print("Temps importation du texte mystere: " + str(round(time.time() - start_time,3))+" secondes")


if __name__=="__main__":
	deviner_Texte()
	#test_performance()