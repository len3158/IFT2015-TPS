"""
En utilisant la méthode de Horner pour la fonction de hashage:
https://en.wikipedia.org/wiki/Horner%27s_method
"""

class HasTable:
	
	def __init__(self, cap=11, p=109345121, somme=33):
		self._Tableau = cap*[None] #taille par defaut lors de l'appel
		self._taille = 0
		self._premier = p				#nombre premier pour compression MAD
		self._polynome = somme		#33 peut-être évaluer autre valeur? à voir
		self._echelle = 1 + randrange(p-1)	#echelle MAD
		self._shift = randrange(p)	#décalage pour MAD
		
	def __len__(self):
		return self._size
		
	def __setitem__(self, k):
		iterateur = self._compress(self._hash_(k))
		self._append(iterateur, key)
	def __getitem__(self, k):
		iterateur = self._compress(self._hash_(k))
	def __delete_item__(self,k):
		
	def _get_bucket(self, i, k):
		bucket = self._Tableau[i]
		if bucket is not None:
			try:
				value = bucket._index(k)
			except ValueError:
				return None
			return bucket[value]
			
	def _append(self, i,k):
		if self._Tableau[i] is None:
			self._Tableau[i] = []	#créer un nouveau sceau
		if k in self._Tableau[i] is None:
			self._Tableau.append(k)
			self._taille += 1	
	
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
	
	