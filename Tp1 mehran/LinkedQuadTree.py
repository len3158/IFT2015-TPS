import collections
class LinkedQuadTree:
    #Class interne _Feuille pour les element de feuilles
	class _Feuille:
		__slots__ = '_xx', '_yy','_est_interne','__dict__'
		def __init__(self, x,y):
			self._xx= x
			self._yy = y
			self._est_interne = False
		def __eq__(self,other):
			return self._xx == other._xx and self._yy == other._yy
		
		def getX(self):
			return self._xx
		
		def __str__(self):
			return "["+ str(self._xx) + " " +str(self._yy) + "]"
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
		
		def _eq_(self, x1,y1,x2,y2):
			return self._x1 == x1 and self._x2 == x2 and self._milieu_x == (x1+x2)//2 and self._milieu_y == (y1+y2)//2

		def _lt_(self, other):
			return self._x1 <= x1 and self._x2 <= x2 and self._milieu_x <= (x1+x2)//2 and self._milieu_y <= (y1+y2)//2
			
		def _gt_(self, other):
			return self._x1 >= x1 and self._x2 >= x2 and self._milieu_x >= (x1+x2)//2 and self._milieu_y >= (y1+y2)//2
			
		def go_nO(self,x1,x2,y1,y2):
			return self._x1 <= x1 <= self._milieu_x and self._x1 <= x2 <= self._milieu_x and self._y1 <= y1 <= self._element._milieu_y and self._y1 <= y2 <= self._element._milieu_y

		def go_nE(self,x1,x2,y1,y2):
			return self._milieu_x + 1 <= x1 <= self._x2 and self._milieu_x + 1 <= x2 <= self._x2 and self._y1 <= y1 <= self._element._milieu_y and self._y1 <= y2 <= self._element._milieu_y

		def go_sE(self,x1,x2,y1,y2):
			return self._milieu_x + 1 <= x1 <= self._x2 and self._milieu_x + 1 <= x2 <= self._x2 and self._element._milieu_y + 1 <= y1 <= self._element.y2 and self._element._milieu_y + 1 <= y2 <= self._element.y2

		def go_sO(self,x1,x2,y1,y2):
			return self._x1 <= x1 <= self._milieu_x and self._x1 <= x2 <= self._milieu_x and self._element._milieu_y + 1 <= y1 <= self._element.y2 and self._element._milieu_y + 1 <= y2 <= self._element.y2 		

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
			return self._element._est_interne and self._element._milieu_x+1 <= x <= self._element._x2 and self._element._y1 <= y <= self._element._milieu_y

		def go_sE(self,x,y):
			return self._element._est_interne and self._element._milieu_x+1 <= x <= self._element._x2 and self._element._milieu_y+1 <= y <= self._element._y2

		def go_sO(self,x,y):
			return self._element._est_interne and self._element._x1 <= x <= self._element._milieu_x and self._element._milieu_y+1 <= y <= self._element._y2			
		
		def __str__( self ):
			if self._element._est_interne:
				mot = "<"
				mot += "1 " if self._nO is not None else "0 "
				mot += "1 " if self._nE is not None else "0 "
				mot += "1 " if self._sE is not None else "0 "
				mot += "1" if self._sO is not None else "0"
				mot += ">"
				return mot
			else:
				return str( self._element )		

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
		return self._size <= 0

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
	def has_children(self,noeud):
		return self.num_children(noeud) > 0
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

	def _subtree_search( self, noeud, x,y):
		# x = feuille.xx
		# y = feuille.yy
		#Trouver le noeud associé aux coordonnes x,y
		if noeud._nO is not None and noeud.go_nO(x,y):
			return self._subtree_search( noeud._nO,x,y)
		if noeud._nE is not None and noeud.go_nE(x,y):
			return self._subtree_search( noeud._nE,x,y)
		if noeud._sE is not None and noeud.go_sE(x,y):
			return self._subtree_search( noeud._sE,x,y)
		if noeud._sO is not None and noeud.go_sO(x,y):
			return self._subtree_search( noeud._sO,x,y)
		return noeud
		
	def _interne_arbre_cherche( self, noeud, x1,x2,y1,y2):
		# x = feuille.xx
		# y = feuille.yy
		#Trouver le noeud associé aux coordonnes x,y
		if not noeud._element._est_interne:
			return noeud
		if noeud._nO is not None and noeud._element.go_nO(x1,x2,y1,y2):
			return self._interne_arbre_cherche( noeud._nO,x1,x2,y1,y2)
		if noeud._nE is not None and noeud._element.go_nE(x1,x2,y1,y2):
			return self._interne_arbre_cherche( noeud._nE,x1,x2,y1,y2)
		if noeud._sE is not None and noeud._element.go_sE(x1,x2,y1,y2):
			return self._interne_arbre_cherche( noeud._sE,x1,x2,y1,y2)
		if noeud._sO is not None and noeud._element.go_sO(x1,x2,y1,y2):
			return self._interne_arbre_cherche( noeud._sO,x1,x2,y1,y2)
		return noeud
		
	def ajouter_element(self,noeud,elem):
		#self._validate(noeud)
		
		x = elem._xx
		y = elem._yy

		if not noeud._element._est_interne:                 #Si le noeud de la position est une feuille
			noeud = noeud._parent								# Trouver le pointeur parent
		if noeud.go_nO(x,y):						#Si la les coordoonée sont dans nord ouest
			if noeud._nO is None:					#Si l'enfant nord oeust est null
				return self._add_nO(noeud,elem)
			if noeud._nO._element._est_interne:             #si l'enfant nord Ouest pointe vers un arbre interne
				p_walk = self._subtree_search(noeud._nO, x,y )						#Marcher vers nord ouest
				return ajouter_element(p_walk,elem)			#ajouter recursif à la position final

			if not noeud._nO._element._est_interne:  								#Si l'enfant nord Ouest appartient deja une feuille
				if noeud._nO._element == elem:
					raise ValueError( 'Coordonnée se ressemble' )
				backup_feuille = noeud._nO._element    # On backup la feuille
				item_interne = self._Item(noeud._element._x1,noeud._element._milieu_x,noeud._element._y1,noeud._element._milieu_y)   #On créer un nouveau item interne avec nouveau dimension
				self._size += 1
				noeud._nO._element = item_interne	#On change l'élément de l'enfant nord oeust							
				self.ajouter_element(noeud._nO,backup_feuille)				#On ajoute le backup feuille au nouveau noeud
				return self.ajouter_element(noeud._nO,elem)							#On ajoute l'élement au nouveau noeud

		if noeud.go_nE(x,y):
			if noeud._nE is None:					#Si l'enfant nord EST n'est pas null
				return self._add_nE(noeud, elem )					#On ajoute l'élément
			if noeud._nE._element._est_interne:             #si l'enfant nord EST pointe vers un arbre interne
				p_walk = self._subtree_search(noeud._nE, x,y ) 					#Marcher vers nord EST
				return ajouter_element(p_walk,elem)			#ajouter recursif à la position final

			if not noeud._nE._element._est_interne:		#Si l'enfant nord EST appartient deja une feuille
				if noeud._nE._element == elem:
					raise ValueError( 'Coordonnée se ressemble' )
				backup_feuille = noeud._nE._element    # On backup la feuille
				item_interne = self._Item(noeud._element._milieu_x+1,noeud._element._x2,noeud._element._y1,noeud._element._milieu_y)   #On créer un nouveau item interne avec nouveau dimension
				self._size += 1
				noeud._nE._element = item_interne     #On change l'élément de l'enfant nord oeust	
				self.ajouter_element(noeud._nE,backup_feuille)				#On ajoute le backup feuille au nouveau noeud
				return self.ajouter_element(noeud._nE,elem)							#On ajoute l'élement au nouveau noeud

		if noeud.go_sE(x,y):
			if noeud._sE is None:					#Si l'enfant sud EST n'est pas null
				return self._add_sE(noeud, elem )					#On ajoute l'élément
			if noeud._sE._element._est_interne:             #si l'enfant sud EST pointe vers un arbre interne
				p_walk = self._subtree_search(noeud._sE, x,y )				#Marcher vers sud EST
				return ajouter_element(p_walk,elem)			#ajouter recursif à la position final

			if not noeud._sE._element._est_interne:											#Si l'enfant sud EST appartient deja une feuille
				if noeud._sE._element == elem:
					raise ValueError( 'Coordonnée se ressemble' )
				backup_feuille = noeud._sE._element    # On backup la feuille
				item_interne = self._Item(noeud._element._milieu_x+1,noeud._element._x2,noeud._element._milieu_y+1,noeud._element._y2)   #On créer un nouveau item interne avec nouveau dimension
				self._size += 1
				noeud._sE._element = item_interne           #On change l'élément de l'enfant nord oeust	
				self.ajouter_element(noeud._sE,backup_feuille)				#On ajoute le backup feuille au nouveau noeud
				return self.ajouter_element(noeud._sE,elem)							#On ajoute l'élement au nouveau noeud

		if noeud.go_sO(x,y):
			if noeud._sO is None:						#Si l'enfant sud oeust n'est pas null
				return self._add_sO(noeud, elem )					#On ajoute l'élément
			if noeud._sO._element._est_interne:             	#si l'enfant sud Ouest pointe vers un arbre interne
				p_walk = self._subtree_search(noeud._sE, x,y )								#Marcher vers sud ouest
				return ajouter_element(p_walk,elem)			#ajouter recursif à la position final

			if not noeud._sO._element._est_interne:											#Si l'enfant nord Ouest appartient deja une feuille
				backup_feuille = noeud._sO._element    # On backup la feuille
				item_interne = self._Item(noeud._element._x1,noeud._element._milieu_x,noeud._element._milieu_y+1,noeud._element._y2)   #On créer un nouveau item interne avec nouveau dimension
				self._size += 1
				noeud._sO._element = item_interne		#On change l'élément de l'enfant nord oeust	
				self.ajouter_element(noeud._sO,backup_feuille)				#On ajoute le backup feuille au nouveau noeud
				return self.ajouter_element(noeud._sO,elem)							#On ajoute l'élement au nouveau noeud

	#Remplacer le nouveau element à la position est retourner l'ancien 
	def ajouter( self,x,y ):
		feuille = self._Feuille(x,y)						#On créer une element feuille avec les coordonnée
		if self.is_empty():									#Si l'arbre n'existe pas
			item_root = self._Item(0,10315,0,10315)				#On creer un item interne racine
			racine = self._add_root( item_root ) 					#On creer un nouveau racine avec l'item 
			return self.ajouter_element(racine,feuille)				# On ajoute la feuille a la racine et on retourn la position 
		else:		#Sinon
			racine = self._root
			noeud = self._subtree_search( racine, x,y)		#On cherche depuis la racine la position pour les coordonnée
			if not noeud._element._est_interne:
				if noeud._element == feuille:
					return False
				else:
					noeud = noeud._parent
			return self.ajouter_element(noeud,feuille)

	def supprimer(self, x,y):
		if self.is_empty():
			return 'L arbre est vide'
		else:
			feuille = self._Feuille(x,y)
			racine = self._root
			noeud = self._subtree_search( racine, x,y )
			if noeud._element._est_interne:
				raise ValueError('Node {} not found'.format(x,y))
			else:
				if noeud._element != feuille:
					raise ValueError('Node {} not found'.format(x,y))
				else:
					# print("Parent du noeud supprimé: " + str(noeud._parent))
					# print("Noeud supprimé: " + str(noeud))
