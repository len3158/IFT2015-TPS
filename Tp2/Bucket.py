import collections		#Just pour test imprimer arbre pour voir la structure
class Bucket():

	class _Noeud():
        #create a static structure for _Bucdoubletet using __slots__
		__slots__ = '_doublet', '_parent', '_left', '_right', '_frequence'
		def __init__( self, doublet, parent = None,left = None,right = None ):
			self._doublet = doublet
			self._parent = parent
			self._left = left
			self._right = right
			self._frequence = 1
		def __str__(self):
			return "(" + str(self._doublet) + "," + str(self._frequence)+ ")"
		

	#BinaryTree constructor
	def __init__(self):
	#create an initially empty binary tree
		self._root = None
		self._size = 0

    #get the size
	def __len__(self):
		return self._size

    #get the root
	def root(self):
		return self._madoublete_position( self._root )

    #get the parent of a position
	def parent( self, noeud ):
		return noeud._parent

    #get the left child of a position
	def left( self, noeud ):
		return noeud._left

    #get the right child of a position
	def right( self, noeud ):
		return noeud._right

	def children( self, noeud ):
		if self.left( noeud ) is not None:
			yield self.left( noeud )
		if self.right( noeud ) is not None:
			yield self.right( noeud )

    #get the number of children of a position
	def num_children( self, noeud ):
		count = 0
		if noeud._left is not None:
			count += 1
		if noeud._right is not None:
			count += 1
		return count

	"""developer-level building methods"""

    #add the root noeud with doublet
	def _add_root( self, doublet ):
		if self._root is not None: raise ValueError( 'Root exists' )
		self._size = 1
		self._root = self._Noeud( doublet )
		return self._root

    #add a left child with doublet
	def _add_left( self, noeud, doublet ):
		if noeud._left is not None: raise ValueError( 'Left child exists' )
		self._size += 1
		noeud._left = self._Noeud( doublet, noeud )
		return noeud._left

    #add a right child with doublet
	def _add_right( self,noeud, doublet ):
		if noeud._right is not None: raise ValueError( 'Right child exists' )
		self._size += 1
		noeud._right = self._Noeud( doublet, noeud )
		return noeud._right

    #replace the doublet of a position
	def _replace( self, noeud, doublet ):
		old = noeud._doublet
		noeud._doublet = doublet
		return old

    
	def ajouter(self,doublet):
		if self._size == 0:
			self._add_root(doublet)
			return 1
		else:
			racine = self._root
			return self.add_tree_search(racine,doublet)
			
	def add_tree_search(self, noeud, doublet):
		if doublet == noeud._doublet:
			return noeud
		elif doublet < noeud._doublet:
			if noeud._left is None:
				#return 1
				return self._add_left(noeud,doublet)
			else:
				return self.add_tree_search(noeud._left,doublet)
		else:
			if noeud._right is None:
				#return 1
				return self._add_right(noeud,doublet)
			else:
				return self.add_tree_search(noeud._right,doublet)
	
	def imprime(self):
		racine = self._root
		self.inorder_print(racine)
        
	def __str__(self):
		return self.breadth_first_print()

	def inorder_print( self, noeud ):
		if noeud._left is not None:
			self.inorder_print( noeud._left )
		print(noeud)
		if noeud._right is not None:
			self.inorder_print( noeud._right )
	## Seulement pour montrer la structure de l'arbre pour test	
	def breadth_first_print( self ):
		if self._root is not None:
			table = collections.deque()
			table1 = collections.deque()
			mot = ""
			mot += str(self._root)
			mot += "\n"
			for c in self.children( self._root ):
				mot += str(c)
				table.appendleft( c )
			mot += "\n"
			while len(table)!= 0:
				p = table.pop()
				for c in self.children(p):
					mot += str(c)
					table1.appendleft(c)
				if len(table)== 0 and not len(table1) == 0:
					mot += "\n"
					table = table1.copy()
					table1.clear()
		else:
			mot = "Tree is empty"
		return mot
