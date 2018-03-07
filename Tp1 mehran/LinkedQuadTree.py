class LinkedQuadTree:
    
    #Class interne _Feuille pour les element de feuilles
	class _Feuille:
		__slots__ = '_xx', '_yy'
		def __init__(self, x,y):
			self._xx= x
			self._yy = y
		
		def __str__(self):
			return "["+ str(self._xx) + ", " +str(self._yy) + "]"
	#inner class _Item pour les element internes (dimension des quadrants)
	class _Item:
		__slots__ = '_x1', '_x2','_y1', '_y2', '_milieu_x','_milieu_y'
		def __init__(self, x1,x2,y1,y2):
			self._x1 = x1
			self._x2 = x2
			self._y1 = y1
			self._y2 = y2
			self._milieu_x = (x1+x2)//2
			self._milieu_y = (y1+y2)//2
	#Class interne _Node
	class _Node:

    #inner class Position, a subclass of BinaryTree Position
		__slots__ = '_element', '_parent', '_nO', '_nE', '_sE', '_sO'
		def __init__( self, elem, parent = None, no = None, ne = None, se = None, so = None ):
			self._element = elem
			self._parent = parent
			self._nO = no
			self._nE = ne
			self._sE = se
			self._sO = so
        #Les operation boolean pour verifier la direction selon la position x et y de l'element feuille
		
		def _est_interne(self):
			#return type(self._element) is type(LinkedQuadTree._Item)
			return isinstance( self._element, LinkedQuadTree._Item)
		
    #inner class Position, a subclass of BinaryTree Position
	class Position:

        #init specifies the Tree container and uses _Node to store the element
		def __init__( self, container, node ):
				self._container = container
				self._node = node
		

		def element( self ):
			return self._node._element

		def __eq__( self, other ):
			return type( other ) is type( self ) and other._node is self._node
	


		def go_nO(self,x,y):
			return self._node._est_interne() and x < self._node._element._milieu_x and y < self._node._element._milieu_y

		def go_nE(self,x,y):
			return self._node._est_interne() and x < self._node._element._milieu_x and y > self._node._element._milieu_y

		def go_sE(self,x,y):
			return self._node._est_interne() and x > self._node._element._milieu_x and y > self._node._element._milieu_y	

		def go_sO(self,x,y):
			return self._node._est_interne() and x > self._node._element._milieu_x and y < self._node._element._milieu_y			
		def __str__( self ):
			if self._node._est_interne():
				mot = "<"
				mot += "1" if self._node._nO is not None else "0"
				mot += "1" if self._node._nE is not None else "0"
				mot += "1" if self._node._sE is not None else "0"
				mot += "1" if self._node._sO is not None else "0"
				mot += " >"
				return mot
			else:
				elemm = self.element()
				return str( elemm )		
	def _validate( self, p ):
		#return associated _Node if position is valid
		if not isinstance( p, self.Position ):
			raise TypeError( 'p must be proper Position type' )
		if p._container is not self:
			raise ValueError( 'p does not belong to this container' )
		#if p was deleted (_parent points to itself: see _delete)
		if p._node._parent is p._node:
			raise ValueError( 'p is no longer valid' )
		return p._node

	def _make_position( self, node ):
		#Retourner l'instance de Position crée si le noeud existe 
		return self.Position( self, node ) if node is not None else None

	#BinaryTree constructor
	def __init__( self ):
	#create an initially empty binary tree
		self._root = None
		self._size = 0

	#get the size
	def __len__( self ):
		return self._size

	#get the root
	def root( self ):
		return self._make_position( self._root )

	#get the parent of a position
	def parent( self, p ):
		node = self._validate( p )			#Trouver le noeud associé à la position
		return self._make_position( node._parent )  #Retourner la position crée


	#Obtenir l'children NordOuest
	def nord_O( self, p ):
		node = self._validate( p )                    #Trouver le noeud associé à la position
		return self._make_position( node._nO )      #Retourner la position crée

	#Obtenir l'children NordEst
	def nord_E( self, p ):
		node = self._validate( p )                    #Trouver le noeud associé à la position
		return self._make_position( node._nE )      #Retourner la position crée

	#Obtenir l'children SudEst
	def sud_E( self, p ):
		node = self._validate( p )                    #Trouver le noeud associé à la position
		return self._make_position( node._sE )      #Retourner la position crée

	#Obtenir l'children SudOuest
	def sud_O( self, p ):
		node = self._validate( p )                    #Trouver le noeud associé à la position
		return self._make_position( node._sO )      #Retourner la position crée

	#ask if the tree is empty
	def is_empty( self ):
		return len( self ) == 0

	#ask if a position is a leaf
	def is_leaf( self, p ):
		return self.num_children( p ) == 0

	#get the height of a position by descending the tree (efficient)
	def hauteur( self, p ):
		#returns the height of the subtree at Position p
		if self.is_leaf( p ):
			return 0
		else:
			return 1 + max( self.hauteur( c ) for c in self.children( p ) )    #1 + (hauteur de chaque children
					
	def imprime_leaf( self, p ):
		for c in self.children( p ):
			if self.is_leaf(c):
				print(c)
			self.imprime_leaf( c )

	#Generate les childrens de même parents
	def sisters_brother( self, p ):
		parent = self.parent( p )          
		if parent is None:                #Verifier si parents exist, sinon retourner None
			return None
		else:
			children = self.children(parent)
			for difchildren in children:
				if p is not difchildren:
					yield difchildren

	#get the children as a generator
	def children( self, p ):
		if self.nord_O( p ) is not None:
			yield self.nord_O( p )
		if self.nord_E( p ) is not None:
			yield self.nord_E( p )
		if self.sud_E( p ) is not None:
			yield self.sud_E( p )
		if self.sud_O( p ) is not None:
			yield self.sud_O( p )
			
	def num_children( self, p ):
		return len(self.children())

	#Retourner le nombre d'enfants 
	def num_children( self, p ):
		node = self._validate( p )            
		count = 0
		if node._nO( p ) is not None:
			count += 1
		if node._nE( p ) is not None:
			count += 1
		if node._sE( p ) is not None:
			count += 1
		if node._sO( p ) is not None:
			count += 1
		return count

	"""developer-level building methods
	"""


	#add the root node with element
	def _add_root( self, e ):
		if self._root is not None: raise ValueError( 'Root exists' )
		self._size = 1
		root = self._Node(e)
		self._root = root
		return self._make_position( root )


	#ajouter enfant Nord Ouest et retourner la position crée
	def _add_nO( self, p, e ):
		node = self._validate( p )    #Trouver le noeud associé à la position
		if node._nO is not None: raise ValueError( 'Enfant Nord Ouest exist' )
		self._size += 1
		node._nO = self._Node(e,node)          #Créer un nouveau noeud(elem,parent = node)
		return self._make_position( node._nO )   

	#ajouter enfant Nord Est et retourner la position crée
	def _add_nE( self, p, e ):
		node = self._validate( p )    #Trouver le noeud associé à la position
		if node._nE is not None: raise ValueError( 'Enfant Nord Est exist' )
		self._size += 1
		node._nE = self._Node(e, node )          #Créer un nouveau noeud(elem,parent = node)
		return self._make_position( node._nE )   

	#ajouter enfant Sud Est et retourner la position crée
	def _add_sE( self, p, e ):
		node = self._validate( p )    #Trouver le noeud associé à la position
		if node._sE is not None: raise ValueError( 'Enfant Nord Est exist' ) 
		self._size += 1
		node._sE = self._Node(e, node )          #Créer un nouveau noeud(elem,parent = node)
		return self._make_position(node._sE ) 		

	#ajouter enfant Sud Ouest et retourner la position crée
	def _add_sO( self, p, e ):
		node = self._validate( p )    #Trouver le noeud associé à la position
		if node._sO is not None: raise ValueError( 'Enfant Sud Ouest exist' )
		self._size += 1
		node._sO = self._Node(e, node )          #Créer un nouveau noeud(elem,parent = node)
		return self._make_position(node._sO ) 	


	def _subtree_search( self, p, x,y ):

		node = self._validate( p )			#Trouver le noeud associé à la position
		#return the Position with key k in subtree rooted at p
		#or the last node visited.
		if p.go_nO(x,y):
		#Position with key k perhaps in left subtree
			if self.nord_O( p ) is not None:
				return self._subtree_search( self.nord_O( p ), x,y )
		elif p.go_nE(x,y):
		#Position with key k perhaps in right subtree
			if self.nord_E( p ) is not None:
				return self._subtree_search( self.nord_E( p ), x,y )
		elif p.go_sE(x,y):
		#Position with key k perhaps in right subtree
			if self.sud_E( p ) is not None:
				return self._subtree_search( self.sud_E(p), x,y )
		elif self.sud_O(p) is not None:
			return self._subtree_search( self.sud_O(p), x,y )
		return p
			
	def ajouter_element(self,p,elem):
		noeud_position = self._validate(p)
		x = elem._xx
		y = elem._yy
		if not noeud_position._est_interne():                 #Si le noeud de la position est une feuille
			noeud_position = noeud_position._parent								# Trouver le pointeur parent
			p = self._make_position(noeud_position)			    # trouver le noeud du parent

		if p.go_nO(x,y):						#Si la les coordoonée sont dans nord ouest
			if noeud_position._nO is None:					#Si l'enfant nord oeust n'est pas null
				return self._add_nO(p,elem)
			if noeud_position._nO._est_interne():             #si l'enfant nord Ouest pointe vers un arbre interne
				p_walk = self.nord_O(p)						#Marcher vers nord ouest
				p = ajouter_element(p_walk,elem)			#ajouter recursif à la position final
			else:											#Si l'enfant nord Ouest appartient deja une feuille
				backup_feuille = noeud_position._nO._element    # On backup la feuille
				item_interne = self._Item(noeud_position._element._x1,noeud_position._element._milieu_x,noeud_position._element._y1,noeud_position._element._milieu_y)   #On créer un nouveau item interne avec nouveau dimension
				noeud_position._nO = self._Node(item_interne,noeud_position)
				pp = self._make_position(noeud_position._nO)										#On ajoute un nouveau enfant Nord Ouest avec le nouveau noeud
				ppp = self.ajouter_element(pp,backup_feuille)				#On ajoute le backup feuille au nouveau noeud
				p = self.ajouter_element(pp,elem)							#On ajoute l'élement au nouveau noeud

		elif p.go_nE(x,y):
			if noeud_position._nE is None:					#Si l'enfant nord EST n'est pas null
				return self._add_nE(p, elem )					#On ajoute l'élément
			if noeud_position._nE._est_interne():             #si l'enfant nord EST pointe vers un arbre interne
				p_walk = self.nord_E						#Marcher vers nord EST
				p = ajouter_element(p_walk,elem)			#ajouter recursif à la position final
			else:											#Si l'enfant nord EST appartient deja une feuille
				backup_feuille = noeud_position._nE._element    # On backup la feuille
				item_interne = self._Item(noeud_position._element._milieu_x,noeud_position._element._x2,noeud_position._element._y1,noeud_position._element._milieu_y)   #On créer un nouveau item interne avec nouveau dimension
				noeud_position._nE = self._Node(item_interne,noeud_position)
				pp = self._make_position(noeud_position._nE)			#On ajoute un nouveau enfant Nord EST avec le nouveau noeud
				ppp = self.ajouter_element(pp,backup_feuille)				#On ajoute le backup feuille au nouveau noeud
				p = self.ajouter_element(pp,elem)							#On ajoute l'élement au nouveau noeud

		elif p.go_sE(x,y):
			if noeud_position._sE is None:					#Si l'enfant sud EST n'est pas null
				return self._add_sE(p, elem )					#On ajoute l'élément
			if noeud_position._sE._est_interne():             #si l'enfant sud EST pointe vers un arbre interne
				p_walk = self.sud_E						#Marcher vers sud EST
				p = ajouter_element(p_walk,elem)			#ajouter recursif à la position final
			else:											#Si l'enfant sud EST appartient deja une feuille
				backup_feuille = noeud_position._sE._element    # On backup la feuille
				item_interne = self._Item(noeud_position._element._milieu_x,noeud_position._element._x2,noeud_position._element._milieu_y,noeud_position._element._y2)   #On créer un nouveau item interne avec nouveau dimension
				noeud_position._sE = self._Node(item_interne,noeud_position)
				pp = self._make_position(noeud_position._sE)									#On ajoute un nouveau enfant sud EST avec le nouveau noeud
				ppp = self.ajouter_element(pp,backup_feuille)				#On ajoute le backup feuille au nouveau noeud
				p = self.ajouter_element(pp,elem)							#On ajoute l'élement au nouveau noeud

		else:
			if noeud_position._sO is None:						#Si l'enfant sud oeust n'est pas null
				return self._add_sO(p, elem )					#On ajoute l'élément
			if noeud_position._sO._est_interne():             	#si l'enfant sud Ouest pointe vers un arbre interne
				p_walk = self.sud_O								#Marcher vers sud ouest
				p = ajouter_element(p_walk,elem)			#ajouter recursif à la position final
			else:											#Si l'enfant nord Ouest appartient deja une feuille
				backup_feuille = noeud_position._sO._element    # On backup la feuille
				item_interne = self._Item(noeud_position._element._x1,noeud_position._element._milieu_x,noeud_position._element._milieu_y,noeud_position._element._y2)   #On créer un nouveau item interne avec nouveau dimension
				noeud_position._sO = self._Node(item_interne,noeud_position)
				pp = self._make_position(noeud_position._sO)										#On ajoute un nouveau enfant sud Ouest avec le nouveau noeud
				ppp = self.ajouter_element(pp,backup_feuille)				#On ajoute le backup feuille au nouveau noeud
				p = self.ajouter_element(pp,elem)							#On ajoute l'élement au nouveau noeud
		return p


	#Remplacer le nouveau element à la position est retourner l'ancien 
	def ajouter( self,x,y ):
		feuille = self._Feuille(x,y)						#On créer une element feuille avec les coordonnée
		if self.is_empty():									#Si l'arbre n'existe pas
			item_root = self._Item(0,10315,0,10315)				#On creer un item interne racine
			p = self._add_root( item_root ) 					#On creer un nouveau racine avec l'item 
			return self.ajouter_element(p,feuille)				# On ajoute la feuille a la racine et on retourn la position 
		else:												#Sinon
			p = self._subtree_search( self.root(), x,y )		#On cherche depuis la racine la position pour les coordonnée
			if not p._node._est_interne():
				p = self.parent( p )
			return self.ajouter_element(p,feuille)
					
	def __str__(self):
		mot = ""
		p = self.root()
		mot += str(p)
		for c in self.children( p ):
			#self.imprime_leaf( c )
			mot += str(c)
		return mot

"""unit testing
"""
if __name__ == '__main__':

        mytree = LinkedQuadTree()

    #level 0
        mytree.ajouter(1,2)
        mytree.ajouter(1,7)

        print(mytree)