<<<<<<< HEAD
					self.supprimer_feuille(noeud)
	def supprimer_feuille(self,noeud):
		if noeud._parent._nO is not None and not noeud._parent._nO._element._est_interne and noeud._parent._nO._element == noeud._element:
			noeud._parent._nO = None
			#print("Parent du noeud nord-oeust supprimé: " + str(noeud._parent))
		elif noeud._parent._nE is not None and not noeud._parent._nE._element._est_interne and noeud._parent._nE._element == noeud._element:
			noeud._parent._nE = None
			#print("Parent du noeud nord-est supprimé: " + str(noeud._parent))
		elif noeud._parent._sE is not None and not noeud._parent._sE._element._est_interne and noeud._parent._sE._element == noeud._element:
			noeud._parent._sE = None
			#print("Parent du noeud sud-est supprimé: " + str(noeud._parent))
		elif noeud._parent._sO is not None and not noeud._parent._sO._element._est_interne and noeud._parent._sO._element == noeud._element:
			noeud._parent._sO = None
			#print("Parent du noeud sud-oeust supprimé: " + str(noeud._parent))
		print("Noeud supprimé: " + str(noeud))
		if not self.has_children(noeud._parent):
			self.supprimer_noeud_interne(noeud._parent)
		noeud._parent = None
		self._size -= 1
	
