from Tree import Tree

class QuadTree( Tree ):

	#Obtenir l'children NordOuest
    def nord_O( self, p ):
        pass
		
	#Obtenir l'children NordEst
    def nord_E( self, p ):
        pass
		
	#Obtenir l'children SudEst
    def sud_E( self, p ):
        pass
		
	#Obtenir l'children SudOuest
    def sud_O( self, p ):
        pass


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
    


