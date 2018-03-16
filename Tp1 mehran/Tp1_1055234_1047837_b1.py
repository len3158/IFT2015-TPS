from LinkedQuadTree import LinkedQuadTree
import random
#class Test:
import time
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
		mot = "";
		for line in f.readlines():
			mot += line.rstrip('\n')
		point = mot.split('.')
		bombs = list(point)
		while len(bombs) > 4:
			y2 = int(bombs.pop())
			x2 = int(bombs.pop())
			y1 = int(bombs.pop())
			x1 = int(bombs.pop())
			tree.test_bombes(x1, x2, y1, y2)
			
		# for line in f:
			# #line=(line.strip().split('.'))
			# bombs.append(line.split('.'))
			# lines = file_handle.read().split('\n')
		# f.close()
		# #x1,y1,x2,y2 | [0]=x1, [1]=y1, [2]=x2, [3]=y2
		# for i in range(len(bombs)):
			# x1, y1, x2, y2 = bombs[i][0], bombs[i][1], bombs[i][2], bombs[i][3]
			# # if x1 > x2:
				# # x1, x2 = x2, x1
			# # if y1 > y2:
				# # y1, y2 = y2, y1
			# #tree.test_bombes(x1, x2, y1, y2)
			# print("("+str(x1)+","+str(y1)+")("+str(x2)+","+str(y2)+")")
	else:
		limite = random.randint(1,1000)
		for _ in range(1000):
			x1 = random.randint(0, 10315)
			y1 = random.randint(0, 10315)
			x2 = random.randint(0, 10315)
			y2 = random.randint(0, 10315)
			if x1 > x2:
				x1, x2 = x2, x1
			if y1 > y2:
				y1, y2 = y2, y1
			bombs.append(x1,y1,x2,y2)
		print('File {} not found/empty, creating {} random bombs...'.format(nomFichier, limite))
	#for i in aDetruire:
	#	print(i)
	
def jouer():
	ocean = setQuadTreeFromFile('bateaux.txt')
	print(ocean)
#	print("Commencer bombardemement")
	bombarder('bombes.txt', ocean)
	print(ocean)
#	ocean.intersect([4,54])


""" Lancer l'application sans le test """
if __name__ == '__main__':
	jouer()


def test():
	""" Methode qui test les fonctionnalité du programme """
	if __name__ != '__main__':
		start_time = time.time()
		jouer()
		return time.time() - start_time
		
