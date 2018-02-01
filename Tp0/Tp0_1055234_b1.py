"""" Auteurs : Mehran Asadi  Matricule : 1047837
			   Lenny Siemeni Matricule : 1055234 """
from Grille import *
from Regles import *
import sys
import time
import os

def effaceEcran():
	"""Methode qui insere 100 lignes vides
       Pour simulaer l'effacement de la grille"""
	for l in range(0,50):
		print('\n')
def creerGrill():
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
	return grilleJeux

def run():
	listeRegles = Regles()
	f=open('config.txt','r')
	gameNotSet = True
	grilleJeu = creerGrill()
	for line in f:
		line=(line.strip()).split(',') 
		if gameNotSet: 
			temp = list(map(int,line))
			grilleJeu=Grille(temp[0], temp[1], temp)
			gameNotSet = False
		elif line[0] == 'R' or line[0] == 'G' or line[0] == 'B' or line[0] == 'Y':
			temp = list(map(int,line[1:]))
			grilleJeu.ajouterCelulle(line[0], temp)
	print("Game of Life : Grille de Jeu au depart\n")
	print(grilleJeu)
	if '--animation' in sys.argv:
		while True:
			grilleJeu.updateGrille(listeRegles)
			input("Appuyez sur entree pour continuer...\n")
			effaceEcran()
			print(grilleJeu)
	nbEtapes = 0
	if(len(sys.argv) <= 1):         #Si rien entrer
		nbEtapes = int(input("Veuillez entrer le nombre etapes :"))
	elif(sys.argv[1].isdigit()):
		nbEtapes = sys.argv[1]
	else:
		print("Format des arguments incorect")
		break
	n=0
	while (n < nbEtapes):
		grilleJeu.updateGrille(listeRegles)   
#		effaceEcran()
#		time.sleep(1)
		n+=1
	print(grilleJeu)
	else:
			print("Format des arguments incorect")
#	else:
#		print("Vous devez specifier le nombre d'etapes en argument")

#Lancer l'application
if __name__ == '__main__':
        run()
##Unitest
def test(arg):
	if __name__ != '__main__':
		nbEtape= int(arg)
		listeRegless = Regles()
		grilleJeuu = creerGrill()
		n = 0
		while (n < nbEtape):
			grilleJeuu.updateGrille(listeRegless)         
			n+=1
		print(grilleJeuu)		

