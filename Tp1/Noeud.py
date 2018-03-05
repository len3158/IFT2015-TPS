from Feuille import Feuille
class Noeud:
	def __init__(self, x1, y1, x2, y2, feuilles, parent):
		self._x1 = x1
		self._y1 = y1
		self._x2 = x2
		self._y2 = y2
		self._feuilles = feuilles
		self.parent = parent
		self._enfants = [None,None,None,None]
		
	
	def __eq__(self, autre):
		return self._quadrant == autre._quadrant

	def isNoeudVide(self, noeud):
		return self._quadrant is None
	
	def get_enfants(self):
		return self._enfants
	
	#marque le noeud racine
	def makeRoot( self ):
		if not self._parent:
			return self._root
	
	def get_width(self):
		return self.x2
		
	def get_height(self):
		return self.y2