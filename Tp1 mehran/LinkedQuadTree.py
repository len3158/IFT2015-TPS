
from QuadTree import QuadTree

class LinkedQuadTree( QuadTree ):
    
    #inner class Feuille
	class _Feuille:
		__slots__ = '_xx', '_yy'
		def __init__(x,y,parent = None):
			self._xx= x
			self._yy = y
	#inner class Feuille
	class _Item:
		__slots__ = '_x1', '_x2','_y1', '_y2'
		def __init__(self, x1,x2,y1,y2):
			self._x1 = x1
			self._x2 = x2
			self._y1 = y1
			self._y2 = y2
			self._milieu_x = (x1+x2)//2
			self._milieu_y = (y1+y2)//2
	#inner class Node	
	class _Node:

    #inner class Position, a subclass of BinaryTree Position
		__slots__ = '_feuille','_x1','_x2', '_parent', '_no', '_ne', '_se', '_so'
		def __init__( self, elem, parent = None, no = None, ne = None, se = None, so = None ):
			self._element = elem
			self._parent = parent
			self._nO = no
			self._nE = ne
			self._sE = se
			self._sO = so
			self._est_interne = (type( elem ) is type( self._Item ))
			
        def same_type( self, other ):
            return type( other ) is type( self )
		
		def go_nO(self,x,y):
			return x < self._element._milieu_x and y < self._element._milieu_y
		def go_nE(self,x,y):
			return x < self._element._milieu_x and y > self._element._milieu_y
		def go_sE(self,x,y):
			return x > self._element._milieu_x and y > self._element._milieu_y	
		def go_sE(self,x,y):
			return x > self._element._milieu_x and y < self._element._milieu_y
    #inner class Position, a subclass of BinaryTree Position
   class Position( QuadTree.Position ):

        #init specifies the Tree container and uses _Node to store the element
        def __init__( self, container, node ):
            self._container = container
            self._node = node

        def __str__( self ):
            return str( self._node._element )

        def element( self ):
            return self._node._element

        def __eq__( self, other ):
            return type( other ) is type( self ) and other._node is self._node
			

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
        self._root = self._Node(e)
        return self._make_position( self._root )

		
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
	def add_leaf(self,x,y):
		feuille = self._Feuille(x,y)
		return self._make_position(feuille)
	
	def _subtree_search( self, p, x,y ):
		
		node = self._validate( p )			#Trouver le noeud associé à la position
        #return the Position with key k in subtree rooted at p
        #or the last node visited.
        if x == node._element._milieu and y == node._element._milieu:
            #Position with key k found
            return p
		elif node.go_nO(x,y):
            #Position with key k perhaps in left subtree
            if self.nord_O( p ) is not None:
                return self._subtree_search( self.nord_O( p ), x,y )
        elif node.go_nE(x,y):
            #Position with key k perhaps in right subtree
            if self.nord_E( p ) is not None:
                return self._subtree_search( self.nord_E( p ), x,y )
		 elif node.go_sE(x,y):
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
		if not noeud_position._est_interne:                 #Si le noeud de la position est une feuille
			p = self.parent(p)								# Trouver le pointeur parent
			noeud_position = self._validate(p)			    # trouver le noeud du parent
		
		if noeud_position.go_nO(x,y):						#Si la les coordoonée sont dans nord ouest
			if noeud_position._nO is None					#Si l'enfant nord oeust n'est pas null
				return self._add_nO(p, elem )					#On ajoute l'élément
			if noeud_position._nO._est_interne:             #si l'enfant nord Ouest pointe vers un arbre interne
				p_walk = self.nord_O						#Marcher vers nord ouest
				p = ajouter_element(p_walk,elem)			#ajouter recursif à la position final
			else:											#Si l'enfant nord Ouest appartient deja une feuille
				backup_feuille = noeud_position._element    # On backup la feuille
				item_interne = self._Item(noeud_position._x1,noeud_position._milieu_x,noeud_position._y1,noeud_position._milieu_y)   #On créer un nouveau item interne avec nouveau dimension
				pp = self._add_nO(p,item_interne)										#On ajoute un nouveau enfant Nord Ouest avec le nouveau noeud
				ppp = self.ajouter_element(pp,backup_feuille)				#On ajoute le backup feuille au nouveau noeud
				p = self.ajouter_element(pp,elem)							#On ajoute l'élement au nouveau noeud
		
		elif noeud_position.go_nE(x,y):
			if noeud_position._nE is None					#Si l'enfant nord EST n'est pas null
				return self._add_nE(p, elem )					#On ajoute l'élément
			if noeud_position._nE._est_interne:             #si l'enfant nord EST pointe vers un arbre interne
				p_walk = self.nord_E						#Marcher vers nord EST
				p = ajouter_element(p_walk,elem)			#ajouter recursif à la position final
			else:											#Si l'enfant nord EST appartient deja une feuille
				backup_feuille = noeud_position._element    # On backup la feuille
				item_interne = self._Item(noeud_position._milieu_x,noeud_position._x2,noeud_position._y1,noeud_position._milieu_y)   #On créer un nouveau item interne avec nouveau dimension
				pp = self._add_nE(p,item_interne)										#On ajoute un nouveau enfant Nord EST avec le nouveau noeud
				ppp = self.ajouter_element(pp,backup_feuille)				#On ajoute le backup feuille au nouveau noeud
				p = self.ajouter_element(pp,elem)							#On ajoute l'élement au nouveau noeud
		
		elif noeud_position.go_sE(x,y):
			if noeud_position._sE is None					#Si l'enfant sud EST n'est pas null
				return self._add_sE(p, elem )					#On ajoute l'élément
			if noeud_position._sE._est_interne:             #si l'enfant sud EST pointe vers un arbre interne
				p_walk = self.sud_E						#Marcher vers sud EST
				p = ajouter_element(p_walk,elem)			#ajouter recursif à la position final
			else:											#Si l'enfant sud EST appartient deja une feuille
				backup_feuille = noeud_position._element    # On backup la feuille
				item_interne = self._Item(noeud_position._milieu_x,noeud_position._x2,noeud_position._milieu_y,noeud_position._y2)   #On créer un nouveau item interne avec nouveau dimension
				pp = self._add_sE(p,item_interne)										#On ajoute un nouveau enfant sud EST avec le nouveau noeud
				ppp = self.ajouter_element(pp,backup_feuille)				#On ajoute le backup feuille au nouveau noeud
				p = self.ajouter_element(pp,elem)							#On ajoute l'élement au nouveau noeud
	
		else:
			if noeud_position._sO is None						#Si l'enfant sud oeust n'est pas null
				return self._add_sO(p, elem )					#On ajoute l'élément
			if noeud_position._sO._est_interne:             	#si l'enfant sud Ouest pointe vers un arbre interne
				p_walk = self.sud_O								#Marcher vers sud ouest
				p = ajouter_element(p_walk,elem)			#ajouter recursif à la position final
			else:											#Si l'enfant nord Ouest appartient deja une feuille
				backup_feuille = noeud_position._element    # On backup la feuille
				item_interne = self._Item(noeud_position._x1,noeud_position._milieu_x,noeud_position._milieu_y,noeud_position._y2)   #On créer un nouveau item interne avec nouveau dimension
				pp = self._add_sO(p,item_interne)										#On ajoute un nouveau enfant sud Ouest avec le nouveau noeud
				ppp = self.ajouter_element(pp,backup_feuille)				#On ajoute le backup feuille au nouveau noeud
				p = self.ajouter_element(pp,elem)							#On ajoute l'élement au nouveau noeud
		return p
		
	
	#Remplacer le nouveau element à la position est retourner l'ancien 
	def ajouter( self,x,y ):
		feuille = self._Feuille(x,y)													#On créer une element feuille avec les coordonnée
        if self.is_empty():																#Si l'arbre n'existe pas
			item_root = self._Item(0,10315,0,10315)										#On creer un item interne racine
            p = self._add_root( item_root ) #from LinkedBinaryTree						#On creer un nouveau racine avec l'item 
			return self.ajouter_element(p,feuille)							# On ajoute la feuille a la racine et on retourn la position 
        else:
            p = self._subtree_search( self.root(), x,y )								#On cherche depuis la racine la position pour les coordonnée
			self.ajouter_element(p,feuille)
            
			
		
    def _replace( self, p, e ):
        node = self._validate( p )      #Trouver le noeud associé à la position
		if node._est_interne: return False
        old = node._element              #Creer un backup de l'ancien element
        node._element = e			    #Assigner le nouveau element a node
        return old

    #delete a position
    def _delete( self, p ):
        #remove node p and replace it with its child if any
        node = self._validate( p )    #Trouver le noeud associé à la position
        if num_children( p ) > 1: raise ValueError( 'p a plus d'un enfant' )
		child = None
		a 
		#Assigner l'enfant à child
		if node._nO is not None:
			child = node._nO
		if node._nE is not None:
			child = node._nE
		if node._sE is not None:
			child = node._sE
		if node._sO is not None:
			child = node._sO

        if child is not None:					#Si le noeud a un enfant, pointer parent child à parent noeud
            child._parent = node._parent
        if node is self._root:					#Si le noeud a une racine, pointer la racine à child
            self._root = child
        else:									#Sinon
            parent = node._parent				   #Pointer parent au parent du noeud correspondant
            if node is parent._nO:
                parent._nO = child
            elif node is parent._nE:
                parent._nE = child
            elif node is parent._sE:
                parent._sE = child
            else:
                parent._sO = child
        self._size -= 1
        #make the deleted node invalid
        node._parent = node
        return node._element