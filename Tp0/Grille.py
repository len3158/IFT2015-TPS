"""" Auteurs : Mehran Asadi  Matricule : 1047837
			   Lenny Siemeni Matricule : 1055234 """
from Cellule import *
from Regles import *
import copy
class Grille:
	"""La grille de jeu"""
	def __init__(self,ligne,colonne, position):
		self._ligne=ligne          
		self._colonne = colonne
		self._grille=[]                    
		for i in range(ligne):
			self._grille.append([Cellule('. ',[i,j]) for j in range(colonne)])  
			
	def afficherGrille(self):
		"""Fonction permettant d'afficher la grille de jeu"""
		for i in range(self._ligne):
			for j in range(self._colonne):   
				print(self._grille[i][j]._Cellule._etat)
				print('\n')
		
	def ajouterCelulle(self,elem,temp):
		"""Initialise l'etat de la cellule courante"""
		if elem in ['R','Y','B','G']:
			self._grille[temp[0]][temp[1]]=Cellule(elem+' ',temp)
		else: 
			self._grille[temp[0]][temp[1]]=Cellule('. ',temp)
	
	def modifierCellule(self,etat,i,j):
		"""Modifie l'etat d'une cellule déjà initialisee"""
		if etat in ['R ','Y ','B ','G ']:
			self._grille[i][j]._etat = etat
		else:
			self._grille[i][j]._etat = '. '
	
	def __str__(self):
		"""Override de toString qui retourne notre grille de jeu lisible"""
		self._image = ""
		for m in range(self._ligne):
			for n in range(self._colonne):
				self._image += self._grille[m][n]._etat
			if(m < self._ligne - 1):
				self._image += "\n"
		return self._image
			
	def __getitem__(self,ligne):
		"""Accesseur qui retourne la grille de jeu"""
		return self._grille[ligne]
				
	def updateGrille(self,listeRegle):
		"""Methode permettant de metre a jour la grille"""
		self._grilleInvisible=copy.deepcopy(self._grille) 
		for i in range(self._ligne):
			for j in range(self._colonne):
				nbVoisins = self._grilleInvisible[i][j].voisinage(self._grilleInvisible)  #on regarde combien de voisins a la cellule courante
				
				if not self._grilleInvisible[i][j].isAlive(): #Si la cellule actuelle est morte on la fait naitre
					if nbVoisins ==listeRegle._bleu[0]:			#conditions reunies pour faire naitre un bleu
						self.modifierCellule('B ',i,j)
					elif nbVoisins ==listeRegle._jaune[0]:		#idem pour un jaune
						self.modifierCellule('Y ',i,j)       
					elif nbVoisins ==listeRegle._rouge[0]:		#idem pour un rouge
						self.modifierCellule('R ',i,j)
					elif nbVoisins ==listeRegle._vert[0]:		#et un vert
						self.modifierCellule('G ',i,j)         
				else:
					if self._grilleInvisible[i][j]._etat=='B ' and (nbVoisins<listeRegle._bleu[1] or nbVoisins>listeRegle._bleu[2]):  
						self.modifierCellule('. ',i,j)
					if self._grilleInvisible[i][j]._etat=='Y ' and (nbVoisins<listeRegle._jaune[1] or nbVoisins>listeRegle._jaune[2]):         
						self.modifierCellule('. ',i,j)
						print(nbVoisins)
					if self._grilleInvisible[i][j]._etat=='R ' and (nbVoisins < listeRegle._rouge[1] or nbVoisins > listeRegle._rouge[2]):    
						self.modifierCellule('. ',i,j)
					if self._grilleInvisible[i][j]._etat=='G ' and (nbVoisins<listeRegle._vert[1] or nbVoisins>listeRegle._vert[2]):    
						self.modifierCellule('. ',i,j)
						print(nbVoisins)
		return self._grille
