"""Classe LinkedQuaTree. Structure principale de notre Quadtree
	**Auteurs: - Mehran ASADI. Matricule: 1047837
			   - Lenny SIEMENI. Matricule: 1055234**
"""
import collections

class LinkedQuadTree:
	"""Class interne _Feuille pour les element de type feuilles"""
	class _Feuille:
		__slots__ = '_xx', '_yy','_est_interne','__dict__'
		def __init__(self, x,y):
			self._xx= x
			self._yy = y
			self._est_interne = False
		def __eq__(self,other):
			return self._xx == other._xx and self._yy == other._yy
		
		#Override toString pour affichage tel que specifie des feuilles	
		def __str__(self):
			return "["+ str(self._xx) + " " +str(self._yy) + "]"
			
	"""Classe interne _Item pour les element internes (dimension des quadrants)
		    une instance de _Item est un pointeur vers un quadrant"""
	class _Item:
		__slots__ = '_x1', '_x2','_y1', '_y2', '_milieu_x','_milieu_y','_est_interne'
		def __init__(self, x1,x2,y1,y2):
			self._x1 = x1
			self._x2 = x2
			self._y1 = y1
			self._y2 = y2
			self._milieu_x = round((x1+x2)/2,2)    #division non entiere max 2 chiffre apres la virgule
			self._milieu_y = round((y1+y2)/2,2)
			self._est_interne = True
		
		def _eq_(self, other):
			return int(self._x1) == int(other._x1) and int(self._x2) == int(other._x2) and int(self._y1) == int(other._y1) and int(self._y2) == int(other._y2)
		
		"""Cette section de methodes boolean permet de determiner la direction a prendre
			lors de la recherche d'un _Item dans un quadrant"""
		def go_nO(self,x1,x2,y1,y2):
			return self._x1 <= x1 <= self._milieu_x and self._x1 <= x2 <= self._milieu_x and self._y1 <= y1 <= self._milieu_y and self._y1 <= y2 <= self._milieu_y

		def go_nE(self,x1,x2,y1,y2):
			return self._milieu_x <= x1 <= self._x2 and self._milieu_x <= x2 <= self._x2 and self._y1 <= y1 <= self._milieu_y and self._y1 <= y2 <= self._milieu_y

		def go_sE(self,x1,x2,y1,y2):
			return self._milieu_x  <= x1 <= self._x2 and self._milieu_x  <= x2 <= self._x2 and self._milieu_y  <= y1 <= self._y2 and self._milieu_y  <= y2 <= self._y2

		def go_sO(self,x1,x2,y1,y2):
			return self._x1 <= x1 <= self._milieu_x and self._x1 <= x2 <= self._milieu_x and self._milieu_y  <= y1 <= self._y2 and self._milieu_y  <= y2 <= self._y2 		

	"""Class interne _Node pour les noeuds internes"""
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
			
		"""Cette section de methodes boolean permet de determiner la direction a prendre
			lors de la recherche d'un noeud dans l'arbre"""
		def go_nO(self,x,y):
			return self._element._est_interne and self._element._x1 <= x <= self._element._milieu_x and self._element._y1 <= y <= self._element._milieu_y

		def go_nE(self,x,y):
			return self._element._est_interne and self._element._milieu_x <= x <= self._element._x2 and self._element._y1 <= y <= self._element._milieu_y

		def go_sE(self,x,y):
			return self._element._est_interne and self._element._milieu_x <= x <= self._element._x2 and self._element._milieu_y <= y <= self._element._y2

		def go_sO(self,x,y):
			return self._element._est_interne and self._element._x1 <= x <= self._element._milieu_x and self._element._milieu_y <= y <= self._element._y2			
		
		#Overide toString pour afficher un noeud interne tel que demande
		def __str__( self ):
			if self._element._est_interne:
				mot = "<"
				mot += "1 " if self._nO is not None else "0 "
				mot += "1 " if self._nE is not None else "0 "
				mot += "1 " if self._sE is not None else "0 "
				mot += "1" if self._sO is not None else "0"
				mot += "> "
				return mot
			else:
				return str( self._element )		

	#Constructeur de l'arbre
	def __init__( self ):
		self._root = None
		self._size = 0

	#get the size
	def __len__( self ):
		return self._size
	
	#Override toString pour afficher l'arbre en Breadth-First-Print
	def __str__(self):
		if self.is_empty():
			return "Arbre vide"
		return self.breadth_first_print()
		
	#get the root
	def root( self ):
		return self._root
	
	#Boolean si l'arbre est vide
	def is_empty( self ):
		return self._size <= 0

	#Bolean si un noeud est une feuille retourne true if not interne
	def is_leaf( self, noeud ):
		return not noeud._element._est_interne

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
	
	#Boolean si un noeud interne possede des enfants
	def has_children(self,noeud):
		return self.num_children(noeud) > 0
		
	"""developer-level building methods
	"""
	#Ajouter la racine a l'arbre
	def _add_root( self, e ):
		if self._root is not None: raise ValueError( 'Root exists' )
		self._size = 1
		root = self._Node(e)
		self._root = root
		return root

	#ajouter enfant Nord Ouest et retourner la position crée
	def _add_nO( self, noeud, e ):
		if noeud._nO is not None: raise ValueError( 'Enfant Nord Ouest exist' )
		self._size += 1
		noeud._nO = self._Node(e,noeud)          #Créer un nouveau noeud(elem,parent = node)
		return noeud._nO 

	#ajouter enfant Nord Est et retourner la position crée
	def _add_nE( self, noeud, e ):
		if noeud._nE is not None: raise ValueError( 'Enfant Nord Est exist' )
		self._size += 1
		noeud._nE = self._Node(e, noeud )          #Créer un nouveau noeud(elem,parent = node)
		return noeud._nE   

	#ajouter enfant Sud Est et retourner la position crée
	def _add_sE( self, noeud, e ):
		if noeud._sE is not None: raise ValueError( 'Enfant Nord Est exist' ) 
		self._size += 1
		noeud._sE = self._Node(e, noeud )          #Créer un nouveau noeud(elem,parent = node)
		return noeud._sE

	#ajouter enfant Sud Ouest et retourner la position crée
	def _add_sO( self, noeud, e ):
		if noeud._sO is not None: raise ValueError( 'Enfant Sud Ouest exist' )
		self._size += 1
		noeud._sO = self._Node(e, noeud )          #Créer un nouveau noeud(elem,parent = node)
		return noeud._sO
		
	"""Descendre l'arbe avec les coordoonees d'une feuille (bateau)"""
	def _subtree_search( self, noeud, x,y):
		#Trouver le bon noeud associé aux coordonnes x,y
		if noeud._nO is not None and noeud.go_nO(x,y):
			return self._subtree_search( noeud._nO,x,y)
		if noeud._nE is not None and noeud.go_nE(x,y):
			return self._subtree_search( noeud._nE,x,y)
		if noeud._sE is not None and noeud.go_sE(x,y):
			return self._subtree_search( noeud._sE,x,y)
		if noeud._sO is not None and noeud.go_sO(x,y):
			return self._subtree_search( noeud._sO,x,y)
		return noeud
		
	"""Descendre l'arbe avec les coordoonees d'une bombe (bateau)"""
	def _interne_arbre_cherche( self, noeud, x1,x2,y1,y2):
		#Trouver le bon noeud interne associé aux coordonnes x,y
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
	
	"""				
	###INSERTION NOEUD##################################
	#Methode recursive d'insertion d'un noeud a l'arbre#
	####################################################
	"""	
	def ajouter_element(self,noeud,elem):
		x = elem._xx
		y = elem._yy

		if not noeud._element._est_interne:                					#Si le noeud de la position est une feuille
			noeud = noeud._parent											# Trouver le pointeur parent
		if noeud.go_nO(x,y):												#Si la les coordoonée sont dans nord ouest
			if noeud._nO is None:											#Si l'enfant nord oeust est null
				return self._add_nO(noeud,elem)								#On ajoute l'element
			if noeud._nO._element._est_interne:             				#si l'enfant nord Ouest pointe vers un arbre interne
				p_walk = self._subtree_search(noeud._nO, x,y )				#Marcher vers nord ouest
				return ajouter_element(p_walk,elem)							#ajout recursif a la position final

			if not noeud._nO._element._est_interne:  						#Si l'enfant nord Ouest est deja une feuille
				if noeud._nO._element == elem:
					raise ValueError( 'Coordonnée se ressemble' )
				backup_feuille = noeud._nO._element    						# On backup la feuille
				item_interne = self._Item(noeud._element._x1,noeud._element._milieu_x,noeud._element._y1,noeud._element._milieu_y)   #On cree un nouveau item interne avec ses nouvelles dimensions
				self._size += 1
				noeud._nO._element = item_interne							#On change l'element de l'enfant nord oeust							
				self.ajouter_element(noeud._nO,backup_feuille)				#On ajoute le backup feuille au nouveau noeud
				return self.ajouter_element(noeud._nO,elem)					#On ajoute l'element au nouveau noeud

		if noeud.go_nE(x,y):
			if noeud._nE is None:											#Si l'enfant nord EST est null
				return self._add_nE(noeud, elem )							#On ajoute l'element
			if noeud._nE._element._est_interne:            					#si l'enfant nord EST pointe vers un arbre interne
				p_walk = self._subtree_search(noeud._nE, x,y ) 				#Marcher vers nord EST
				return ajouter_element(p_walk,elem)							#ajout recursif a la position finale

			if not noeud._nE._element._est_interne:							#Si l'enfant nord EST appartient deja une feuille
				if noeud._nE._element == elem:
					raise ValueError( 'Coordonnée se ressemble' )
				backup_feuille = noeud._nE._element    						# On backup la feuille
				item_interne = self._Item(noeud._element._milieu_x,noeud._element._x2,noeud._element._y1,noeud._element._milieu_y)   #On cree un nouveau item interne avec ses nouvelles dimensions
				self._size += 1
				noeud._nE._element = item_interne     						#On change l'element de l'enfant nord oeust	
				self.ajouter_element(noeud._nE,backup_feuille)				#On ajoute le backup feuille au nouveau noeud
				return self.ajouter_element(noeud._nE,elem)					#On ajoute l'element au nouveau noeud

		if noeud.go_sE(x,y):
			if noeud._sE is None:											#Si l'enfant sud EST est null
				return self._add_sE(noeud, elem )							#On ajoute l'element
			if noeud._sE._element._est_interne:             				#si l'enfant sud EST pointe vers un arbre interne
				p_walk = self._subtree_search(noeud._sE, x,y )				#Marcher vers sud EST
				return ajouter_element(p_walk,elem)							#ajouter recursif à la position final

			if not noeud._sE._element._est_interne:							#Si l'enfant sud EST appartient deja une feuille
				if noeud._sE._element == elem:
					raise ValueError( 'Coordonnée se ressemble' )
				backup_feuille = noeud._sE._element    						# On backup la feuille
				item_interne = self._Item(noeud._element._milieu_x,noeud._element._x2,noeud._element._milieu_y,noeud._element._y2)   #On cree un nouveau item interne avec ses nouvelles dimensions
				self._size += 1
				noeud._sE._element = item_interne           				#On change l'element de l'enfant nord oeust	
				self.ajouter_element(noeud._sE,backup_feuille)				#On ajoute le backup feuille au nouveau noeud
				return self.ajouter_element(noeud._sE,elem)					#On ajoute l'élement au nouveau noeud

		if noeud.go_sO(x,y):
			if noeud._sO is None:											#Si l'enfant sud oeust est null
				return self._add_sO(noeud, elem )							#On ajoute l'élément
			if noeud._sO._element._est_interne:             				#si l'enfant sud Ouest pointe vers un arbre interne
				p_walk = self._subtree_search(noeud._sO, x,y )				#Marcher vers sud ouest
				return ajouter_element(p_walk,elem)							#ajouter recursif à la position final

			if not noeud._sO._element._est_interne:							#Si l'enfant nord Ouest appartient deja une feuille
				if noeud._sO._element == elem:
					raise ValueError( 'Coordonnée se ressemble' )
				backup_feuille = noeud._sO._element    						# On backup la feuille
				item_interne = self._Item(noeud._element._x1,noeud._element._milieu_x,noeud._element._milieu_y,noeud._element._y2)   #On créer un nouveau item interne avec nouveau dimension
				self._size += 1
				noeud._sO._element = item_interne							#On change l'élément de l'enfant nord oeust	
				self.ajouter_element(noeud._sO,backup_feuille)				#On ajoute le backup feuille au nouveau noeud
				return self.ajouter_element(noeud._sO,elem)					#On ajoute l'élement au nouveau noeud
					

	"""Methode d'insertion iterative determinant comment inserer un element dans
			le QuadTree"""
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
					
	"""				
	###SUPRIMER FEUILLE (BATEAU)##########################################################################
	#Ici on cherche quel bateau appartient a quel quadrant parent, si on trouve le bateau, on le supprime#
	#sinon SI le quadrant n'a aucun enfant on supprime le quadrant										 #
	######################################################################################################
	"""
	def supprimer_feuille(self,noeud):
		if noeud._parent._nO is not None and not noeud._parent._nO._element._est_interne and noeud._parent._nO._element == noeud._element:
			noeud._parent._nO = None    				#Changer le pointeur parent de l'enfant a None
			if not self.has_children(noeud._parent):	#Si le Noeud-Parent n'a plus d'enfant, supprimer le quadrant parent
				self.supprimer_noeud_interne(noeud._parent)
			noeud._parent = None						#Pointer le parent du noeud a None
			self._size -= 1
			return

		if noeud._parent._nE is not None and not noeud._parent._nE._element._est_interne and noeud._parent._nE._element == noeud._element:
			noeud._parent._nE = None					#Changer le pointeur parent de l'enfant a None
			if not self.has_children(noeud._parent):	#Si le Noeud-Parent n'a plus d'enfant, supprimer le quadrant parent
				self.supprimer_noeud_interne(noeud._parent)
			noeud._parent = None						#Pointer le parent du noeud a None
			self._size -= 1
			return

		if noeud._parent._sE is not None and not noeud._parent._sE._element._est_interne and noeud._parent._sE._element == noeud._element:
			noeud._parent._sE = None					#Changer pointeur parent enfant a None
			if not self.has_children(noeud._parent):	#Si le Noeud-Parent n'a plus d'enfant, supprimer le quadrant parent
				self.supprimer_noeud_interne(noeud._parent)
			noeud._parent = None						#Pointer le parent du noeud à None
			self._size -= 1
			return

		if noeud._parent._sO is not None and not noeud._parent._sO._element._est_interne and noeud._parent._sO._element == noeud._element:
			noeud._parent._sO = None					#Changer pointeur parent enfant à None
			if not self.has_children(noeud._parent):	#Si le Noeud-Parent n'a plus d'enfant, supprimer le quadrant parent
				self.supprimer_noeud_interne(noeud._parent)
			noeud._parent = None						#Pointer le parent du noeud à None
			self._size -= 1
			return
	
	"""
	#####SUPPRIMER QUADRANT#######################################################################
	#Ici on cherhce quel quadrant appartient a quel quadrant parent, son le trouve on le supprime#
	#et SI le quadrant parent n'a plus d'enfant, supprimer le quadrant parent					 #
	##############################################################################################
	"""
	def supprimer_noeud_interne(self,noeud):
		if(self.root()._element == noeud._element):		#Si le pointeur du noeud a supprimer est la racine
			self._size = 0								#On le supprime
			return										#On ne retourne rien l'arbre est vide
		if noeud._parent._element == noeud._element:
			return
		if (noeud._parent is not None and noeud._parent._nO is not None and noeud._parent._nO._element._est_interne and noeud._parent._nO._element == noeud._element):
			noeud._parent._nO = None					#Changer le pointeur parent enfant à None
			if not self.has_children(noeud._parent):	#le noeud interne n'a plus d'enfants
				self.supprimer_noeud_interne(noeud._parent)
			noeud._parent = None						#Pointer le parent du noeud à None
			self._size -= 1

			return
		if(noeud._parent._nE is not None and noeud._parent._nE._element._est_interne and noeud._parent._nE._element == noeud._element):
			noeud._parent._nE = None					#Changer pointeur parent enfant à None
			if not self.has_children(noeud._parent):	#le noeud interne n'a plus d'enfants
				self.supprimer_noeud_interne(noeud._parent)
			noeud._parent = None						#Pointer le parent du noeud à None
			self._size -= 1
			return

		if(noeud._parent._sE is not None and noeud._parent._sE._element._est_interne and noeud._parent._sE._element == noeud._element):
			noeud._parent._sE = None					#Changer pointeur parent enfant à None
			if not self.has_children(noeud._parent):	#le noeud interne n'a plus d'enfants
				self.supprimer_noeud_interne(noeud._parent)
			noeud._parent = None						#Pointer le parent du noeud à None
			self._size -= 1
			return

		if(noeud._parent._sO is not None and noeud._parent._sO._element._est_interne and noeud._parent._sO._element == noeud._element):
			noeud._parent._sO = None					#Changer pointeur parent enfant à None
			if not self.has_children(noeud._parent):	#le noeud interne n'a plus d'enfants
				self.supprimer_noeud_interne(noeud._parent)
			noeud._parent = None						#Pointer le parent du noeud à None
			self._size -= 1
			return
	
	#FORMAT X1, Y1, X2, Y2
	"""Methode permettant de pointer sur la racine du QuadTree
		et appelant la suppression recursive des bateaux a l'aide des bombes"""
	def test_bombes(self,x1,x2,y1,y2):
		noeud = self._root
		self.bombes(noeud,x1,x2,y1,y2)
		
	"""Methode recursive permettant la suppression des bateaux"""
	def bombes(self,racine,x1,x2,y1,y2):
		noeud_bombes = self._Item(x1,x2,y1,y2)
		noeud = self._interne_arbre_cherche(racine,x1,y1,x2,y2)	#Descendre les arbres internes tant que la bombe se trouve dans le quadrant
		
		#Si le noeud est un bateau et qu'il se trouve a l'interieur des coordonees de la bombe, alors supprimer le bateau et return vide
		if not noeud._element._est_interne and x1 <= noeud._element._xx <= x2 and y1 <= noeud._element._yy <= y2:
			self.supprimer_feuille(noeud)
			return																		
		
		#Si noeud est un quadrant
		if noeud._element._est_interne:
			#Si le quadrant se trouve a l'interieur des coordonnes de la bombe, alors supprimer le quadrant et ne rien retourner
			if x1 <= noeud._element._x1 and noeud._element._x2 <= x2 and y1 <= noeud._element._y1 and noeud._element._y2 <= y2:
				self.supprimer_noeud_interne(noeud)
				return
			if noeud._nO is not None:  #Si enfant Nord-Ouest existe
				#Si l'enfant Nord-Ouest est un bateau et qu'il se trouve a l'interieur de coordoonee bombe, alors supprimer le bateau Nord-Ouest
				if not noeud._nO._element._est_interne and x1 <= noeud._nO._element._xx <= x2 and y1 <= noeud._nO._element._yy <= y2:
					self.supprimer_feuille(noeud._nO)
				#Si enfant Nord-Ouest est un quadrant
				elif noeud._nO._element._est_interne:
					#Si le quadrant se trouve a l'interieur de la coordonnees de la bombe, supprimer le quadrant Nord-Ouest
					if x1 <= noeud._nO._element._x1 and noeud._nO._element._x2 <= x2 and y1 <= noeud._nO._element._y1 and noeud._nO._element._y2 <= y2: 
						self.supprimer_noeud_interne(noeud._nO)
					#Sinon si une partie de la bombe se trouve dans le quadrant Nord-Ouest,alors on appele recursivement en partant du quadrant Nord-Ouest
					elif (noeud._nO._element._x1 <= x1 <= noeud._nO._element._x2  or noeud._nO._element._x1 <= x2 <= noeud._nO._element._x2) and (noeud._nO._element._y1 <= y1 <= noeud._nO._element._y2 or noeud._nO._element._y1 <= y2 <= noeud._nO._element._y2):
						self.bombes(noeud._nO,x1,x2,y1,y2)
			if noeud._nE is not None: #Si enfant Nord-Est existe
				#Si l'enfant Nord-Est est un bateau et qu'il se trouve a l'interieur des coordonnees de la bombe, alors supprimer le bateau Nord-Est
				if not noeud._nE._element._est_interne and x1 <= noeud._nE._element._xx <= x2 and y1 <= noeud._nE._element._yy <= y2:	
						self.supprimer_feuille(noeud._nE)	
				#Sinon si enfant Nord-Est est un quadrant
				elif noeud._nE._element._est_interne:
					#Si le quadrant se trouve a l'interieur des coordonnees de la bombe, alors supprimer le quadrant Nord-Est
					if x1 <= noeud._nE._element._x1 and noeud._nE._element._x2 <= x2 and y1 <= noeud._nE._element._y1 and noeud._nE._element._y2 <= y2: 
						self.supprimer_noeud_interne(noeud._nE)
					#Sinon si une partie de la bombe se trouve dans le quadrant Nord-Est, alors on appele recursivement en partant du quadrant Nord-Est
					elif (noeud._nE._element._x1 <= x1 <= noeud._nE._element._x2 or noeud._nE._element._x1 <= x2 <= noeud._nE._element._x2) and (noeud._nE._element._y1 <= y1 <= noeud._nE._element._y2 or noeud._nE._element._y1 <= y2 <= noeud._nE._element._y2):	
						self.bombes(noeud._nE,x1,x2,y1,y2)
			if noeud._sE is not None:	#Si enfant Sud-Est existe
				#Si l'enfant Sud-Est est un bateau et qu'il se trouve a l'interieur des coordoonees de la bombe, alors supprimer le bateau Sud-Est
				if not noeud._sE._element._est_interne and x1 <= noeud._sE._element._xx <= x2 and y1 <= noeud._sE._element._yy <= y2:
						self.supprimer_feuille(noeud._sE)
				#Sinon si enfant Surd-Est est un quadrant
				elif noeud._sE._element._est_interne:
					#Si le quadrant se trouve a l'interieur des coordonnees bombe, alors supprimer le quadrant Sud-Est
					if x1 <= noeud._sE._element._x1 and noeud._sE._element._x2 <= x2 and y1 <= noeud._sE._element._y1 and noeud._sE._element._y2 <= y2: 
						self.supprimer_noeud_interne(noeud._sE)
					#Sinon si une partie de la bombe se trouve dans le quadrant Sud-Est, alors on appele recursivement en partant du quadrant Sud-Est
					elif (noeud._sE._element._x1 <= x1 <= noeud._sE._element._x2 or noeud._sE._element._x1 <= x2 <= noeud._sE._element._x2) and (noeud._sE._element._y1 <= y1 <= noeud._sE._element._y2 or noeud._sE._element._y1 <= y2 <= noeud._sE._element._y2):
						self.bombes(noeud._sE,x1,x2,y1,y2)
			if noeud._sO is not None: #Si enfant Sud-Ouest existe
				#Si l'enfant Sud-Ouest est un bateau et il se trouve à l'interieur des coordonnees de la bombe, alors supprimer le bateau Nord-Ouest
				if not noeud._sO._element._est_interne and x1 <= noeud._sO._element._xx <= x2 and y1 <= noeud._sO._element._yy <= y2:
						self.supprimer_feuille(noeud._sO)
				#Sinon si enfant Sud-Ouest est un quadrant
				elif noeud._sO._element._est_interne:
					#Si le quadrant se trouve à l'interieur de scoordonnees de la bombe, alors supprimer le quadrant Sud-Ouest
					if x1 <= noeud._sO._element._x1 and noeud._sO._element._x2 <= x2 and noeud._sO._element._y1 >= y1 and noeud._sO._element._y2 <= y2:
						self.supprimer_noeud_interne(noeud._sO)
					#Sinon si une partie de la bombe se trouve dans le quadrant Sud-Ouest, alors on appele recursivement en partant du quadrant Sud-Ouest
					elif (noeud._sO._element._x1 <= x1 <= noeud._sO._element._x2 or noeud._sO._element._x1 <= x2 <= noeud._sO._element._x2) and (noeud._sO._element._y1 <= y1 <= noeud._sO._element._y2 or noeud._sO._element._y1 <= y2 <= noeud._sO._element._y2):
						self.bombes(noeud._sO,x1,x2,y1,y2)				

	"""Affichage de l'arbre en utilisant la traversée
			breadth-first"""
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
					if c._element._est_interne:
						table1.appendleft(c)
				if len(table)== 0 and not len(table1) == 0:
					mot += "\n"
					table = table1.copy()
					table1.clear()
		else:
			mot = "Tree is empty"
		return mot
		