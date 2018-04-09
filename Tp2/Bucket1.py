"""Code Python pour le cours IFT2015
   Mise à jour par François Major le 23 mars 2014.
"""
class Bucket1():

	class _Node:

		def __init__( self, doublet = None, next = None):
			__slots__ = '_doublet','_next'
			self._doublet = doublet
			self._next = next
			
		
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
			yield curr._doublet
			curr = curr._next
			
	def __contains__(self,doublet):
		noeud = self.find(doublet)
		if noeud is not None:
			return True
		return False

	def append( self, doublet):
		newNode = self._Node( doublet, None)
		if self._tail == None:
			self._head = self._tail = newNode
		else:
			self._tail._next = newNode
			self._tail = newNode
		self._size += 1

