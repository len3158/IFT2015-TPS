"""" Auteurs : Mehran Asadi  Matricule : 
			   Lenny Siemeni Matricule : 1055234 """
from Grille import *
from Regles import *
import sys

def effaceEcran():
	"""Methode qui insere 100 lignes vides
       Pour simulaer l'effacement de la grille"""
	for l in range(0,100):
		print('\n')

def run():
	listeRegles = Regles()
	f=open('config.txt','r')
	gameNotSet = True
	for line in f:
		line=(line.strip()).split(',') 
		if gameNotSet: 
			temp = list(map(int,line))
			grilleJeu=Grille(temp[0], temp[1], temp)
			gameNotSet = False
		elif line[0] == 'R' or line[0] == 'G' or line[0] == 'B' or line[0] == 'Y':
			temp = list(map(int,line[1:]))
			grilleJeu.ajouterCelulle(line[0], temp)
	#print("Game of Life : Grille de Jeu au depart\n")
	print(grilleJeu)
	if '--animation' in sys.argv:
		while True:
			grilleJeu.updateGrille(listeRegles)
			input("Appuyez sur entree pour continuer...\n")
			effaceEcran()
			print(grilleJeu)
	nbEtapes = 0
	# if(len(sys.argv) <= 1):         #Si rien entrer
		# nbEtapes = int(input("Entrer le nombre etape: "))
	if(sys.argv[0].isdigit()):
		nbEtapes = int(sys.argv[1])
	n=0
	while (n < nbEtapes):
		grilleJeu.updateGrille(listeRegles)
#		effaceEcran()           Pour verifier simulation pour l'instant
		print(grilleJeu)
		time.sleep(1)
		n+=1
	else:
			print("Format des arguments incorect")
#	else:
#		print("Vous devez specifier le nombre d'etapes en argument")
run()
def test(argv):
	run()

