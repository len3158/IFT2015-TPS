""" Classe permettant de construire le Quadtree, et de supprimer des elements
	**Auteurs: - Mehran ASADI. Matricule: 1047837
			 - Lenny SIEMENI. Matricule: 1055234**
"""

from LinkedQuadTree import LinkedQuadTree
import random

"""Boolean test si le fichier specifie est non vide"""
def isEmpty(nomFichier):
	e=open(nomFichier,'r')
	return e.read(0)

"""Instacier un Quadtree selon un fichier ou bien des donnees aleatoires"""
def	setQuadTreeFromFile(nomFichier):		
	boats = []
	mytree = LinkedQuadTree()
	try:
		f=open(nomFichier,'r')
	except FileNotFoundError:
		return None
	if not isEmpty(nomFichier):
		for line in f:
			line=(line.strip().split(' '))
			boats.append(list(map(int,line)))
		f.close()
		for x,y in boats:
			mytree.ajouter(x,y)
		return mytree
	else:
		limite = random.randint(1,10315)		#Changez cette limites pour des coordonnees plus grandes
		for _ in range(limite):
			x = random.randint(0, 10315)		#Generateur de nombre aleatoires changez de preference ces

			y = random.randint(0, 10315)		#valeurs en tandem
			mytree.ajouter(x,y)
		return mytree

"""Fonction simulant le bombardement sur notre grille de jeu"""
def bombarder(nomFichier, tree):
	bombs = []
	aDetruire = []
	try:
		f=open(nomFichier,'r')
	except FileNotFoundError:
		return None
	if not isEmpty(nomFichier):
		for line in f:
			line=(line.strip().split('.'))
			bombs.append(list(map(int,line)))
		f.close()
		#x1,y1,x2,y2 | [0]=x1, [1]=y1, [2]=x2, [3]=y2
		for i in range(len(bombs)):
			x1, y1, x2, y2 = bombs[i][0], bombs[i][1], bombs[i][2], bombs[i][3]
			if x1 > x2:							#Normalisation des coordonnees tel que demande
				x1, x2 = x2, x1
			if y1 > y2:							#Meme chose sur l'axe des y
				y1, y2 = y2, y1
			tree.test_bombes(x1, x2, y1, y2)
	else:
		limite = random.randint(1,1000)			#Meme principe que dans setQuadTree() si le fichier n'est pas specifie/vide
		for _ in range(limite):					
			x1 = random.randint(0, 10315)		#on genere un nombre x de bombes
			y1 = random.randint(0, 10315)		#dont les coordonnes sont des nombres aleatoires
			x2 = random.randint(0, 10315)
			y2 = random.randint(0, 10315)
			if x1 > x2:							#Encore une fois normalisation des donnees
				x1, x2 = x2, x1
			if y1 > y2:
				y1, y2 = y2, y1
			bombs.append(x1,x2,y1,y2)

def jouer():
	ocean = setQuadTreeFromFile('bateaux.txt')
	bombarder('bombes.txt', ocean)
	print(ocean,end="")


""" Lancer l'application sans le test """
if __name__ == '__main__':
	jouer()


def test():
	""" Methode qui test les fonctionnalité du programme """
	if __name__ != '__main__':
		start_time = time.time()
		jouer()
		return time.time() - start_time
		

