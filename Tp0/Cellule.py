"""" Auteurs : Mehran Asadi  Matricule : 1047837
			   Lenny Siemeni Matricule : 1055234 """
from Grille import *

class Cellule:
	"""On considere une cellule de la grille comme un organisme"""
	
	def __init__(self,etat,position):
		self._etat=etat #son etat
		self._position = position
	
	def __str__(self):
		"""Override de toString pour afficher la couleur de la cellule"""
		return self._etat
		
	def voisinage(self,grilleInvisible):
		"""Determine le nombre de voisins d'une cellule dynamiquement
		   Le point de depart est la celulle elle-meme"""

		nb_voisins = 0	#Place le nombre voisin [B,Y,R,G]
		for x in [-1,0,1]:	#place i sur la ligne precedente,courante et suivante
			for y in [-1,0,1]:            #place j sur la colonne precedente,courante et suivante
				if x == 0 and y == 0:     #si i=0 et j=0, on est pas sur un voisin
					continue			  #on evite d evaluer et on continue
				elif ((self._position[0] + x) < 0) or ((self._position[1] + y) < 0):	#eviter index out of range
					continue 
				try:             
					if (grilleInvisible[self._position[0]+x][self._position[1]+y].isAlive()):
						nb_voisins += 1
				except IndexError:	#si un index out of range survient, on l'ignore
					continue
		return nb_voisins
	
	def isAlive(self):
		"""Determine si une cellule est vivante ou non"""
		return str(self._etat) != ". "

	def __getitem__(self):
		"""Accesseur qui retourne l'etat d'une cellule"""
		return self._etat