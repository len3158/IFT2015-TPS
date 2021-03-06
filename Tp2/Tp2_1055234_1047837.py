"""
IFT2015 - Hiver 2018
Ce programme est capable de générer une signature,
a partir d'une banque de donnees d'autres
auteurs, de déterminer l'auteur le plus probable d'un
texte mystere, a l'aide d'un Dictionnaire Abstrait.
**Auteurs: - Mehran ASADI. Matricule: 1047837
		   - Lenny SIEMENI. Matricule: 1055234**
"""

from Dictionnaire import Dictionnaire
import time
import math

PONC = ["!",'"',"'",")","(",",",".",";",":","?", "-", "_"]

"""Represents text with doublet frequencies."""
def treatText(table, filename):
	prevword = None
	with open(filename,encoding="utf8") as f:
		lines = f.readlines()
		for line in lines:
			line = line.rstrip()
			if line == '': continue
			words = treatLine(line)
			for item in range(len(words)):
				if prevword is not None:
					table.insertKey(prevword+" "+words[item])
					prevword = None
					pass
				try:
					if words[item+1] is not None:
						table.insertKey(words[item]+" "+words[item+1])
				except IndexError:
					prevword = words[item]
					pass

"""Separates words and removes punctuation."""
def treatLine(line):
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

"""Calcule la distance entre deux signatures de deux dictionnaires"""
def dist_between_ds(d1, d2):
	commond = []
	thisn = 0
	othern = 0
	dist = 0
	for k,x in d1.__items__():
		y = d2[k]
		if y is not None:
			commond.append((x,y))
			thisn += x
			othern += y
	if not len(commond) == 0:
		for x,y in commond:
			dist += (x/thisn - y/othern)**2
		dist = dist / len(commond)
		dist = math.sqrt(dist)

	return dist

"""Determine qui est l'auteur le plus probable du texte mystere
parmis 6 textes donnes"""	
def deviner_Texte():
	start_time = time.time()
	resultats = []
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

	resultats.append([dist_between_ds(tableSegur, tableMystere), "Segur"])
	resultats.append([dist_between_ds(tableBalzac, tableMystere), "Balzac"])
	resultats.append([dist_between_ds(tableVoltaire, tableMystere), "Voltaire"])
	resultats.append([dist_between_ds(tableZola, tableMystere), "Zola"])
	resultats.append([dist_between_ds(tableVerne, tableMystere), "Verne"])
	resultats.append([dist_between_ds(tableHugo, tableMystere), "Hugo"])
	
	for i in resultats:
		print(i[1]+" : "+str(i[0]))
	value = min(resultats)
	print("Auteur du texte mystère: "+value[1])
	print(str(time.time() - start_time)+" trouvé en secondes.")

"""Retourne le temps d'importation pour chaque texte dans un dictionnaire"""	
def test_performance():		
	
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