=======
					if (noeud._parent._nO is not None and not noeud._parent._nO._element._est_interne and noeud._parent._nO._element == feuille) and noeud._parent._nO.contains(x,y,x1,x2,y1,y2):
						noeud._parent._nO = None
						#print("Parent du noeud nord-oeust supprimé: " + str(noeud._parent))
					elif(noeud._parent._nE is not None and not noeud._parent._nE._element._est_interne and noeud._parent._nE._element == feuille) and noeud._parent._nE.contains(x,y,x1,x2,y1,y2):
						noeud._parent._nE = None
						#print("Parent du noeud nord-est supprimé: " + str(noeud._parent))
					elif(noeud._parent._sE is not None and not noeud._parent._sE._element._est_interne and noeud._parent._sE._element == feuille) and noeud._parent._sE.contains(x,y,x1,x2,y1,y2):
						noeud._parent._sE = None
						#print("Parent du noeud sud-est supprimé: " + str(noeud._parent))
					elif(noeud._parent._sO is not None and not noeud._parent._sO._element._est_interne and noeud._parent._sO._element == feuille) and noeud._parent._sO.contains(x,y,x1,x2,y1,y2):
						noeud._parent._sO = None
						#print("Parent du noeud sud-oeust supprimé: " + str(noeud._parent))
					print("Noeud supprimé: " + str(noeud))
					if not self.has_children(noeud._parent):
						self.supprimer_noeud_interne(noeud._parent)
					noeud._parent = None
					self._size -= 1

	def supprimer_test(self, x1, y1, x2, y2, n):
		for c in self.children(n):
			if(self.is_leaf(c)):
				print('feuille')
				print(c._element._x1)
