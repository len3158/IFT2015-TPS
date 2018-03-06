"""Code Python pour le cours IFT2015
   Mise à jour par François Major le 23 mars 2014.

   Pris dans Goodrich, Tamassia & Goldwasser
   Data Structures & Algorithms in Python (c)2013
"""
from ArrayQueue import ArrayQueue
    
#ADT Tree "interface"
class Tree:

    #inner class position
    class Position:

        def element( self ):
            pass

        def __eq__( self, other ):
            pass

        def __ne__( self, other):
            return not( self == other )

    #get the root
    def root( self ):
        pass

    #get the parent
    def parent( self, p ):
        pass

    #get the number of children
    def num_children( self, p ):
        pass

    #get the children
    def children( self, p ):
        pass

    #get the number of nodes
    def __len__( self ):
        pass

    #ask if a position is the root
    def is_root( self, p ):
        return self.root() == p

    #ask if a position is a leaf
    def is_leaf( self, p ):
        return self.num_children( p ) == 0

    #ask if the tree is empty
    def is_empty( self ):
        return len( self ) == 0


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
            
