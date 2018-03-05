import random
from Noeud import Noeud
from Feuille import Feuille

#def _boucleNoeud(parent):
#	for enfant in parent.enfants:
#		if enfant.enfants:
#			for elem in _boucleNoeud(enfant):
#				yield elem
#		yield enfant
#	
class Quadtree:
	def __init__(self, hauteur=0):
		self._tabFeuilles = []
		self._hauteur = hauteur
		self._racine = Noeud(0, 0, 10, 10, self._tabFeuilles)
		f=open('bateaux.txt','r')
		for ligneLue in f:
			ligneLue=(ligneLue.strip()).split(' ')
			self._tabFeuilles.append([Feuille(ligneLue[0],ligneLue[1])])
		f.close()
		
	def __eq__(self, autre):
		return self._quadrant == autre._quadrant
	
	def __iter__(self):
		for enfant in boucleNoeud(self):
			yield enfant
	def __str__(self):
		"""Override de toString qui retourne notre grille de jeu lisible"""
		for e in range(self._tabFeuilles):
				self._image += '['+e[0]+' '+e[1]+']'
		return self._image
	
	def diviserNoeud(self):
		diviserNoeudRecursif(self._racine, self._hauteur)
 
	def diviserNoeudRecursif(self, noeud):
		if len(noeud.enfants)<=self._hauteur:
			return
		else:
			largeur = int(noeud.x2//2)
			hauteur = int(noeud.y2//2)

			p = contains(noeud.x1, noeud.y1, largeur, h_, noeud.feuilles)
			x1 = Noeud(noeud.x1, noeud.y1, largeur, h_, p)
			recursive_subdivide(x1, niveau)

			p = contains(noeud.x1, noeud.y1+h_, largeur, h_, noeud.feuilles)
			x2 = Noeud(noeud.x1, noeud.y1+h_, largeur, h_, p)
			recursive_subdivide(x2, niveau)

			p = contains(noeud.x1+largeur, noeud.y1, largeur, h_, noeud.feuilles)
			x3 = Noeud(noeud.x1+largeur, noeud.y1, largeur, h_, p)
			recursive_subdivide(x3, niveau)

			p = contains(noeud.x1+largeur, noeud.y1+largeur, largeur, h_, noeud.feuilles)
			x4 = Noeud(noeud.x1+largeur, noeud.y1+h_, largeur, h_, p)
			recursive_subdivide(x4, niveau)

			noeud._enfants = [x1, x2, x3, x4]
	
	
	def contains(self, x, y, l, h, feuilles):
		tempFeuilles = []
		for f in feuille:
			if f.x >= x and f.x <= x+l and f.y>=y and f.y<=y+h:
					tempFeuilles.append(f)
		return tempFeuilles


	def intersection(self, noeud):
		if not noeud.enfants:
			return [noeud]
		else:
			tempEnfants = []
			for e in noeud.enfants:
				tempEnfants += (intersection(e))
			return tempEnfants
	
	def breadth_first_search(self):
		# keep track of all visited nodes
		visites = []
		# keep track of nodes to be checked
		nonVisite = [self._racine]
		# keep looping until there are nodes still to be checked
		while nonVisite:
		   # pop shallowest node (first node) from queue
			elem = nonVisite.pop(0)
			visites.append(elem)
			voisinage = self[elem]

			# add neighbours of node to queue
			for e in voisinage:
				if voisinage not in visites:
					nonVisite.append(voisinage)
					visited.append(voisinage)
		return visites
	
	
t = Quadtree(4)
print(t._tabFeuilles)
