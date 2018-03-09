import sys
import collections
class LinkedQuadTree:
    #Class interne _Feuille pour les element de feuilles
	class _Feuille:
		__slots__ = '_xx', '_yy','_est_interne'
		def __init__(self, x,y):
			self._xx= x
			self._yy = y
			self._est_interne = False
		def __eq__(self,other):
			return self._xx == other._xx and self._yy == other._yy
		
		def __str__(self):
			return "["+ str(self._xx) + ", " +str(self._yy) + "]"
	#inner class _Item pour les element internes (dimension des quadrants)
	class _Item:
		__slots__ = '_x1', '_x2','_y1', '_y2', '_milieu_x','_milieu_y','_est_interne'
		def __init__(self, x1,x2,y1,y2):
			self._x1 = x1
			self._x2 = x2
			self._y1 = y1
			self._y2 = y2
			self._milieu_x = (x1+x2)//2
			self._milieu_y = (y1+y2)//2
			self._est_interne = True
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

		
		def go_nO(self,x,y):
			return self._element._est_interne and self._element._x1 <= x <= self._element._milieu_x and self._element._y1 <= y <= self._element._milieu_y

		def go_nE(self,x,y):
			return self._element._est_interne and self._element._milieu_x <= x <= self._element._x2 and self._element._y1 <= y <= self._element._milieu_y

		def go_sE(self,x,y):
			return self._element._est_interne and self._element._milieu_x <= x <= self._element._x2 and self._element._milieu_y <= y <= self._element._y2

		def go_sO(self,x,y):
			return self._element._est_interne and self._element._x1 <= x <= self._element._milieu_x and self._element._milieu_y <= y <= self._element._y2	
		
		def __str__( self ):
			if self._element._est_interne:
				mot = "<"
				mot += "1" if self._nO is not None else "0"
				mot += "1" if self._nE is not None else "0"
				mot += "1" if self._sE is not None else "0"
				mot += "1" if self._sO is not None else "0"
				mot += ">"
				return mot
			else:
				return str( self._element )		

	sys.setrecursionlimit(3000)
	#BinaryTree constructor
	def __init__( self ):
		self._root = None
		self._size = 0

	#get the size
	def __len__( self ):
		return self._size

	#get the root
	def root( self ):
		return self._root

	#get the parent of a position
	def parent( self, noeud ):
		#self._validate( noeud )			#Tester si le noeud existe
		return noeud._parent

	#Obtenir l'children NordOuest
	def nord_O( self, noeud ):
		#self._validate( noeud )                    #Trouver le noeud associé à la position
		return noeud._nO     #Retourner la position crée

	#Obtenir l'children NordEst
	def nord_E( self, noeud ):
		#self._validate( noeud )                    #Trouver le noeud associé à la position
		return noeud._nE      #Retourner la position crée

	#Obtenir l'children SudEst
	def sud_E( self, noeud ):
		#self._validate( noeud )                    #Trouver le noeud associé à la position
		return noeud._sE       #Retourner la position crée

	#Obtenir l'children SudOuest
	def sud_O( self, noeud ):
		#self._validate( noeud )                    #Trouver le noeud associé à la position
		return noeud._sO       #Retourner la position crée

	#ask if the tree is empty
	def is_empty( self ):
		return len( self ) == 0

	#ask if a position is a leaf
	def is_leaf( self, noeud ):
		return not noeud._element._est_interne

	#get the height of a position by descending the tree (efficient)
	def hauteur( self, noeud ):
		#returns the height of the subtree at Position p
		if self.is_leaf( noeud ):
			return 0
		else:
			return 1 + max( self.hauteur( c ) for c in self.children( noeud ) )    #1 + (hauteur de chaque children
					
