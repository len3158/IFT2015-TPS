"""
Notre classe dictionnaire

En utilisant la méthode de Horner pour la fonction de hashage:
https://en.wikipedia.org/wiki/Horner%27s_method

"""
from random import randrange
from Bucket import Bucket
from Bucket1 import Bucket1
import time
class Tp2_1055234_1047837_b1:
	def __init__(self,cap = 786433, p = 109345121):
		self._taille = cap
		start_time = time.time()
		self._Tableau = self._taille * [None] #taille par defaut lors de l'appel
		#print(str(time.time() - start_time))
		self._premier = p				#nombre premier pour compression MAD
		self._coefficient = 33		#33 peut-être évaluer autre valeur? à voir
		self._echelle = 1 + randrange(self._premier-1)	#echelle MAD
		self._shift = randrange(self._premier)	#décalage pour MAD
		self._nbElem = 0
		#self._keys = Bucket1()	 #keep track of all inserted keys pour la distance
		self._index = Bucket1()		#List des index à utiliser pour la methode items
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
			#self._keys.append(k)
			self._nbElem += 1
	
	"""Inserer une clée sans valeur associee a la cle k dans la hashTable"""
	def insert(self, k):
		iterateur = self._hash_(k)
		i = self._compress(iterateur)
		existe = self._bucket_insert(i, k)
		if self._nbElem > len(self._Tableau)//2:
			print("il fait appel a resize")
			self._resize(2*len(self._Tableau)-1)
		if not existe:
			#self._keys.append(k)
			self._nbElem += 1
			
	"""Generate a sequence of key in the map"""
	def __iter__(self):
		for bucket in self._index:
			for k in bucket:
				yield k

	"""Generate a sequence of (k,v) tuples for all entries of M"""
	def __items__(self):
		for bucket in self._index:
			for k,v in bucket.__items__():
				yield (k,v)
			
	def generatebucket(self):
		for bucket in self._index:
			yield bucket
			
	#def keys(self):
	#	return self._keys
		
		
	def nbIndex(self):
		return len(self._index)
	
	
	def __contains__(self,k):
		value = self.__getitem__(k)
		if value is None:
			return False
		else:
			return True
	
	# def __str__(self):	
		# pp = "Taille de table: "+ str(self._taille) + "\n"
		# for i in self._index:
			# pp += "Index: " + str(i)
			# pp += str(self._Tableau[i])
			# pp += "\n"
		# return pp
	
	
	"""Retourner la valeur associee a la cle k"""
	def __getitem__(self, k):
		iterateur = self._hash_(k)
		i = self._compress(iterateur)
		return self._bucket_getitems(i, k)
		
	def _bucket_getitems(self,i,k):
		bucket = self._Tableau[i]
		if bucket is not None:
			return bucket[k]
		return None		#If bucket is None
			
	def _bucket_setitem(self,i,k,v):
		if self._Tableau[i] is None:
			self._Tableau[i] = Bucket()
			self._index.append(self._Tableau[i])
			self._Tableau[i].add_first(k,v)
			return False
		return self._Tableau[i]._setitem(k,v)	
	

	def _bucket_insert(self, i,k):
		if self._Tableau[i] is None:
			self._Tableau[i] = Bucket()
			self._index.append(self._Tableau[i])
			self._Tableau[i].add_first(k)
			return False
		return self._Tableau[i].insert(k)

			
	"""Grows the table as more keys are added
		http://www.orcca.on.ca/~yxie/courses/cs2210b-2011/htmls/extra/PlanetMath_%20goodhashtable.pdf"""
	def _resize(self, newSize):		#Est ce qu'on utilise l'attribut newSize?
		listePremiers = [7, 53, 97, 193, 389, 769, 1543, 3079, 6151, 12289, 24593, 49157, 98317, 196613, 393241, 786433, 1572869, 3145739, 6291469, 12582917, 25165843, 50331653, 100663319, 201326611, 402653189, 805306457, 1610612741]
		i = listePremiers.index(self._taille)
		print("On a appeller resize")
		while i < len(listePremiers):
			#print("i= "+str(i))
			#print("nbElem= "+str(self._nbElem))
			#print("TabLen= "+str(len(self._Tableau)))
			#print("listepremier= "+str(listePremiers[i]))
			if self._nbElem > (len(self._Tableau)//2):
				#self._indice_premier = i+1
				#print("true")
				old = list(self.__items__())
				self._index = Bucket1()
				#self._keys = Bucket1()
				print("Redimension de la table de (" + str(self._taille) + ") a (" + str(listePremiers[i+1]) +")")
				self._Tableau = listePremiers[i+1] * [None]
				self._taille = listePremiers[i+1]
				#print(str(self._taille))
				#self._premier = listePremiers[i+1]
				self._nbElem = 0
				if old is not None:
					for tt in old:
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
	
	