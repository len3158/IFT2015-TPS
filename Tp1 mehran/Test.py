from LinkedQuadTree import LinkedQuadTree
import random
#class Test:

def isEmpty(nomFichier):
	e=open(nomFichier,'r')
	return e.read(0)

def	setQuadTreeFromFile(nomFichier):		
	boats = []
	mytree = LinkedQuadTree()
	try:
		f=open(nomFichier,'r')
	except FileNotFoundError:
		return None
	if not isEmpty(nomFichier):
		for line in f:
			line=(line.strip().split(' '))
			boats.append(list(map(int,line)))
		f.close()
		for x,y in boats:
			mytree.ajouter(x,y)
		return mytree
	else:
		limite = random.randint(1,1000)
		for _ in range(1000):
			x = random.randint(0, 10315)
			y = random.randint(0, 10315)
			mytree.ajouter(x,y)
		print('File {} not found/empty, creating an ocean with {} random boats...'.format(nomFichier, limite))
		return mytree

def bombarder(nomFichier, tree):
	bombs = []
	aDetruire = []
	try:
		f=open(nomFichier,'r')
	except FileNotFoundError:
		return None
	if not isEmpty(nomFichier):
		for line in f:
			line=(line.strip().split(' '))
#			line.insert(0,0)
#			line.insert(2,0)
			bombs.append(list(map(int,line)))
		f.close()
		for x,y in bombs:
			tree.supprimer(x,y)
	else:
		limite = random.randint(1,1000)
		for _ in range(1000):
			x = random.randint(0, 10315)
			y = random.randint(0, 10315)
			bombs.append(x,y)
		print('File {} not found/empty, creating {} random bombs...'.format(nomFichier, limite))
	#for i in aDetruire:
	#	print(i)
		
def jouer():
	ocean = setQuadTreeFromFile('bateaux.txt')
	print(ocean)
	print("Commencer bombardemement")
	bombarder('bombes.txt', ocean)
	print(ocean)
#	ocean.intersect([4,54])

if __name__=='__main__':
	jouer()

		
