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
			self._milieu_x = round((x1+x2)/2,2)   #max 2 chiffre apres la virgule
			self._milieu_y = round((y1+y2)/2,2)
			self._est_interne = True
		
		def _eq_(self, other):
			return int(self._x1) == int(other._x1) and int(self._x2) == int(other._x2) and int(self._y1) == int(other._y1) and int(self._y2) == int(other._y2)
			
		def go_nO(self,x1,x2,y1,y2):
			return self._x1 <= x1 <= self._milieu_x and self._x1 <= x2 <= self._milieu_x and self._y1 <= y1 <= self._milieu_y and self._y1 <= y2 <= self._milieu_y

		def go_nE(self,x1,x2,y1,y2):
			return self._milieu_x <= x1 <= self._x2 and self._milieu_x <= x2 <= self._x2 and self._y1 <= y1 <= self._milieu_y and self._y1 <= y2 <= self._milieu_y

		def go_sE(self,x1,x2,y1,y2):
			return self._milieu_x  <= x1 <= self._x2 and self._milieu_x  <= x2 <= self._x2 and self._milieu_y  <= y1 <= self._y2 and self._milieu_y  <= y2 <= self._y2

		def go_sO(self,x1,x2,y1,y2):
			return self._x1 <= x1 <= self._milieu_x and self._x1 <= x2 <= self._milieu_x and self._milieu_y  <= y1 <= self._y2 and self._milieu_y  <= y2 <= self._y2 		

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
				mot += "1 " if self._nO is not None else "0 "
				mot += "1 " if self._nE is not None else "0 "
				mot += "1 " if self._sE is not None else "0 "
				mot += "1" if self._sO is not None else "0"
				mot += "> "
				#mot += "(" + str(self._element._x1) +"," + str(self._element._y1) + "," + str(self._element._x2) + "," + str(self._element._y2) + ")"
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
	#print the tree
	def __str__(self):
		if self.is_empty():
			return "Arbre vide"
		return self.breadth_first_print()
	#get the root
	def root( self ):
		return self._root
	
	#ask if the tree is empty
	def is_empty( self ):
		return self._size <= 0

	#ask if a position is a leaf
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
	##Descendre l'arbe avec coordoonee bateau#####################
	def _subtree_search( self, noeud, x,y):
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
	##Descendre l'arbr avec coordonnee bombe###########################
	def _interne_arbre_cherche( self, noeud, x1,x2,y1,y2):
		#Trouver le noeud interne associé aux coordonnes x,y
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
				item_interne = self._Item(noeud._element._milieu_x,noeud._element._x2,noeud._element._y1,noeud._element._milieu_y)   #On créer un nouveau item interne avec nouveau dimension
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
				item_interne = self._Item(noeud._element._milieu_x,noeud._element._x2,noeud._element._milieu_y,noeud._element._y2)   #On créer un nouveau item interne avec nouveau dimension
				self._size += 1
				noeud._sE._element = item_interne           #On change l'élément de l'enfant nord oeust	
				self.ajouter_element(noeud._sE,backup_feuille)				#On ajoute le backup feuille au nouveau noeud
				return self.ajouter_element(noeud._sE,elem)							#On ajoute l'élement au nouveau noeud

		if noeud.go_sO(x,y):
			if noeud._sO is None:						#Si l'enfant sud oeust n'est pas null
				return self._add_sO(noeud, elem )					#On ajoute l'élément
			if noeud._sO._element._est_interne:             	#si l'enfant sud Ouest pointe vers un arbre interne
				p_walk = self._subtree_search(noeud._sO, x,y )								#Marcher vers sud ouest
				return ajouter_element(p_walk,elem)			#ajouter recursif à la position final

			if not noeud._sO._element._est_interne:											#Si l'enfant nord Ouest appartient deja une feuille
				if noeud._sO._element == elem:
					raise ValueError( 'Coordonnée se ressemble' )
				backup_feuille = noeud._sO._element    # On backup la feuille
				item_interne = self._Item(noeud._element._x1,noeud._element._milieu_x,noeud._element._milieu_y,noeud._element._y2)   #On créer un nouveau item interne avec nouveau dimension
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
					
	###SUPRIMER BATEAU####################################################################################################################
	#Ici on cherche le bateau appartient à quel quadrant parent, puis supprimer le bateau correspodant 
	#et SI le quadrant n'a aucun enfant, supprimer le quadrant
	########################################################################################################################
	def supprimer_feuille(self,noeud):
		if noeud._parent._nO is not None and not noeud._parent._nO._element._est_interne and noeud._parent._nO._element == noeud._element:
			noeud._parent._nO = None    #Changer pointeur parent enfant à None
			if not self.has_children(noeud._parent):	#Si Noeud-Parent n'a plus d'enfant, supprimer quadrant parent
				self.supprimer_noeud_interne(noeud._parent)
			noeud._parent = None		#Pointer le parent du noeud à None
			self._size -= 1
			return
			#print("Parent du noeud nord-oeust supprimé: " + str(noeud._parent))
		if noeud._parent._nE is not None and not noeud._parent._nE._element._est_interne and noeud._parent._nE._element == noeud._element:
			noeud._parent._nE = None	#Changer pointeur parent enfant à None
			if not self.has_children(noeud._parent):	#Si Noeud-Parent n'a plus d'enfant, supprimer quadrant parent
				self.supprimer_noeud_interne(noeud._parent)
			noeud._parent = None	#Pointer le parent du noeud à None
			self._size -= 1
			return
			#print("Parent du noeud nord-est supprimé: " + str(noeud._parent))
		if noeud._parent._sE is not None and not noeud._parent._sE._element._est_interne and noeud._parent._sE._element == noeud._element:
			noeud._parent._sE = None	#Changer pointeur parent enfant à None
			if not self.has_children(noeud._parent):	#Si Noeud-Parent n'a plus d'enfant, supprimer quadrant parent
				self.supprimer_noeud_interne(noeud._parent)
			noeud._parent = None	#Pointer le parent du noeud à None
			self._size -= 1
			return
			#print("Parent du noeud sud-est supprimé: " + str(noeud._parent))
		if noeud._parent._sO is not None and not noeud._parent._sO._element._est_interne and noeud._parent._sO._element == noeud._element:
			noeud._parent._sO = None	#Changer pointeur parent enfant à None
			if not self.has_children(noeud._parent):	#Si Noeud-Parent n'a plus d'enfant, supprimer quadrant parent
				self.supprimer_noeud_interne(noeud._parent)
			noeud._parent = None	#Pointer le parent du noeud à None
			self._size -= 1
			return
			#print("Parent du noeud sud-oeust supprimé: " + str(noeud._parent))
		#print("Noeud supprimé: " + str(noeud))

	#####SUPPRIMER QUADRANT#########################################################################################################################
	#Ici on cherhce le quadrant appartient à quel quadrant parent, puis supprimer le quadrant correspondant
	#et SI le quadrant parent n'a plus d'enfant, supprimer le quadrant parent
	#############################################################################################################################
	def supprimer_noeud_interne(self,noeud):
		if(self.root()._element == noeud._element):
			self._size = 0
			#print("Racine supprimer")
			return
		if noeud._parent._element == noeud._element:
			return
		if (noeud._parent is not None and noeud._parent._nO is not None and noeud._parent._nO._element._est_interne and noeud._parent._nO._element == noeud._element):
			noeud._parent._nO = None	#Changer pointeur parent enfant à None
			if not self.has_children(noeud._parent):
				self.supprimer_noeud_interne(noeud._parent)
			noeud._parent = None	#Pointer le parent du noeud à None
			self._size -= 1
			#print("Parent du noeud interne nord-oeust supprimé: " + str(noeud._parent))
			return
		if(noeud._parent._nE is not None and noeud._parent._nE._element._est_interne and noeud._parent._nE._element == noeud._element):
			noeud._parent._nE = None	#Changer pointeur parent enfant à None
			if not self.has_children(noeud._parent):
				self.supprimer_noeud_interne(noeud._parent)
			noeud._parent = None	#Pointer le parent du noeud à None
			self._size -= 1
			return
			#print("Parent du noeud interne nord-est supprimé: " + str(noeud._parent))
		if(noeud._parent._sE is not None and noeud._parent._sE._element._est_interne and noeud._parent._sE._element == noeud._element):
			noeud._parent._sE = None	#Changer pointeur parent enfant à None
			if not self.has_children(noeud._parent):
				self.supprimer_noeud_interne(noeud._parent)
			noeud._parent = None	#Pointer le parent du noeud à None
			self._size -= 1
			return
			#print("Parent du noeud interne sud-est supprimé: " + str(noeud._parent))
		if(noeud._parent._sO is not None and noeud._parent._sO._element._est_interne and noeud._parent._sO._element == noeud._element):
			noeud._parent._sO = None	#Changer pointeur parent enfant à None
			if not self.has_children(noeud._parent):
				self.supprimer_noeud_interne(noeud._parent)
			noeud._parent = None	#Pointer le parent du noeud à None
			self._size -= 1
			return
				#print("Parent du noeud interne sud-oeust supprimé: " + str(noeud._parent))
			#print("Noeud interne supprimé: " + "(" + str(noeud._element._x1) + ", " + str(noeud._element._y1) + ") (" + str(noeud._element._x2) + ", " + str(noeud._element._y2) + ")")
	
	def test_bombes(self,x1,x2,y1,y2):
		noeud = self._root
		self.bombes(noeud,x1,x2,y1,y2)
	def bombes(self,racine,x1,x2,y1,y2):
		#print("Bombes:"+"("+str(x1)+","+str(y1)+")("+str(x2)+","+str(y2)+")")
		noeud_bombes = self._Item(x1,x2,y1,y2)
		noeud = self._interne_arbre_cherche(racine,x1,y1,x2,y2)	#Descendre les arbres internes tant que bombe se trouve dans quadrant
		
		#Si le noeud est un bateau et il se trouve à l'interieur coordonee bombe, alors supprimer le bateau et return vide
		if not noeud._element._est_interne and x1 <= noeud._element._xx <= x2 and y1 <= noeud._element._yy <= y2:
			self.supprimer_feuille(noeud)
			return																		
		
		#Si noeud est un quadrant
		if noeud._element._est_interne:
			#Si le quadrant se trouve à l'interieur coordonne bombe, alors supprimer le quadrant et retourner vide
			if x1 <= noeud._element._x1 and noeud._element._x2 <= x2 and y1 <= noeud._element._y1 and noeud._element._y2 <= y2:
				self.supprimer_noeud_interne(noeud)
				return
			if noeud._nO is not None:  #Si enfant Nord-Ouest existe
				#Si enfant Nord-Ouest est un bateau et il se trouve à l'interieur de coordoonee bombe, alors supprimer bateaux Nord-Ouest
				if not noeud._nO._element._est_interne and x1 <= noeud._nO._element._xx <= x2 and y1 <= noeud._nO._element._yy <= y2:
					self.supprimer_feuille(noeud._nO)
				#Si enfant Nord-Ouest est un quadrant
				elif noeud._nO._element._est_interne:
					#Si le quadrant se trouve à l'interieur de coordonnee bombe, supprimer le quadrant Nord-Ouest
					if x1 <= noeud._nO._element._x1 and noeud._nO._element._x2 <= x2 and y1 <= noeud._nO._element._y1 and noeud._nO._element._y2 <= y2: 
						self.supprimer_noeud_interne(noeud._nO)
					#Sinon si une partie de la bombe se trouve dans quadrant Nord-Ouest, alors operation recursif de methode bombes pour quadrant Nord-Ouest
					elif (noeud._nO._element._x1 <= x1 <= noeud._nO._element._x2  or noeud._nO._element._x1 <= x2 <= noeud._nO._element._x2) and (noeud._nO._element._y1 <= y1 <= noeud._nO._element._y2 or noeud._nO._element._y1 <= y2 <= noeud._nO._element._y2):
						self.bombes(noeud._nO,x1,x2,y1,y2)
			if noeud._nE is not None: #Si enfant Nord-Est existe
				#Si enfant Nord-Est est un bateau et il se trouve à l'interieur coordonne bombe, alors supprimer bateau Nord-Est
				if not noeud._nE._element._est_interne and x1 <= noeud._nE._element._xx <= x2 and y1 <= noeud._nE._element._yy <= y2:	
						self.supprimer_feuille(noeud._nE)	
				#Sinon si enfant Nord-Est est un quadrant
				elif noeud._nE._element._est_interne:
					#Si le quadrant se trouve à l'interieur de coordonnee bombe, alors supprimer le quadrant Nord-Est
					if x1 <= noeud._nE._element._x1 and noeud._nE._element._x2 <= x2 and y1 <= noeud._nE._element._y1 and noeud._nE._element._y2 <= y2: 
						self.supprimer_noeud_interne(noeud._nE)
					#Sinon si une partie de la bombe se trouve dans quadrant Nord-Est, alors operation recursif de methode bombes pour quadrant Nord-Est
					elif (noeud._nE._element._x1 <= x1 <= noeud._nE._element._x2 or noeud._nE._element._x1 <= x2 <= noeud._nE._element._x2) and (noeud._nE._element._y1 <= y1 <= noeud._nE._element._y2 or noeud._nE._element._y1 <= y2 <= noeud._nE._element._y2):	
						self.bombes(noeud._nE,x1,x2,y1,y2)
			if noeud._sE is not None:	#Si enfant Sud-Est existe
				#Si endant Sud-Est est un bateau et il se trouve à l'interieur de coordoonee bombe, alors supprimer bateau Sud-Est
				if not noeud._sE._element._est_interne and x1 <= noeud._sE._element._xx <= x2 and y1 <= noeud._sE._element._yy <= y2:
						self.supprimer_feuille(noeud._sE)
				#Sinon si enfant Surd-Est est un quadrant
				elif noeud._sE._element._est_interne:
					#Si le quadrant se trouve à l'interieur de coordonnee bombe, alors supprimer le quadrant Sud-Est
					if x1 <= noeud._sE._element._x1 and noeud._sE._element._x2 <= x2 and y1 <= noeud._sE._element._y1 and noeud._sE._element._y2 <= y2: 
						self.supprimer_noeud_interne(noeud._sE)
					#Sinon si une partie de la bombe se trouve dans quadrant Sud-Est, alors operation recursif de methode bombes pour quadrant Sud-Est
					elif (noeud._sE._element._x1 <= x1 <= noeud._sE._element._x2 or noeud._sE._element._x1 <= x2 <= noeud._sE._element._x2) and (noeud._sE._element._y1 <= y1 <= noeud._sE._element._y2 or noeud._sE._element._y1 <= y2 <= noeud._sE._element._y2):
						self.bombes(noeud._sE,x1,x2,y1,y2)
			if noeud._sO is not None: #Si enfant Sud-Ouest existe
				#Si enfant Sud-Ouest est un bateaux et il se trouve à l'interieur coordonnee bombe, alors supprimer bateaux Nord-Ouest
				if not noeud._sO._element._est_interne and x1 <= noeud._sO._element._xx <= x2 and y1 <= noeud._sO._element._yy <= y2:
						self.supprimer_feuille(noeud._sO)
				#Sinon si enfant Sud-Ouest est un quadrant
				elif noeud._sO._element._est_interne:
					#Si le quadrant se trouve à l'interieur de coordonnee bombe, alors supprimer le quadrant Sud-Ouest
					if x1 <= noeud._sO._element._x1 and noeud._sO._element._x2 <= x2 and noeud._sO._element._y1 >= y1 and noeud._sO._element._y2 <= y2:
						self.supprimer_noeud_interne(noeud._sO)
					#Sinon si une partie de la bombe se trouve dans quadrant Sud-Ouest, alors operation recursif de bombes pour quadrant Sud-Ouest
					elif (noeud._sO._element._x1 <= x1 <= noeud._sO._element._x2 or noeud._sO._element._x1 <= x2 <= noeud._sO._element._x2) and (noeud._sO._element._y1 <= y1 <= noeud._sO._element._y2 or noeud._sO._element._y1 <= y2 <= noeud._sO._element._y2):
						self.bombes(noeud._sO,x1,x2,y1,y2)				

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
					if c._element._est_interne:
						table1.appendleft(c)
				if len(table)== 0 and not len(table1) == 0:
					if not len(table1) == 0:
						mot += "\n"
						table = table1.copy()
						table1.clear()
		else:
			mot = "Tree is empty"
		return mot
		