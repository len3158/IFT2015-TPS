"""
Notre classe dictionnaire

En utilisant la méthode de Horner pour la fonction de hashage:
https://en.wikipedia.org/wiki/Horner%27s_method

"""
from random import randrange
from Bucket import Bucket
import sys
class Tp2_1055234_1047837_b1:
	sys.setrecursionlimit(1500)
	def __init__(self,cap = 786433, p = 109345121):
		self._taille = cap
		self._Tableau = self._taille * [None] #taille par defaut lors de l'appel
		self._premier = p				#nombre premier pour compression MAD
		self._coefficient = 33		#33 peut-être évaluer autre valeur? à voir
		self._echelle = 1 + randrange(self._premier-1)	#echelle MAD
		self._shift = randrange(self._premier)	#décalage pour MAD
		self._nbElem = 0
		self._keys = Bucket()	 #keep track of all inserted keys pour la distance
		self._index = Bucket()		#List des index à utiliser pour la methode items
		self._indice_premier = 0 #keep track of prime number in prime list
		
	def __len__(self):
		return len(self._Tableau)
		
	"""Inserer valeur associee a la cle k dans la hashTable"""
	def __setitem__(self, k, v):
		iterateur = self._hash_(k)
		i = self._compress(iterateur)
		existe = self._bucket_setitem(i, k, v)
		if self._nbElem > len(self._Tableau)//2:
			self._resize(2*len(self._Tableau)-1)
		if not existe:
			self._keys.append(k)
			self._nbElem += 1
	
	"""Inserer une clée sans valeur associee a la cle k dans la hashTable"""
	def insert(self, k):
		iterateur = self._hash_(k)
		i = self._compress(iterateur)
		existe = self._bucket_insert(i, k)
		if self._nbElem > len(self._Tableau)//2:
			self._resize(2*len(self._Tableau)-1)
		if not existe:
			self._keys.append(k)
			self._nbElem += 1
			
	"""Generate a sequence of key in the map"""
	def __iter__(self):
		for key in self._keys:
			yield key

	"""Generate a sequence of (k,v) tuples for all entries of M"""
	def __items__(self):
		for i in self._index:
			yield list(self._Tableau[i].__items__())
			
	def keys(self):
		return self._keys
	
	def __str__(self):
		
		pp = "Taille de table: "+ str(self._taille) + "\n"
		for i in self._index:
			pp += "Index: " + str(i)
			pp += str(self._Tableau[i])
			pp += "\n"
		return pp
	
	
	"""Retourner la valeur associee a la cle k"""
	def __getitem__(self, k):
		iterateur = self._hash_(k)
		i = self._compress(iterateur)
		return self._bucket_getitems(i, k)
		
	def __delitem__(self,k):
		iterateur = self._hash_(k)
		i = self._compress(iterateur)
		if self._bucket_deleteitem(i,k):
			self._nbElem -= 1
			del self._keys[k]
		
	def _bucket_getitems(self,i,k):
		bucket = self._Tableau[i]
		if bucket is not None:
			return bucket[k]
		return None		#If bucket is None
			
	def _bucket_setitem(self,i,k,v):
		if self._Tableau[i] is None:
			self._Tableau[i] = Bucket()
			self._index.append(i)
		return self._Tableau[i]._setitem(k,v)	
	

	def _bucket_insert(self, i,k):
		if self._Tableau[i] is None:
			self._Tableau[i] = Bucket()
			self._index.append(i)
		return self._Tableau[i].insert(k)
	
	def _bucket_deleteitem(self, i, k):
		bucket = self._Tableau[i]
		if bucket is None:
			return False
		succes = bucket.remove(k)
		if bucket.is_empty():
			self._T = None
			del self._index[i]
		return succes
			
	"""Grows the table as more keys are added
		http://www.orcca.on.ca/~yxie/courses/cs2210b-2011/htmls/extra/PlanetMath_%20goodhashtable.pdf"""
	def _resize(self, newSize):		#Est ce qu'on utilise l'attribut newSize?
		listePremiers = [7, 53, 97, 193, 389, 769, 1543, 3079, 6151, 12289, 24593, 49157, 98317, 196613, 393241, 786433, 1572869, 3145739, 6291469, 12582917, 25165843, 50331653, 100663319, 201326611, 402653189, 805306457, 1610612741]
		i = listePremiers.index(self._taille)
		#print("i= "+str(i))
		while i < len(listePremiers):
			#print("i= "+str(i))
			#print("nbElem= "+str(self._nbElem))
			#print("TabLen= "+str(len(self._Tableau)))
			#print("listepremier= "+str(listePremiers[i]))
			if self._nbElem > (len(self._Tableau)//2):
				#self._indice_premier = i+1
				#print("true")
				old = list(self.__items__())
				self._index = Bucket()
				self._keys = Bucket()
				print("Redimension de la table de (" + str(self._taille) + ") a (" + str(listePremiers[i+1]) +")")
				self._Tableau = listePremiers[i+1] * [None]
				self._taille = listePremiers[i+1]
				#print(str(self._taille))
				self._premier = listePremiers[i+1]
				self._nbElem = 0
				if old is not None:
					for ss in old:
						for tt in ss:
							self.__setitem__(tt[0],tt[1])
			
			return
			#break
		
		
	def _hash_(self,k):
			return self._horner_method(k)
	
	"""Fonction de hashage"""
	def _horner_method(self, k):
		if len(k) <= 1:
			return ord(k[0])
		else:
			return  ord(k[0]) + self._coefficient*self._horner_method(k[1:])	#ord retourne le char en entier (coefficient)
		
	"""En utilisant la methode MAD"""
	def _compress(self, hash_value):
		return (hash_value*self._echelle+self._shift)%self._premier%len(self._Tableau)
	
	