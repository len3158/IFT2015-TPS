"""
La classe principale du dictionnaire Abstrait
**Auteurs: - Mehran ASADI. Matricule: 1047837
		   - Lenny SIEMENI. Matricule: 1055234**
En utilisant la méthode de Horner pour la fonction de hashage:
https://en.wikipedia.org/wiki/Horner%27s_method

Et en utilisant la methode des "buckets", et la compression MAD
pour la gestion des collisions

Inspire du code vu en classe par François Major le 23 mars 2014
dans le cadre du cours IFT2015.
"""

from random import randrange
from Bucket import Bucket
from Index import Index
import time

class Dictionnaire:
	def __init__(self,cap = 786433, p = 109345121):
		self._taille = cap
		start_time = time.time()
		self._Tableau = self._taille * [None] #taille par defaut lors de l'appel
		self._premier = p				#nombre premier pour compression MAD
		self._coefficient = 33		
		self._echelle = 1 + randrange(self._premier-1)	#echelle MAD
		self._shift = randrange(self._premier)	#décalage pour MAD
		self._nbElem = 0
		self._index = Index()		#Liste des index à utiliser pour la methode items
		self._indice_premier = 0    #keep track of prime number in prime liste
		
	def __len__(self):
		return len(self._Tableau)
		
	"""Inserer valeur associee a la cle k dans la hashTable"""
	def __setitem__(self, k, v):
		iterateur = self._hash_(k)
		i = self._compress(iterateur)
		existe = self._bucket_setitem(i, k, v)
		if self._nbElem > len(self._Tableau)//2:	#load factor
			self._resize(2*len(self._Tableau)-1)
		if not existe:
			self._nbElem += 1

	
	"""Inserer une clée k sans valeur dans la hashTable"""
	def insertKey(self, k):
		iterateur = self._hash_(k)
		i = self._compress(iterateur)
		existe = self._bucket_insertKey(i, k)
		if self._nbElem > len(self._Tableau)//2:	#load factor
			self._resize(2*len(self._Tableau)-1)
		if not existe:
			self._nbElem += 1
			
	"""Generate a sequence of key in the map"""
	def __iter__(self):
		for bucket in self._index:
			for k in bucket:
				yield k

	"""Generate a sequence of (k,v) tuples for all entries of M"""
	def __items__(self):
		for index in self._index:
			for k,v in index.__items__():
				yield (k,v)

	"""Iterateur"""	
	def generatebucket(self):
		for index in self._index:
			yield index
	
	"""Retourne la longueur de la liste d'indexes contenant un bucket"""	
	def nbIndex(self):
		return len(self._index)
	
	"""Determine si la cle se trouve dans notre dictionnaire"""
	def __contains__(self,k):
		value = self.__getitem__(k)
		if value is None:
			return False
		else:
			return True
	
	"""Retourner la valeur associee a la cle k"""
	def __getitem__(self, k):
		iterateur = self._hash_(k)
		i = self._compress(iterateur)
		return self._bucket_getitems(i, k)
	
	"""Retourner le bucket associe a la collision a l'indice i"""
	def _bucket_getitems(self,i,k):
		bucket = self._Tableau[i]
		if bucket is not None:
			return bucket[k]
		return None
	
	"""Instancier le bucket associe a la collision a l'indice i"""
	def _bucket_setitem(self,i,k,v):
		if self._Tableau[i] is None:
			self._Tableau[i] = Bucket()
			self._index.append(self._Tableau[i])
			self._Tableau[i].add_first(k,v)
			return False
		return self._Tableau[i]._setitem(k,v)	
	
	"""Inserer la collision dans le bucket a l'indice i"""
	def _bucket_insertKey(self, i,k):
		if self._Tableau[i] is None:
			self._Tableau[i] = Bucket()			#si pas de sceau a cet index, on en instancie un
			self._index.append(self._Tableau[i])	#on append la cle
			self._Tableau[i].add_first(k)			
			return False
		return self._Tableau[i].insertKey(k)
			
	"""Agrandit la table si le load factor est en desequilibre
	liste optimale de nombre premiers pour la taille de la table:
		http://www.orcca.on.ca/~yxie/courses/cs2210b-2011/htmls/extra/PlanetMath_%20goodhashtable.pdf"""
	def _resize(self, newSize):
		listePremiers = [7, 53, 97, 193, 389, 769, 1543, 3079, 6151, 12289, 24593, 49157, 98317, 196613, 393241, 786433, 1572869, 3145739, 6291469, 12582917, 25165843, 50331653, 100663319, 201326611, 402653189, 805306457, 1610612741]
		i = listePremiers.index(self._taille)
		while i < len(listePremiers):
			if self._nbElem > (len(self._Tableau)//2):
				old = list(self.__items__())
				self._index = Index()
				self._Tableau = listePremiers[i+1] * [None]
				self._taille = listePremiers[i+1]
				self._nbElem = 0
				if old is not None:
					for tt in old:
						self.__setitem__(tt[0],tt[1])
				return
	
	"""Utilitaire pour appeler la fonction de hasahage"""
	def _hash_(self,k):
			return self._horner_method(k)

	"""Fonction de hashage"""
	def _horner_method(self, k):
		if len(k) <= 1:
			return ord(k[0])
		else:
			return  ord(k[0]) + self._coefficient*self._horner_method(k[1:])	#ord retourne le char en entier (coefficient)
		
	"""Fonction de compression en utilisant la methode MAD"""
	def _compress(self, hash_value):
		return (hash_value*self._echelle+self._shift)%self._premier%len(self._Tableau)