#	def imprime_leaf( self, noeud ):
#		for c in self.children( noeud ):
#			if self.is_leaf(c):
#				print(c)
#			self.imprime_leaf( c )

	#Generate les childrens de même parents
	def sisters_brother( self, noeud ):
		parent = self.parent( noeud )          
		if parent is None:                #Verifier si parents exist, sinon retourner None
			return None
		else:
			children = self.children(parent)
			for difchildren in children:
				if noeud is not difchildren:
					yield difchildren

	#get the children as a generator
	def children( self, noeud ):
		if noeud._element._est_interne:
			if noeud._nO is not None:
				yield noeud._nO
			if noeud._nE is not None:
				yield noeud._nE
			if noeud._sE is not None:
				yield noeud._sE
			if noeud._sO is not None:
				yield noeud._sO


	#Retourner le nombre d'enfants d'UN SEUL noeud interne
	def num_children( self, noeud ):
		#self._validate( noeud )            
		if not noeud._element._est_interne:
			return 0
		count = 0
		if noeud._nO is not None:
			count += 1
		if noeud._nE is not None:
			count += 1
		if noeud._sE is not None:
			count += 1
		if noeud._sO is not None:
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
		return root

	#ajouter enfant Nord Ouest et retourner la position crée
	def _add_nO( self, noeud, e ):
		#self._validate( noeud )    #Valider le noeud
		if noeud._nO is not None: raise ValueError( 'Enfant Nord Ouest exist' )
		self._size += 1
		noeud._nO = self._Node(e,noeud)          #Créer un nouveau noeud(elem,parent = node)
		return noeud._nO 

	#ajouter enfant Nord Est et retourner la position crée
	def _add_nE( self, noeud, e ):
		#self._validate( noeud )    
		if noeud._nE is not None: raise ValueError( 'Enfant Nord Est exist' )
		self._size += 1
		noeud._nE = self._Node(e, noeud )          #Créer un nouveau noeud(elem,parent = node)
		return noeud._nE   

	#ajouter enfant Sud Est et retourner la position crée
	def _add_sE( self, noeud, e ):
		#self._validate( noeud )    #Trouver le noeud associé à la position
		if noeud._sE is not None: raise ValueError( 'Enfant Nord Est exist' ) 
		self._size += 1
		noeud._sE = self._Node(e, noeud )          #Créer un nouveau noeud(elem,parent = node)
		return noeud._sE

	#ajouter enfant Sud Ouest et retourner la position crée
	def _add_sO( self, noeud, e ):
		#self._validate( noeud )    #Trouver le noeud associé à la position
		if noeud._sO is not None: raise ValueError( 'Enfant Sud Ouest exist' )
		self._size += 1
		noeud._sO = self._Node(e, noeud )          #Créer un nouveau noeud(elem,parent = node)
		return noeud._sO

	def _subtree_search( self, noeud, feuille):
		x = feuille._xx
		y = feuille._yy
		#self._validate( noeud )			#Trouver le noeud associé à la position
		#return the Position with key k in subtree rooted at p
		#or the last node visited.

		if noeud._nO is not None and noeud.go_nO(x,y):
			return self._subtree_search( noeud._nO,feuille)
		if noeud._nE is not None and noeud.go_nE(x,y):
			return self._subtree_search( noeud._nE,feuille)
		if noeud._sE is not None and noeud.go_sE(x,y):
			return self._subtree_search( noeud._sE,feuille)
		if noeud._sO is not None and noeud.go_sO(x,y):
			return self._subtree_search( noeud._sO,feuille)
		return noeud
		
	def ajouter_element(self,noeud,elem):
		#self._validate(noeud)
		
		x = elem._xx
		y = elem._yy

		# if not noeud._element._est_interne:                 #Si le noeud de la position est une feuille
			# noeud = noeud._parent								# Trouver le pointeur parent
			# new_node = noeud
		if noeud.go_nO(x,y):						#Si la les coordoonée sont dans nord ouest
			if noeud._nO is None:					#Si l'enfant nord oeust est null
				return self._add_nO(noeud,elem)
			if noeud._nO._element._est_interne:             #si l'enfant nord Ouest pointe vers un arbre interne
				p_walk = self._subtree_search(noeud._nO, elem )						#Marcher vers nord ouest
				return ajouter_element(p_walk,elem)			#ajouter recursif à la position final

			if not noeud._nO._element._est_interne:  								#Si l'enfant nord Ouest appartient deja une feuille
				if noeud._nO._element == elem:
					raise ValueError( 'Coordonnée se ressemble' )
				backup_feuille = noeud._nO._element    # On backup la feuille
				item_interne = self._Item(noeud._element._x1,noeud._element._milieu_x,noeud._element._y1,noeud._element._milieu_y)   #On créer un nouveau item interne avec nouveau dimension
				noeud._nO._element = item_interne	#On change l'élément de l'enfant nord oeust							
				self.ajouter_element(noeud._nO,backup_feuille)				#On ajoute le backup feuille au nouveau noeud
				return self.ajouter_element(noeud._nO,elem)							#On ajoute l'élement au nouveau noeud

		if noeud.go_nE(x,y):
			if noeud._nE is None:					#Si l'enfant nord EST n'est pas null
				return self._add_nE(noeud, elem )					#On ajoute l'élément
			if noeud._nE._element._est_interne:             #si l'enfant nord EST pointe vers un arbre interne
				p_walk = self._subtree_search(noeud._nE, elem ) 					#Marcher vers nord EST
				return ajouter_element(p_walk,elem)			#ajouter recursif à la position final

			if not noeud._nE._element._est_interne:		#Si l'enfant nord EST appartient deja une feuille
				if noeud._nE._element == elem:
					raise ValueError( 'Coordonnée se ressemble' )
				backup_feuille = noeud._nE._element    # On backup la feuille
				item_interne = self._Item(noeud._element._milieu_x+1,noeud._element._x2,noeud._element._y1,noeud._element._milieu_y)   #On créer un nouveau item interne avec nouveau dimension
				noeud._nE._element = item_interne     #On change l'élément de l'enfant nord oeust	
				self.ajouter_element(noeud._nE,backup_feuille)				#On ajoute le backup feuille au nouveau noeud
				return self.ajouter_element(noeud._nE,elem)							#On ajoute l'élement au nouveau noeud

		if noeud.go_sE(x,y):
			if noeud._sE is None:					#Si l'enfant sud EST n'est pas null
				return self._add_sE(noeud, elem )					#On ajoute l'élément
			if noeud._sE._element._est_interne:             #si l'enfant sud EST pointe vers un arbre interne
				p_walk = self._subtree_search(noeud._sE, elem )				#Marcher vers sud EST
				return ajouter_element(p_walk,elem)			#ajouter recursif à la position final

			if not noeud._sE._element._est_interne:											#Si l'enfant sud EST appartient deja une feuille
				if noeud._sE._element == elem:
					raise ValueError( 'Coordonnée se ressemble' )
				backup_feuille = noeud._sE._element    # On backup la feuille
				item_interne = self._Item(noeud._element._milieu_x+1,noeud._element._x2,noeud._element._milieu_y+1,noeud._element._y2)   #On créer un nouveau item interne avec nouveau dimension
				noeud._sE._element = item_interne           #On change l'élément de l'enfant nord oeust	
				self.ajouter_element(noeud._sE,backup_feuille)				#On ajoute le backup feuille au nouveau noeud
				return self.ajouter_element(noeud._sE,elem)							#On ajoute l'élement au nouveau noeud

		if noeud.go_sO(x,y):
			if noeud._sO is None:						#Si l'enfant sud oeust n'est pas null
				return self._add_sO(noeud, elem )					#On ajoute l'élément
			if noeud._sO._element._est_interne:             	#si l'enfant sud Ouest pointe vers un arbre interne
				p_walk = self._subtree_search(noeud._sE, elem )								#Marcher vers sud ouest
				return ajouter_element(p_walk,elem)			#ajouter recursif à la position final

			if not noeud._sO._element._est_interne:											#Si l'enfant nord Ouest appartient deja une feuille
				backup_feuille = noeud._sO._element    # On backup la feuille
				item_interne = self._Item(noeud._element._x1,noeud._element._milieu_x,noeud._element._milieu_y+1,noeud._element._y2)   #On créer un nouveau item interne avec nouveau dimension
				noeud._sO._element = item_interne		#On change l'élément de l'enfant nord oeust	
				self.ajouter_element(noeud._sO,backup_feuille)				#On ajoute le backup feuille au nouveau noeud
				return self.ajouter_element(noeud._sO,elem)							#On ajoute l'élement au nouveau noeud

	def ajouter_element_backup(self,noeud,elem):
	#self._validate(noeud)
		
		x = elem._xx
		y = elem._yy

		if noeud.go_nO(x,y):						#Si la les coordoonée sont dans nord ouest
			return self._add_nO(noeud,elem)

		if noeud.go_nE(x,y):
			return self._add_nE(noeud, elem )					#On ajoute l'élément

		if noeud.go_sE(x,y):
			if noeud._sE is None:					#Si l'enfant sud EST n'est pas null
				return self._add_sE(noeud, elem )					#On ajoute l'élément

		if noeud.go_sO(x,y):
			if noeud._sO is None:						#Si l'enfant sud oeust n'est pas null
				return self._add_sO(noeud, elem )					#On ajoute l'élément
			
	
	
	#Remplacer le nouveau element à la position est retourner l'ancien 
	def ajouter( self,x,y ):
		feuille = self._Feuille(x,y)						#On créer une element feuille avec les coordonnée
		if self.is_empty():									#Si l'arbre n'existe pas
			item_root = self._Item(0,10315,0,10315)				#On creer un item interne racine
			racine = self._add_root( item_root ) 					#On creer un nouveau racine avec l'item 
			return self.ajouter_element(racine,feuille)				# On ajoute la feuille a la racine et on retourn la position 
		else:		#Sinon
			racine = self._root
			noeud = self._subtree_search( racine, feuille )		#On cherche depuis la racine la position pour les coordonnée
			if not noeud._element._est_interne:
				if noeud._element == feuille:
					return False
				else:
					noeud = noeud._parent
			return self.ajouter_element(noeud,feuille)
					
	def __str__(self):
		mot = self.breadth_first_print()
		return mot

	#print the subtree rooted by position p
    #using a breadth-first traversal
	def breadth_first_print( self ):
		table = collections.deque()
		table1 = collections.deque()
		#table.appendleft( self._root )
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
			if len(table)== 0:
				mot += "\n"
				table.extendleft(table1)
				table1.clear()
		return mot
		
	