#				c.contains(x1,y1,x2,y2)
			self.supprimer_test(x1, y1, x2, y2, c)



>>>>>>> parent of be02c9b... problème accès feuille
	def supprimer_noeud_interne(self,noeud):
		if(self.root()._element == noeud._element):
			self._size = 0
			print("Racine supprimer")
		else:
			if (noeud._parent._nO is not None and noeud._parent._nO._element._est_interne and noeud._parent._nO._element == noeud._element):
				noeud._parent._nO = None
				#print("Parent du noeud interne nord-oeust supprimé: " + str(noeud._parent))
			elif(noeud._parent._nE is not None and noeud._parent._nE._element._est_interne and noeud._parent._nE._element == noeud._element):
				noeud._parent._nE = None
				#print("Parent du noeud interne nord-est supprimé: " + str(noeud._parent))
			elif(noeud._parent._sE is not None and noeud._parent._sE._element._est_interne and noeud._parent._sE._element == noeud._element):
				noeud._parent._sE = None
				#print("Parent du noeud interne sud-est supprimé: " + str(noeud._parent))
			elif(noeud._parent._sO is not None and noeud._parent._sO._element._est_interne and noeud._parent._sO._element == noeud._element):
				noeud._parent._sO = None
				#print("Parent du noeud interne sud-oeust supprimé: " + str(noeud._parent))
			print("Noeud interne supprimé: " + "(" + str(noeud._element._x1) + ", " + str(noeud._element._y1) + ") (" + str(noeud._element._x2) + ", " + str(noeud._element._y2) + ")")
			if not self.has_children(noeud._parent):
				self.supprimer_noeud_interne(noeud._parent)
			noeud._parent = None
			self._size -= 1
	
	def test_bombes(self,x1,x2,y1,y2):
		noeud = self._root
		self.bombes(noeud,x1,x2,y1,y2)
	def bombes(self,racine,x1,x2,y1,y2):
		noeud_bombes = self._Item(x1,x2,y1,y2)
		noeud = self._interne_arbre_cherche(racine,x1,x2,y1,y2)			#Descendre les arbres internes avec les coordonnees
		if not noeud._element._est_interne:							#Si le noeud est une feuille
			if x1 <= noeud._element._xx <= x2 and y1 <= noeud._element._yy <= y2:   #Si la feuille est a l'interieur de les coordonnes bombe
				self.supprimer_feuille(noeud)											#Effacer la feuille
			else:																	#Sinon
				print("Espace vide")													#Afficer espace vide 
				return																	#Retourner vide
		elif noeud._element == noeud_bombes:						#Sinon si le noeud interne a les meme dimension que la dimension de la bombe
			self.supprimer_noeud_interne(noeud)							#Supprimer le noeud interne
			return
		else:														#Sinon
			if noeud._nO is not None:									#Si enfant Nord-Ouest existe
				if not noeud._nO._element._est_interne and x1 <= noeud._nO._element._xx <= x2 and y1 <= noeud._nO._element._yy <= y2:						#S'il n'est pas interne
					self.supprimer_feuille(noeud._nO)												#Supprimer la feuille
				elif noeud._nO._element._est_interne:														#Sinon il est interne
					if noeud._nO._element._x1 >= x1 and noeud._nO._element._x2 <= x2 and noeud._nO._element._y1 >= y1 and noeud._nO._element._y2 <= y2: #Si le noeud interne se trouve dans coordoonée bombe
						self.supprimer_noeud_interne(noeud._nO)																								#Detruire le noeud interne
					elif noeud._nO._element._x1 <= x1 <= noeud._nO._element._x2 and noeud._nO._element._y1 <= y1 <= noeud._element._y2:					#Sinon si une partie de bombe se trouve dans le noeud interne
						self.bombes(noeud._nO,x1,x2,y1,y2)
			if noeud._nE is not None:							#Si enfant Nord-Est existe
				if not noeud._nE._element._est_interne:				#S'il n'est pas interne
					if x1 <= noeud._nE._element._xx <= x2 and y1 <= noeud._nE._element._yy <= y2:	#Si la feuille se trouve dans coordoonee bombe
						self.supprimer_feuille(noeud._nE)												#Supprimer la feuille
				else:												#Sinon il est interne
					if noeud._nE._element._x1 >= x1 and noeud._nE._element._x2 <= x2 and noeud._nE._element._y1 >= y1 and noeud._nE._element._y2 <= y2: #Si le noeud interne se trouve dans coordoonée bombe
						self.supprimer_noeud_interne(noeud._nE)																								#Detruire le noeud interne
					elif noeud._nE._element._x1 <= x1 <= noeud._nE._element._x2 or noeud._nE._element._x1 <= x2 <= noeud._nE._element._x2 and noeud._nE._element._y1 <= y1 <= noeud._element._y2:	#Sinon si une partie de bombe se trouve dans le noeud interne
						self.bombes(noeud._nE,x1,x2,y1,y2)
			if noeud._sE is not None:							#Si enfant Sud-Est existe
				if not noeud._sE._element._est_interne:				#S'il n'est pas interne
					if x1 <= noeud._sE._element._xx <= x2 and y1 <= noeud._sE._element._yy <= y2:	#Si la feuille se trouve dans coordoonee bombe
						self.supprimer_feuille(noeud._sE)												#Supprimer la feuille
				else:												#Sinon il est interne
					if noeud._sE._element._x1 >= x1 and noeud._sE._element._x2 <= x2 and noeud._sE._element._y1 >= y1 and noeud._sE._element._y2 <= y2: #Si le noeud interne se trouve dans coordoonée bombe
						self.supprimer_noeud_interne(noeud._sE)																								#Detruire le noeud interne
					elif noeud._sE._element._x1 <= x1 <= noeud._sE._element._x2 or noeud._sE._element._x1 <= x2 <= noeud._sE._element._x2 and noeud._sE._element._y1 <= y2 <= noeud._element._y2:	#Sinon si une partie de bombe se trouve dans le noeud interne
						self.bombes(noeud._sE,x1,x2,y1,y2)
			if noeud._sO is not None:							#Si enfant Sud-Ouest existe
				if not noeud._sO._element._est_interne:				#S'il n'est pas interne
					if x1 <= noeud._sO._element._xx <= x2 and y1 <= noeud._sO._element._yy <= y2:	#Si la feuille se trouve dans coordoonee bombe
						self.supprimer_feuille(noeud._sO)												#Supprimer la feuille
				else:												#Sinon il est interne
					if noeud._sO._element._x1 >= x1 and noeud._sO._element._x2 <= x2 and noeud._sO._element._y1 >= y1 and noeud._sO._element._y2 <= y2: #Si le noeud interne se trouve dans coordoonée bombe
						self.supprimer_noeud_interne(noeud._sO)																								#Detruire le noeud interne
					elif noeud._sO._element._x1 <= x1 <= noeud._sO._element._x2 and noeud._sO._element._y1 <= y2 <= noeud._element._y2:	#Sinon si une partie de bombe se trouve dans le noeud interne
						self.bombes(noeud._sO,x1,x2,y1,y2)				

				
	# def diviser_bombe(noeud,x1,x2,y1,y2):
		# if x1 <= noeud._element._milieu_x and x2 >= noeud._element._element._milieu_x +1:	#Si le bombe entre Ouest et Est
			# if y1 <= noeud._element._milieu_y and y2 >= noeud._element._milieu_y + 1:			#Si le bombe entre Nord et Sud
				# self.bombes(noeud,x1,noeud._element._milieu_x,y1,noeud._milieu_y)					#Divisier bombe Nord-Ouest
				# self.bombes(noeud,noeud._element._milieu_x+1,x2,y1,noeud._element._milieu_y)		#Divisier bombe Nord-Est
				# self.bombes(noeud,noeud._element._milieu_x+1,x2,noeud._element._milieu_y+1,y2)		#Diviser bombe Sud-Est
				# self.bombes(noeud,x1,noeud._element._milieu_x,noeud._element._milieu_y+1,y2)		#Diviser bombe Sud-Ouest
			# else:																				#Sinon
				# self.bombes(noeud,x1,noeud._element._milieu_x,y1,y2)								#Bombe Ouest
				# self.bombes(noeud._element._milieu_x +1, x2,y1,y2)									#Bombe Est
		# else:																				#Sinon
			# self.bombes(noeud,x1,x2,y1,noeud._milieu_y)											#Bombe Nord
			# self.bombes(noeud,x1,x2,noeud._milieu_y+1,y2)										#Bombe Sud
				
			# bombe_O = self._Item(x1,noeud._element._milieu_x,y1,y2)
			# bombe_e = self._Item(noeud._milieu_x+1,x2,y1,y2)
		
	
	
	def __str__(self):
		if self.is_empty():
			return "Arbre vide"
		return self.breadth_first_print()

	#print the subtree rooted by position p
    #using a breadth-first traversal
	def breadth_first_print( self ):
		if self._root is not None:
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
		else:
			mot = "Tree is empty"
		return mot
		