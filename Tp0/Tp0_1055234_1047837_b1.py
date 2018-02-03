"""" Auteurs : Mehran Asadi  Matricule : 1047837
			   Lenny Siemeni Matricule : 1055234 """
from Grille import *
from Regles import *
import sys
import time

def effaceEcran():
	"""Methode qui insere 100 lignes vides
       Pour simulaer l'effacement de la grille"""
	for l in range(0,50):
		print('\n')


def creerGrill():
	"""Methode qui lit le fichier, creer un grille en placeant les organismes
		puis le retourne """
	f=open('config.txt','r')
	gameNotSet = True
	for line in f:
		line=(line.strip()).split(',') 
		if gameNotSet: 
			temp = list(map(int,line))
			grilleJeux=Grille(temp[0], temp[1], temp)
			gameNotSet = False
		elif line[0] == 'R' or line[0] == 'G' or line[0] == 'B' or line[0] == 'Y':
			temp = list(map(int,line[1:]))
			grilleJeux.ajouterCelulle(line[0], temp)
	f.close()
	return grilleJeux
	
def simulation(grille,nombreEtape,lesRegles):
	"""Methode qui recois en parametres la grille du jeu,le nombre etape et la list des regles 
		et qui lance la simulation puis affiche la dernière grille resultante """
	for n in range(nombreEtape):
		grille.updateGrille(lesRegles)
	print(grille)


def animations(grillee,listRegless):
	""" Methode qui recois en parametres la grille du jeu et la list des regles
		puis affiche la simulation lorsque l'utilisateur appuie sur Enter."""
	while True:
		grillee.updateGrille(listRegless)
		input("Appuyez sur entree pour continuer...\n")
		effaceEcran()
		print(grillee)

def run():
	""" Methode qui lance le jeu principale """
	listeRegles = Regles()					#Creer la liste des regles
	grilleJeu = creerGrill()				#Creer la grille du jeu
	print("Game of Life : Grille de Jeu au depart\n")
	print(grilleJeu)						#Afficher la grille originale
	if '--animation' in sys.argv:			#Si l'utilisateur lance l'animation
		animations(grilleJeu,listeRegles)
	elif(len(sys.argv) > 1 and sys.argv[1].isdigit()):	#Si l'utilisateur entre une valeur en lanceant l'application
		nbEtapes = int(sys.argv[1])
		simulation(grilleJeu,nbEtapes,listeRegles)
	else:												#Si l'utilisateur n'a entree aucune argument en leanceant l'application,
		print("Format des arguments incorect")			#un message erreur sera afficher
		nbEtapes = int(input("Veuillez entrer le nombre etapes :"))		#L'utilisateur devra alors entrer le nombre etapes
		simulation(grilleJeu,nbEtapes,listeRegles)


""" Lancer l'application sans le test """
if __name__ == '__main__':
	run()


def test(arg):
	""" Methode qui test les fonctionnalité du programme """
	if __name__ != '__main__':
		nbEtape= int(arg)
		listeRegless = Regles()
		grilleJeuu = creerGrill()
		simulation(grilleJeuu,nbEtape,listeRegless)		

