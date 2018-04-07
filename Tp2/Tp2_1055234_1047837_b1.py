"""
En utilisant la méthode de Horner pour la fonction de hashage:
https://en.wikipedia.org/wiki/Horner%27s_method
"""
from Bucket import Bucket
class HasTable:

	""" Class interne Item"""
	class _Item:
		__slots__ = '_key', '_value'

        def __init__( self, k, v = None ):
            self._key = k
            self._value = v

        def __eq__( self, other ):
            return self._key == other._key

        def __ne__( self, other ):
            return not( self == other )

        def __lt__( self, other ):
            return self._key < other._key

        def __ge__( self, other ):
            return self._key >= other._key

        def __str__( self ):
            return "<" + str( self._key ) + "," + str( self._value ) + ">"

        def key( self ):
            return self._key

        def value( self ):
            return self._value
			
	""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
	
	def __init__(self, cap=11, p=109345121, somme=33):
		self._Tableau = cap*[None] #taille par defaut lors de l'appel
		self._taille = 0
		self._premier = p				#nombre premier pour compression MAD
		self._polynome = somme		#33 peut-être évaluer autre valeur? à voir
		self._echelle = 1 + randrange(p-1)	#echelle MAD
		self._shift = randrange(p)	#décalage pour MAD
		self._index = []		# List des index à utiliser pour les methode iter et items
		
	def __len__(self):
		return self._size
		
	def __setitem__(self, k):
		iterateur = self._compress(self._hash_(k))
		self._append(iterateur, key)
	def __getitem__(self, k):
		iterateur = self._compress(self._hash_(k))
	def __delete_item__(self,k):
		
	
	"""Generate a sequence of key in the map"""
	def __iter__(self):
	
	"""Generate a sequence of (k,v) tuples for all entries of M"""
	def __items__(self):
	
	def _get_bucket_item(self, i, k):
		bucket = self._Tableau[i]
		if bucket is not None:
			return bucket[value]
		return False		#If bucket is None
	
	def _append(self, i,k):
		if self._Tableau[i] is None:
			self._Tableau[i] = Bucket()
		frequence = self._Tableau[i].insert(k)
		if frequence != 1:
			self._size += 1
	
	def _resize(self, newSize):
		
		
	def _hash_(self,k):
			return self._horner_method(self._polynome, obj)
			
	def _horner_method(self, polyValX, obj):
		hash_value = 0
		for x in obj:
			hash_value = x*hash_value + ord(c)	#ord retourne le char en entier (coefficient)
		return hash_value
		
	"""En utilisant la methode MAD"""
	def _compress(self, hash_value):
		return (hash_value*self._echelle+self._shit)%self._premier%len(self._table)
	
	