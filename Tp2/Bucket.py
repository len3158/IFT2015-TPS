"""
La classe Index de notre dictionnaire abstrait
**Auteurs: - Mehran ASADI. Matricule: 1047837
		   - Lenny SIEMENI. Matricule: 1055234**

On utilise une liste simplement chainee pour gerer la structure dans un sceau

Inspire du code vu en classe par François Major le 23 mars 2014
dans le cadre du cours IFT2015.
"""
class Bucket():

	class _Node:

		def __init__( self, doublet = None, next = None,frequence = 1 ):
			__slots__ = '_doublet', '_next', '_frequence'
			self._doublet = doublet
			self._next = next
			self._frequence = frequence
		
		#utile pour deboggage	
		def __str__(self):
			return "(" + str(self._doublet) + "," + str(self._frequence) + ")"
			
	def __init__(self):
		self._head = None
		self._tail = None
		self._size = 0

	def __len__(self):
		return self._size

	def is_empty(self):
		return self._size == 0

	def find( self, doublet ):
		curr = self._head
		for i in range( self._size ):
			if curr._doublet == doublet:
				return curr
			else:
				curr = curr._next
		return None

	def __iter__(self):
		curr = self._head
		for i in range( self._size ):
			yield curr._doublet
			curr = curr._next
			
	def __items__(self):
		curr = self._head
		for i in range( self._size ):
			yield (curr._doublet,curr._frequence)
			curr = curr._next
			
	def __contains__(self,doublet):
		noeud = self.find(doublet)
		if noeud is not None:
			return True
		return False

	def append( self, doublet,frequence = 1 ):
		newNode = self._Node( doublet, None,frequence )
		self._tail._next = newNode
		self._tail = newNode
		self._size += 1
		
	def add_first( self, doublet,frequence = 1):
		newNode = self._Node( doublet, None,frequence )
		self._head = self._tail = newNode
		self._size += 1

	
	def insertKey( self, doublet):
		noeud = self.find(doublet)
		if noeud is not None:
			noeud._frequence += 1
			return True
		self.append(doublet)
		return False

	def	__getitem__(self,doublet):
		noeud = self.find(doublet)
		if noeud is not None:
			return noeud._frequence
		else:
			return None
			
	def __setitem__(self,doublet,frequence):
		self._setitem(doublet,frequence)
		
	def _setitem(self,doublet,frequence):
		noeud = self.find(doublet)
		if noeud is not None:
			noeud._frequence = frequence
			return True
		else:
			self.append(doublet,frequence)
			return False			
		
	def __str__(self):
		if self.is_empty():
			return "Tableau vide"
		pp = "[ "
		curr = self._head
		pp += str(curr)
		curr = curr._next
		for i in range( self._size - 1 ):
			pp += " ," + str(curr)
			curr = curr._next
		pp += " ]"
		return pp
			