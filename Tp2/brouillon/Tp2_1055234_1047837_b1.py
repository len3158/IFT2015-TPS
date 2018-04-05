"""
Notre classe dictionnaire

En utilisant la méthode de Horner pour la fonction de hashage:
https://en.wikipedia.org/wiki/Horner%27s_method

"""
import random

class HasTable:
	
	def __init__(self, initSize):
		self._taille = 0
		self._Tableau = [None]*self._taille #taille par defaut lors de l'appel
		#self._premier = p				#nombre premier pour compression MAD
		self._coefficient = 33		#33 peut-être évaluer autre valeur? à voir
		self._echelle = 1 + randrange(self._premier-1)	#echelle MAD
		self._shift = randrange(self._premier)	#décalage pour MAD
		self._nbElem = 0
		self._keys =[]	#keep track of all inserted keys pour la distance
		
	def __len__(self):
		return self._taille = len(self._Tableau)
		
	"""Inserer valeur associee a la cle k dans la hashTable"""
	def __setitem__(self, k, v):
		iterateur = self._hash_(k)
		succes = self._bucket_setitem(iterateur, k, v)
		if self._n > len(self._Tableau)//2:
			self._resize(2*len(self._Tableau)-1)
		if succes:
			if k not in self._keys:		#keep track of inserted keys
				self._keys.append(k)	#insert new key
			return True
		else 
			return False
			
	"""Retourner la valeur associee a la cle k"""
	def __getitem__(self, k):
		iterateur = self._hash_(k)
		if self._Tableau[iterateur] is not None:
			return self._get_bucket(iterateur, k)
		return None
		
	def __delete_item__(self,k):
		iterateur = self._hash_(k)
		if self._bucket_deleteitem(iterateur,k):
			self._nbElem -= 1
		
	def _get_bucket(self, i, k):
		bucket = self._Tableau[i]
		if bucket is not None:
			try:
				value = bucket.[k]
			except IndexError:
				return None
			return bucket[value]
			
	def _bucket_setitem(self,i,k,v):
		bucket = self._Tableau[i]
		if bucket is None:
			bucket = []	#créer un nouveau sceau
		if k in bucket is None:
			bucket.append(k)
			self._taille += 1	
	
	def _bucket_deleteitem(self, i, k):
		try:
			if self._Tableau[i] is not None:
				
	
	"""Grows the table as more keys are added
		http://www.orcca.on.ca/~yxie/courses/cs2210b-2011/htmls/extra/PlanetMath_%20goodhashtable.pdf"""
	def _resize(self, newSize):
		listePremiers = [53, 97, 193, 389, 769, 1543, 3079, 6151, 12289, 24593, 49157, 98317, 196613, 393241, 786433, 1572869, 3145739, 6291469]
		
		for i in range(1, len(listePremiers)-1):
			if self.__len__ < 2*self.__len__:
				self._taille = listePremiers[i]
				self._premier = listePremiers[i]
				break;
		
	def _hash_(self,k):
			return self._horner_method(k)
			
	def _horner_method(self, k):
		if len(k)==1:
			return k
		else:
			return ord(k[0]) + self._coefficient*self._horner_method(k[1:])	#ord retourne le char en entier (coefficient)
		
	"""En utilisant la methode MAD"""
	def _compress(self, hash_value):
		return (hash_value*self._echelle+self._shit)%self._premier%len(self._table)
	
	